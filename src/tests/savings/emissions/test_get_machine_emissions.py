import pytest
from unittest import TestCase
from unittest.mock import patch

from openapi_client.models import (
    SpaceHeatingEnum,
    CooktopEnum,
    WaterHeatingEnum,
)

from constants.fuel_stats import EMISSIONS_FACTORS, FuelTypeEnum
from constants.machines.machine_info import MachineInfoMap
from constants.machines.cooktop import COOKTOP_INFO
from constants.machines.water_heating import WATER_HEATING_INFO
from constants.machines.space_heating import SPACE_HEATING_INFO
from constants.utils import PeriodEnum
from openapi_client.models.location_enum import LocationEnum
from savings.emissions.get_machine_emissions import (
    get_appliance_emissions,
    get_emissions_per_day,
    get_other_appliance_emissions,
    get_vehicle_emissions,
)
from tests.mocks import (
    mock_household,
    mock_vehicle_petrol,
    mock_vehicle_diesel,
    mock_vehicle_ev,
    mock_vehicle_hev,
    mock_vehicle_phev,
)

mock_emissions_daily = 12.3
mock_emissions_weekly = 12.3 * 7


class TestGetEmissionsPerDay(TestCase):
    mock_appliance_info: MachineInfoMap = {
        CooktopEnum.GAS: {"fuel_type": FuelTypeEnum.NATURAL_GAS, "per_location": {LocationEnum.NEW_SOUTH_WALES: {"kwh_per_day": 10.0}}},
        SpaceHeatingEnum.ELECTRIC_HEAT_PUMP: {
            "fuel_type": FuelTypeEnum.ELECTRICITY,
            "per_location": {LocationEnum.NEW_SOUTH_WALES: {"kwh_per_day": 5.0}},
        },
    }

    def test_get_emissions_per_day_gas_cooktop(self):
        emissions = get_emissions_per_day(CooktopEnum.GAS, self.mock_appliance_info, LocationEnum.NEW_SOUTH_WALES)
        expected_emissions = 10.0 * EMISSIONS_FACTORS[FuelTypeEnum.NATURAL_GAS]
        assert emissions == expected_emissions

    def test_get_emissions_per_day_electric_heat_pump(self):
        emissions = get_emissions_per_day(
            SpaceHeatingEnum.ELECTRIC_HEAT_PUMP, self.mock_appliance_info, LocationEnum.NEW_SOUTH_WALES
        )
        expected_emissions = 5.0 * EMISSIONS_FACTORS[FuelTypeEnum.ELECTRICITY][LocationEnum.NEW_SOUTH_WALES]
        assert emissions == expected_emissions

    def test_get_emissions_per_day_scaled_by_occupancy(self):
        emissions = get_emissions_per_day(
            SpaceHeatingEnum.ELECTRIC_HEAT_PUMP, self.mock_appliance_info, LocationEnum.NEW_SOUTH_WALES, 3
        )
        expected_emissions = 5.0 * 1.03 * EMISSIONS_FACTORS[FuelTypeEnum.ELECTRICITY][LocationEnum.NEW_SOUTH_WALES]
        assert pytest.approx(emissions) == expected_emissions

    def test_get_emissions_per_day_handles_missing_fuel_type(self):
        mock_appliance_info = {
            CooktopEnum.GAS: {"kwh_per_day": 10.0, "fuel_type": None}
        }
        with self.assertRaises(KeyError):
            get_emissions_per_day(CooktopEnum.GAS, mock_appliance_info, LocationEnum.NEW_SOUTH_WALES)

    def test_get_emissions_per_day_handles_missing_kwh_per_day(self):
        mock_appliance_info = {
            CooktopEnum.GAS: {
                "fuel_type": FuelTypeEnum.NATURAL_GAS,
                "per_location": {LocationEnum.NEW_SOUTH_WALES: {"kwh_per_day": None}},
            }
        }
        with self.assertRaises(TypeError):
            get_emissions_per_day(CooktopEnum.GAS, mock_appliance_info, LocationEnum.NEW_SOUTH_WALES)

    def test_get_emissions_per_day_handles_invalid_machine_type(self):
        invalid_machine_type = CooktopEnum.GAS
        invalid_mock_appliance_info = {}
        with self.assertRaises(KeyError):
            get_emissions_per_day(invalid_machine_type, invalid_mock_appliance_info, LocationEnum.NEW_SOUTH_WALES)


