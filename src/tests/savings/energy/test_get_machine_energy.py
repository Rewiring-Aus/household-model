from unittest import TestCase
from unittest.mock import patch

import pytest

from constants.machines.vehicles import VEHICLE_INFO
from openapi_client.models import (
    SpaceHeatingEnum,
    CooktopEnum,
)

from constants.fuel_stats import (
    FuelTypeEnum,
)
from constants.machines.machine_info import MachineInfoMap
from constants.machines.cooktop import COOKTOP_INFO
from constants.machines.space_heating import SPACE_HEATING_INFO
from constants.utils import PeriodEnum
from openapi_client.models.location_enum import LocationEnum
from openapi_client.models.vehicle_fuel_type_enum import VehicleFuelTypeEnum
from savings.energy.get_machine_energy import (
    get_energy_per_day,
    get_energy_per_period,
    get_other_appliances_energy_per_period,
    get_total_appliance_energy,
    get_vehicle_energy,
)
from tests.mocks import (
    mock_household,
    mock_vehicle_petrol,
    mock_vehicle_diesel,
    mock_vehicle_ev,
    mock_vehicle_hev,
    mock_vehicle_phev,
)

mock_energy_daily = {
    FuelTypeEnum.ELECTRICITY: 2.5,
}
mock_energy_weekly = {
    FuelTypeEnum.ELECTRICITY: 17.5,  # 12.345 * 7
}


class TestGetEnergyPerDay(TestCase):
    mock_appliance_info: MachineInfoMap = {
        CooktopEnum.GAS: {"fuel_type": FuelTypeEnum.NATURAL_GAS, "per_location": {
            LocationEnum.NEW_SOUTH_WALES: {"kwh_per_day": 10.0},
        }},
        SpaceHeatingEnum.ELECTRIC_HEAT_PUMP: {
            "fuel_type": FuelTypeEnum.ELECTRICITY,
            "per_location": {
                LocationEnum.NEW_SOUTH_WALES: {"kwh_per_day": 5.0},
            },
        },
    }

    def test_get_energy_per_day(self):
        assert get_energy_per_day(CooktopEnum.GAS, self.mock_appliance_info, LocationEnum.NEW_SOUTH_WALES) == {
            FuelTypeEnum.NATURAL_GAS: 10
        }
        assert get_energy_per_day(
            SpaceHeatingEnum.ELECTRIC_HEAT_PUMP, self.mock_appliance_info, LocationEnum.NEW_SOUTH_WALES
        ) == {FuelTypeEnum.ELECTRICITY: 5.0}

    def test_get_energy_per_day_multiple_fuels(self):
        assert get_energy_per_day(VehicleFuelTypeEnum.HYBRID, VEHICLE_INFO, LocationEnum.NEW_SOUTH_WALES) == {
            FuelTypeEnum.PETROL: 36.7 * 0.7,
            FuelTypeEnum.ELECTRICITY: 9.4 * 0.3,
        }
        assert get_energy_per_day(VehicleFuelTypeEnum.PLUG_IN_HYBRID, VEHICLE_INFO, LocationEnum.NEW_SOUTH_WALES) == {
            FuelTypeEnum.PETROL: 36.7 * 0.6,
            FuelTypeEnum.ELECTRICITY: 9.4 * 0.4,
        }

    def test_get_energy_per_day_handles_missing_kwh_per_day(self):
        mock_appliance_info = {
            CooktopEnum.GAS: {
                "fuel_type": FuelTypeEnum.NATURAL_GAS,
                "per_location": {
                    LocationEnum.NEW_SOUTH_WALES: {"kwh_per_day": None},
                },
            }
        }
        with self.assertRaises(ValueError):
            get_energy_per_day(CooktopEnum.GAS, mock_appliance_info, LocationEnum.NEW_SOUTH_WALES)

    def test_get_energy_per_day_handles_invalid_machine_type(self):
        invalid_machine_type = CooktopEnum.GAS
        invalid_mock_appliance_info = {}
        with self.assertRaises(KeyError):
            get_energy_per_day(invalid_machine_type, invalid_mock_appliance_info, LocationEnum.NEW_SOUTH_WALES)


