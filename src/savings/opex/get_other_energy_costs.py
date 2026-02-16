from constants.fuel_stats import COST_PER_FUEL_KWH_AVG_15_YEARS, COST_PER_FUEL_KWH_TODAY, FuelTypeEnum
from constants.utils import PeriodEnum
from openapi_client.models.location_enum import LocationEnum
from savings.energy.get_other_energy_consumption import (
    OtherEnergyConsumption,
)


def get_other_energy_costs(
    other_e_consumption: OtherEnergyConsumption,
    period: PeriodEnum,
    location: LocationEnum,
) -> float:
    """Get energy costs for fuels other than electricity (e.g. gas, LPG, petrol, diesel)

    Args:
        other_e_consumption (OtherEnergyConsumption): dict with kWh of energy use per fuel type
        period (PeriodEnum): the period for which this calculation is over

    Returns:
        float: cost in NZD
    """
    total = 0
    costs = (
        COST_PER_FUEL_KWH_AVG_15_YEARS
        if period == PeriodEnum.OPERATIONAL_LIFETIME
        else COST_PER_FUEL_KWH_TODAY
    )
    for fuel_type, energy in other_e_consumption.items():
        total += energy * costs[fuel_type][location]
    return total


def get_other_energy_costs_by_fuel_type(
    other_e_consumption: OtherEnergyConsumption,
    period: PeriodEnum,
    location: LocationEnum,
) -> dict:
    """Get energy costs for fuels other than electricity (e.g. gas, LPG, petrol, diesel)

    Args:
        other_e_consumption (OtherEnergyConsumption): dict with kWh of energy use per fuel type
        period (PeriodEnum): the period for which this calculation is over

    Returns:
        dict: cost in NZD per fuel type
    """
    costs = (
        COST_PER_FUEL_KWH_AVG_15_YEARS
        if period == PeriodEnum.OPERATIONAL_LIFETIME
        else COST_PER_FUEL_KWH_TODAY
    )
    return {
        "gas" if fuel_type == FuelTypeEnum.NATURAL_GAS else fuel_type.value: other_e_consumption[fuel_type] * costs[fuel_type][location]
        for fuel_type in other_e_consumption.keys()
    }