@patch(
    "savings.emissions.get_machine_emissions.scale_daily_to_period",
    return_value=mock_emissions_weekly,
)
@patch(
    "savings.emissions.get_machine_emissions.get_emissions_per_day",
    return_value=mock_emissions_daily,
)
class TestGetApplianceEmissions:
    def test_it_calls_get_emissions_for_space_heating_correctly(
        self, mock_get_emissions_per_day, _
    ):
        get_appliance_emissions(
            mock_household.space_heating, SPACE_HEATING_INFO, LocationEnum.NEW_SOUTH_WALES
        )
        mock_get_emissions_per_day.assert_called_once_with(
            SpaceHeatingEnum.WOOD, SPACE_HEATING_INFO, LocationEnum.NEW_SOUTH_WALES, None
        )

    def test_it_calls_get_emissions_for_water_heating_correctly(
        self, mock_get_emissions_per_day, _
    ):
        get_appliance_emissions(
            mock_household.water_heating, WATER_HEATING_INFO, LocationEnum.NEW_SOUTH_WALES
        )
        mock_get_emissions_per_day.assert_called_once_with(
            WaterHeatingEnum.GAS, WATER_HEATING_INFO, LocationEnum.NEW_SOUTH_WALES, None
        )

    def test_it_calls_get_emissions_for_cooktop_correctly(
        self, mock_get_emissions_per_day, _
    ):
        get_appliance_emissions(
            mock_household.cooktop, COOKTOP_INFO, LocationEnum.NEW_SOUTH_WALES
        )
        mock_get_emissions_per_day.assert_called_once_with(
            CooktopEnum.ELECTRIC_RESISTANCE, COOKTOP_INFO, LocationEnum.NEW_SOUTH_WALES, None
        )

    def test_it_calls_scale_daily_to_period_correctly(
        self, _, mock_scale_daily_to_period
    ):
        get_appliance_emissions(mock_household.cooktop, COOKTOP_INFO, PeriodEnum.WEEKLY)
        mock_scale_daily_to_period.assert_called_once_with(
            mock_emissions_daily, PeriodEnum.DAILY
        )

    def test_it_calls_scale_daily_to_period_correctly_with_default(
        self, _, mock_scale_daily_to_period
    ):
        get_appliance_emissions(
            mock_household.cooktop, COOKTOP_INFO, LocationEnum.NEW_SOUTH_WALES
        )
        mock_scale_daily_to_period.assert_called_once_with(
            mock_emissions_daily, PeriodEnum.DAILY
        )

    def test_it_returns_emissions_per_period(self, _, __):
        result = get_appliance_emissions(
            mock_household.space_heating, SPACE_HEATING_INFO, LocationEnum.NEW_SOUTH_WALES
        )
        assert result == mock_emissions_weekly


@patch(
    "savings.emissions.get_machine_emissions.scale_daily_to_period",
    return_value=mock_emissions_weekly,
)
class TestGetOtherApplianceEmissions:
    emissions_daily = (0.77 + 5.32 + 3.40 + 1.01) * 0.79

    def test_it_calls_scale_daily_to_period_correctly(self, mock_scale_daily_to_period):
        get_other_appliance_emissions(LocationEnum.NEW_SOUTH_WALES, None, PeriodEnum.WEEKLY)
        mock_scale_daily_to_period.assert_called_once_with(
            self.emissions_daily, PeriodEnum.WEEKLY
        )

    def test_it_calls_scale_daily_to_period_correctly_with_default(
        self, mock_scale_daily_to_period
    ):
        get_other_appliance_emissions(LocationEnum.NEW_SOUTH_WALES)
        mock_scale_daily_to_period.assert_called_once_with(
            self.emissions_daily, PeriodEnum.DAILY
        )

    def test_it_returns_emissions_per_period(self, _):
        result = get_other_appliance_emissions(LocationEnum.NEW_SOUTH_WALES)
        assert result == mock_emissions_weekly


def assert_any_call_with_approx(mock, expected_arg0, expected_arg1, tol=1e-6):
    for call in mock.call_args_list:
        arg0, arg1 = call.args
        if abs(arg0 - expected_arg0) < tol and arg1 == expected_arg1:
            return
    raise AssertionError(f"No call found with approx({expected_arg0}) and {expected_arg1}")