@patch(
    "savings.energy.get_machine_energy.scale_daily_to_period",
    return_value=mock_energy_weekly[FuelTypeEnum.ELECTRICITY],
)
@patch(
    "savings.energy.get_machine_energy.get_energy_per_day",
    return_value=mock_energy_daily,
)
class TestGetEnergyPerPeriod:
    def test_it_calls_get_energy_per_day_correctly(self, mock_get_energy_per_day, _):
        get_energy_per_period(
            mock_household.space_heating,
            SPACE_HEATING_INFO,
            LocationEnum.NEW_SOUTH_WALES,
            1,
            PeriodEnum.DAILY,
        )
        mock_get_energy_per_day.assert_called_once_with(
            SpaceHeatingEnum.WOOD, SPACE_HEATING_INFO, LocationEnum.NEW_SOUTH_WALES, 1
        )

    def test_it_calls_get_energy_per_day_correctly_with_defaults(
        self, mock_get_energy_per_day, _
    ):
        get_energy_per_period(
            mock_household.space_heating,
            SPACE_HEATING_INFO,
            LocationEnum.NEW_SOUTH_WALES,
        )
        mock_get_energy_per_day.assert_called_once_with(
            SpaceHeatingEnum.WOOD, SPACE_HEATING_INFO, LocationEnum.NEW_SOUTH_WALES, None
        )

    def test_it_calls_scale_daily_to_period_correctly(
        self, _, mock_scale_daily_to_period
    ):
        get_energy_per_period(
            mock_household.cooktop,
            COOKTOP_INFO,
            LocationEnum.NEW_SOUTH_WALES,
            1,
            PeriodEnum.WEEKLY,
        )
        mock_scale_daily_to_period.assert_called_once_with(
            mock_energy_daily[FuelTypeEnum.ELECTRICITY], PeriodEnum.WEEKLY
        )

    def test_it_calls_scale_daily_to_period_correctly_with_default(
        self, _, mock_scale_daily_to_period
    ):
        get_energy_per_period(
            mock_household.cooktop,
            COOKTOP_INFO,
            LocationEnum.NEW_SOUTH_WALES,
        )
        mock_scale_daily_to_period.assert_called_once_with(
            mock_energy_daily[FuelTypeEnum.ELECTRICITY], PeriodEnum.DAILY
        )

    def test_it_calls_scale_daily_to_period_per_fuel_type(
        self, mock_get_energy_per_day, mock_scale_daily_to_period
    ):
        mock_get_energy_per_day.side_effect = [
            {
                FuelTypeEnum.ELECTRICITY: 2,
                FuelTypeEnum.PETROL: 3,
            }
        ]

        get_energy_per_period(
            mock_household.cooktop,
            COOKTOP_INFO,
            LocationEnum.NEW_SOUTH_WALES,
        )
        assert len(mock_scale_daily_to_period.call_args_list) == 2
        mock_scale_daily_to_period.assert_any_call(2, PeriodEnum.DAILY)
        mock_scale_daily_to_period.assert_any_call(3, PeriodEnum.DAILY)

    def test_it_returns_energy_per_period(self, _, __):
        result = get_energy_per_period(
            mock_household.space_heating,
            SPACE_HEATING_INFO,
            LocationEnum.NEW_SOUTH_WALES,
        )
        assert result == mock_energy_weekly


