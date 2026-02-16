import pytest
from constants.fuel_stats import FuelTypeEnum
from constants.utils import PeriodEnum
from openapi_client.models.location_enum import LocationEnum
from savings.opex.get_other_energy_costs import get_other_energy_costs


def test_it_merges_correctly():
    e_consmpt = {
        FuelTypeEnum.NATURAL_GAS: 2000.0,
        FuelTypeEnum.PETROL: 6000.0,
        FuelTypeEnum.DIESEL: 2500.0,
    }
    result = get_other_energy_costs(e_consmpt, PeriodEnum.DAILY, LocationEnum.NEW_SOUTH_WALES)
    expected = 2000.0 * 0.153 + 6000.0 * 0.200 + 2500.0 * 0.18
    assert result == expected


@pytest.mark.parametrize(
    "period,expected",
    [
        (PeriodEnum.DAILY, 500.0 * 0.153 + 1000.0 * 0.200),
        (PeriodEnum.WEEKLY, 500.0 * 0.153 + 1000.0 * 0.200),
        (PeriodEnum.YEARLY, 500.0 * 0.153 + 1000.0 * 0.200),
        (PeriodEnum.OPERATIONAL_LIFETIME, 500.0 * 0.19 + 1000.0 * 0.22),
    ],
)
def test_it_uses_correct_pricing(period, expected):
    e_consmpt = {
        FuelTypeEnum.NATURAL_GAS: 500.0,
        FuelTypeEnum.PETROL: 1000.0,
    }
    assert get_other_energy_costs(e_consmpt, period, LocationEnum.NEW_SOUTH_WALES) == expected