class TestGetVehicleEmissionsPerDay(TestCase):
    petrol = 36.7 * 0.24
    ev = 9.4 * 0.79

    def test_it_calculates_daily_emissions_for_one_petrol_car(self):
        result = get_vehicle_emissions([mock_vehicle_petrol], LocationEnum.NEW_SOUTH_WALES)
        assert pytest.approx(result) == self.petrol * (250 / 253.4)

    def test_it_calculates_daily_emissions_for_one_diesel_car(self):
        result = get_vehicle_emissions([mock_vehicle_diesel], LocationEnum.NEW_SOUTH_WALES)
        expected = 29 * 0.25 * (50 / 253.4)
        assert pytest.approx(result) == expected

    def test_it_calculates_daily_emissions_for_one_ev(self):
        result = get_vehicle_emissions([mock_vehicle_ev], LocationEnum.NEW_SOUTH_WALES)
        assert pytest.approx(result) == self.ev * (250 / 253.4)

    def test_it_calculates_daily_emissions_for_one_hybrid(self):
        result = get_vehicle_emissions([mock_vehicle_hev], LocationEnum.NEW_SOUTH_WALES)
        expected = (self.petrol * 0.7 + self.ev * 0.3) * (150 / 253.4)
        assert result == expected

    def test_it_calculates_daily_emissions_for_one_plugin_hybrid(self):
        result = get_vehicle_emissions([mock_vehicle_phev], LocationEnum.NEW_SOUTH_WALES)
        expected = (self.petrol * 0.6 + self.ev * 0.4) * (175 / 253.4)
        assert pytest.approx(result) == expected

    def test_it_combines_vehicles_correctly(self):
        result = get_vehicle_emissions(
            [
                mock_vehicle_petrol,
                mock_vehicle_diesel,
                mock_vehicle_ev,
                mock_vehicle_hev,
                mock_vehicle_phev,
            ],
            LocationEnum.NEW_SOUTH_WALES
        )
        expected = (
            (36.7 * 0.24 * (250 / 253.4))
            + (29 * 0.25 * (50 / 253.4))
            + (9.4 * 0.79 * (250 / 253.4))
            + (self.petrol * 0.7 + self.ev * 0.3) * (150 / 253.4)
            + (self.petrol * 0.6 + self.ev * 0.4) * (175 / 253.4)
        )
        assert pytest.approx(result) == expected

    @patch(
        "savings.emissions.get_machine_emissions.scale_daily_to_period",
    )
    def test_it_calls_scale_daily_to_period_correctly(self, mock_scale_daily_to_period):
        get_vehicle_emissions([mock_vehicle_ev, mock_vehicle_petrol], LocationEnum.NEW_SOUTH_WALES, PeriodEnum.WEEKLY)
        assert len(mock_scale_daily_to_period.call_args_list) == 2
        assert_any_call_with_approx(
            mock_scale_daily_to_period,
            self.petrol * (250 / 253.4),
            PeriodEnum.WEEKLY
        )
        assert_any_call_with_approx(
            mock_scale_daily_to_period,
            self.ev * (250 / 253.4),
            PeriodEnum.WEEKLY
        )

    @patch(
        "savings.emissions.get_machine_emissions.scale_daily_to_period",
    )
    def test_it_calls_scale_daily_to_period_correctly_with_default(
        self, mock_scale_daily_to_period
    ):
        get_vehicle_emissions([mock_vehicle_ev, mock_vehicle_petrol], LocationEnum.NEW_SOUTH_WALES)
        assert len(mock_scale_daily_to_period.call_args_list) == 2
        assert_any_call_with_approx(
            mock_scale_daily_to_period,
            self.petrol * (250 / 253.4),
            PeriodEnum.DAILY
        )
        assert_any_call_with_approx(
            mock_scale_daily_to_period,
            self.ev * (250 / 253.4),
            PeriodEnum.DAILY
        )

    def test_it_returns_emissions_with_default_period(self):
        result = get_vehicle_emissions([mock_vehicle_ev, mock_vehicle_petrol], LocationEnum.NEW_SOUTH_WALES)
        expected = (self.petrol * (250 / 253.4)) + (self.ev * (250 / 253.4))
        assert pytest.approx(result) == expected

    def test_it_returns_emissions_with_specified_period(self):
        result = get_vehicle_emissions(
            [mock_vehicle_ev, mock_vehicle_petrol], LocationEnum.NEW_SOUTH_WALES, PeriodEnum.WEEKLY
        )
        expected = ((self.petrol * (250 / 253.4)) + (self.ev * (250 / 253.4))) * 7
        assert pytest.approx(result) == expected