@patch(
    "savings.energy.get_machine_energy.get_energy_per_period",
    side_effect=[
        {
            FuelTypeEnum.ELECTRICITY: 1,
            FuelTypeEnum.NATURAL_GAS: 5,
            FuelTypeEnum.LPG: 3,
            FuelTypeEnum.WOOD: 4,
            FuelTypeEnum.PETROL: 0.5,
            FuelTypeEnum.DIESEL: 7,
        },
        {
            FuelTypeEnum.ELECTRICITY: 2,
            FuelTypeEnum.NATURAL_GAS: 10,
            FuelTypeEnum.LPG: 6,
            FuelTypeEnum.WOOD: 4.5,
            FuelTypeEnum.PETROL: 0.5,
            FuelTypeEnum.DIESEL: 8,
        },
        {
            FuelTypeEnum.ELECTRICITY: 3,
            FuelTypeEnum.NATURAL_GAS: 15,
            FuelTypeEnum.LPG: 9,
            FuelTypeEnum.WOOD: 5,
            FuelTypeEnum.PETROL: 0.5,
            FuelTypeEnum.DIESEL: 9,
        },
    ],
)
class TestGetTotalApplianceEnergy:
    def test_it_combines_fuel_types_correctly(self, mock_get_energy_per_period):
        result = get_total_appliance_energy(
            mock_household, PeriodEnum.DAILY, LocationEnum.NEW_SOUTH_WALES
        )
        expected = {
            FuelTypeEnum.ELECTRICITY: 6,
            FuelTypeEnum.NATURAL_GAS: 30,
            FuelTypeEnum.LPG: 18,
            FuelTypeEnum.WOOD: 13.5,
            FuelTypeEnum.PETROL: 1.5,
            FuelTypeEnum.DIESEL: 24,
        }
        assert result == expected

    def test_it_works_if_fuel_types_missing(self, mock_get_energy_per_period):
        mock_get_energy_per_period.side_effect = [
            {
                FuelTypeEnum.ELECTRICITY: 1,
                FuelTypeEnum.NATURAL_GAS: 0,
                FuelTypeEnum.LPG: 0,
                FuelTypeEnum.WOOD: 0,
                # FuelTypeEnum.PETROL: 0.5,
                # FuelTypeEnum.DIESEL: 7,
            },
            {
                FuelTypeEnum.ELECTRICITY: 2,
                FuelTypeEnum.NATURAL_GAS: 0,
                FuelTypeEnum.LPG: 0,
                FuelTypeEnum.WOOD: 0,
                FuelTypeEnum.PETROL: 0.5,
                # FuelTypeEnum.DIESEL: 8,
            },
            {
                FuelTypeEnum.ELECTRICITY: 3,
                FuelTypeEnum.NATURAL_GAS: 0,
                FuelTypeEnum.LPG: 0,
                FuelTypeEnum.WOOD: 0,
                FuelTypeEnum.PETROL: 0.5,
                # FuelTypeEnum.DIESEL: 9,
            },
        ]
        result = get_total_appliance_energy(
            mock_household, PeriodEnum.DAILY, LocationEnum.NEW_SOUTH_WALES
        )
        expected = {
            FuelTypeEnum.ELECTRICITY: 6,
            FuelTypeEnum.NATURAL_GAS: 0,
            FuelTypeEnum.LPG: 0,
            FuelTypeEnum.WOOD: 0,
            FuelTypeEnum.PETROL: 1.0,
            FuelTypeEnum.DIESEL: 0,  # Still includes a key for it with zero value
        }
        assert result == expected


@patch(
    "savings.energy.get_machine_energy.scale_daily_to_period",
    return_value=mock_energy_weekly[FuelTypeEnum.ELECTRICITY],
)
@patch(
    "savings.energy.get_machine_energy.scale_energy_by_occupancy",
    return_value=mock_energy_daily[FuelTypeEnum.ELECTRICITY],
)
class TestGetOtherAppliancesEnergyPerPeriod:
    energy = 0.77 + 5.32 + 3.40 + 1.01

    def test_it_calls_scale_energy_by_occupancy_correctly(
        self, mock_scale_energy_by_occupancy, mock_scale_daily_to_period
    ):
        get_other_appliances_energy_per_period(LocationEnum.NEW_SOUTH_WALES, 1, PeriodEnum.WEEKLY)
        mock_scale_energy_by_occupancy.assert_called_once_with(self.energy, 1)

    def test_it_calls_scale_energy_by_occupancy_correctly_with_default(
        self, mock_scale_energy_by_occupancy, mock_scale_daily_to_period
    ):
        get_other_appliances_energy_per_period(LocationEnum.NEW_SOUTH_WALES)
        mock_scale_energy_by_occupancy.assert_called_once_with(self.energy, None)

    def test_it_calls_scale_daily_to_period_correctly(
        self, mock_scale_energy_by_occupancy, mock_scale_daily_to_period
    ):
        get_other_appliances_energy_per_period(LocationEnum.NEW_SOUTH_WALES, None, PeriodEnum.WEEKLY)
        mock_scale_daily_to_period.assert_called_once_with(
            mock_energy_daily[FuelTypeEnum.ELECTRICITY], PeriodEnum.WEEKLY
        )

    def test_it_calls_scale_daily_to_period_correctly_with_default(
        self, mock_scale_energy_by_occupancy, mock_scale_daily_to_period
    ):
        get_other_appliances_energy_per_period(LocationEnum.NEW_SOUTH_WALES)
        mock_scale_daily_to_period.assert_called_once_with(
            mock_energy_daily[FuelTypeEnum.ELECTRICITY], PeriodEnum.DAILY
        )

    def test_it_returns_energy_per_period(self, _, __):
        assert get_other_appliances_energy_per_period(
            LocationEnum.NEW_SOUTH_WALES, 1, PeriodEnum.WEEKLY
        ) == {
            FuelTypeEnum.ELECTRICITY: 17.5
        }
        assert get_other_appliances_energy_per_period(
            LocationEnum.NEW_SOUTH_WALES
        ) == {
            FuelTypeEnum.ELECTRICITY: 17.5
        }


def assert_any_call_with_approx(mock, expected_arg0, expected_arg1, tol=1e-6):
    for call in mock.call_args_list:
        arg0, arg1 = call.args
        if abs(arg0 - expected_arg0) < tol and arg1 == expected_arg1:
            return
    raise AssertionError(f"No call found with approx({expected_arg0}) and {expected_arg1}")

class TestGetVehicleEnergyPerDay(TestCase):
    # kWh per day for average mileage
    petrol = 36.7
    ev = 9.4

    expected_weighted_energy_daily_petrol = petrol * (250 / 253.4)
    expected_weighted_energy_daily_ev = ev * (250 / 253.4)

    def test_it_calculates_daily_energy_for_one_petrol_car(self):
        result = get_vehicle_energy(
            [mock_vehicle_petrol], LocationEnum.NEW_SOUTH_WALES
        )
        assert result[FuelTypeEnum.PETROL] == pytest.approx(self.expected_weighted_energy_daily_petrol)

    def test_it_calculates_daily_energy_for_one_diesel_car(self):
        result = get_vehicle_energy(
            [mock_vehicle_diesel], LocationEnum.NEW_SOUTH_WALES
        )
        expected = 29 * 50 / 253.4
        assert result[FuelTypeEnum.DIESEL] == pytest.approx(expected)

    def test_it_calculates_daily_energy_for_one_ev(self):
        result = get_vehicle_energy(
            [mock_vehicle_ev], LocationEnum.NEW_SOUTH_WALES
        )
        assert result[FuelTypeEnum.ELECTRICITY] == pytest.approx(self.ev * (250 / 253.4))

    def test_it_calculates_daily_energy_for_one_hybrid(self):
        result = get_vehicle_energy(
            [mock_vehicle_hev], LocationEnum.NEW_SOUTH_WALES
        )
        weighting_factor = 150 / 253.4
        expected = {
            FuelTypeEnum.PETROL: self.petrol * 0.7 * weighting_factor,
            FuelTypeEnum.ELECTRICITY: self.ev * 0.3 * weighting_factor,
        }
        assert result == expected

    def test_it_calculates_daily_energy_for_one_plugin_hybrid(self):
        result = get_vehicle_energy(
            [mock_vehicle_phev], LocationEnum.NEW_SOUTH_WALES
        )
        weighting_factor = 175 / 253.4
        expected = {
            FuelTypeEnum.PETROL: self.petrol * 0.6 * weighting_factor,
            FuelTypeEnum.ELECTRICITY: self.ev * 0.4 * weighting_factor,
        }
        assert result[FuelTypeEnum.PETROL] == pytest.approx(expected[FuelTypeEnum.PETROL])
        assert result[FuelTypeEnum.ELECTRICITY] == pytest.approx(expected[FuelTypeEnum.ELECTRICITY])

    def test_it_combines_vehicles_correctly(self):
        result = get_vehicle_energy(
            [
                mock_vehicle_petrol,
                mock_vehicle_diesel,
                mock_vehicle_ev,
                mock_vehicle_hev,
                mock_vehicle_phev,
            ],
            LocationEnum.NEW_SOUTH_WALES,
        )
        expected = {
            FuelTypeEnum.PETROL: (36.7 * (250 / 253.4))  # petrol
            + (self.petrol * 0.7 * (150 / 253.4))  # HEV
            + (self.petrol * 0.6 * (175 / 253.4)),  # PHEV
            FuelTypeEnum.DIESEL: (29 * (50 / 253.4)),  # diesel
            FuelTypeEnum.ELECTRICITY: (9.4 * (250 / 253.4))  # EV
            + (self.ev * 0.3 * (150 / 253.4))  # HEV
            + (self.ev * 0.4 * (175 / 253.4)),  # PHEV
        }
        assert result[FuelTypeEnum.PETROL] == pytest.approx(expected[FuelTypeEnum.PETROL])
        assert result[FuelTypeEnum.DIESEL] == pytest.approx(expected[FuelTypeEnum.DIESEL])
        assert result[FuelTypeEnum.ELECTRICITY] == pytest.approx(expected[FuelTypeEnum.ELECTRICITY])

    @patch(
        "savings.energy.get_machine_energy.scale_daily_to_period",
    )
    def test_it_calls_scale_daily_to_period_correctly(self, mock_scale_daily_to_period):

        get_vehicle_energy(
            [mock_vehicle_ev, mock_vehicle_petrol],
            LocationEnum.NEW_SOUTH_WALES,
            PeriodEnum.WEEKLY,
        )

        assert len(mock_scale_daily_to_period.call_args_list) == 2
        assert_any_call_with_approx(
            mock_scale_daily_to_period,
            self.expected_weighted_energy_daily_petrol,
            PeriodEnum.WEEKLY,
        )
        assert_any_call_with_approx(
            mock_scale_daily_to_period,
            self.expected_weighted_energy_daily_ev,
            PeriodEnum.WEEKLY
        )

    @patch(
        "savings.energy.get_machine_energy.scale_daily_to_period",
    )
    def test_it_calls_scale_daily_to_period_correctly_with_default(
        self, mock_scale_daily_to_period
    ):
        get_vehicle_energy(
            [mock_vehicle_ev, mock_vehicle_petrol],
            LocationEnum.NEW_SOUTH_WALES,
        )
        assert len(mock_scale_daily_to_period.call_args_list) == 2
        assert_any_call_with_approx(
            mock_scale_daily_to_period,
            self.expected_weighted_energy_daily_petrol,
            PeriodEnum.DAILY,
        )
        assert_any_call_with_approx(
            mock_scale_daily_to_period,
            self.expected_weighted_energy_daily_ev,
            PeriodEnum.DAILY
        )

    def test_it_returns_energy_with_default_period(self):
        result = get_vehicle_energy(
            [mock_vehicle_ev, mock_vehicle_petrol],
            LocationEnum.NEW_SOUTH_WALES,
        )

        assert pytest.approx(result) == {
            FuelTypeEnum.PETROL: self.expected_weighted_energy_daily_petrol,
            FuelTypeEnum.ELECTRICITY: self.expected_weighted_energy_daily_ev,
        }

    def test_it_returns_energy_with_specified_period(self):
        result = get_vehicle_energy(
            [mock_vehicle_ev, mock_vehicle_petrol],
            LocationEnum.NEW_SOUTH_WALES,
            PeriodEnum.WEEKLY,
        )
        expected = {
            FuelTypeEnum.PETROL: self.expected_weighted_energy_daily_petrol * 7,
            FuelTypeEnum.ELECTRICITY: self.expected_weighted_energy_daily_ev * 7,
        }
        assert pytest.approx(result) == expected
