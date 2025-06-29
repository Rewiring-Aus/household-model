from typing import Dict, List, Optional, TypedDict

from constants.fuel_stats import FuelTypeEnum
from constants.machines.cooktop import COOKTOP_INFO
from constants.machines.space_heating import (
    SPACE_HEATING_INFO,
)
from constants.machines.water_heating import WATER_HEATING_INFO
from constants.machines.machine_info import MachineEnum, MachineInfoMap
from constants.machines.other_machines import ENERGY_NEEDS_OTHER_MACHINES_PER_DAY
from constants.machines.vehicles import (
    VEHICLE_AVG_KMS_PER_WEEK,
    VEHICLE_INFO,
)
from constants.utils import PeriodEnum
from openapi_client.models.location_enum import LocationEnum
from openapi_client.models.space_heating_enum import SpaceHeatingEnum
from savings.energy.scale_energy_by_occupancy import scale_energy_by_occupancy
from utils.scale_daily_to_period import scale_daily_to_period

from openapi_client.models import Vehicle, Household
from utils.sum_dicts import sum_dicts


class MachineEnergyNeeds(TypedDict):
    appliances: Dict[FuelTypeEnum, float]
    vehicles: Dict[FuelTypeEnum, float]
    other_appliances: Dict[FuelTypeEnum, float]


def get_total_energy_needs(
    household: Household,
    period: PeriodEnum,
    location: LocationEnum,
) -> MachineEnergyNeeds:
    appliance_energy = get_total_appliance_energy(household, period, location)
    vehicle_energy = get_vehicle_energy(household.vehicles, location, period)
    other_energy = get_other_appliances_energy_per_period(
        location, household.occupancy, period
    )
    return {
        "appliances": appliance_energy,
        "vehicles": vehicle_energy,
        "other_appliances": other_energy,
    }


def get_energy_per_day(
    machine_type: MachineEnum,
    machine_stats_map: MachineInfoMap,
    location: LocationEnum,
    occupancy: Optional[int] = None,
) -> Dict[FuelTypeEnum, float]:
    """Get energy needs per day for a given machine

    Args:
        machine_type (MachineEnum): the type of machine, e.g. a gas cooktop
        machine_stats_map (MachineInfoMap): info about the machine's energy use per day and its fuel type
        occupancy (int, optional): The number of people in the household.
        location (LocationEnum, optional): The location of the machine (for determining heating needs)

    Returns:
        Dict[FuelTypeEnum, float]: machine's energy needs per day per fuel type
    """
    machine_infos = machine_stats_map[machine_type]
    if type(machine_stats_map[machine_type]) != list:
        machine_infos = [machine_infos]

    e_fuel_type = {}

    for machine_info in machine_infos:
        e_daily = machine_info["per_location"][location]["kwh_per_day"]
        if e_daily is None:
            raise ValueError(f"Can not find kwh_per_day value for {machine_type}")

        fuel_type = machine_info["fuel_type"]
        if fuel_type is None:
            raise ValueError(f"Can not find fuel type value for {machine_type}")

        e_daily_scaled = scale_energy_by_occupancy(e_daily, occupancy)
        e_fuel_type[fuel_type] = e_daily_scaled

    return e_fuel_type


def get_energy_per_period(
    machine: MachineEnum,
    machine_info: MachineInfoMap,
    location: LocationEnum,
    occupancy: Optional[int] = None,
    period: PeriodEnum = PeriodEnum.DAILY,
) -> Dict[FuelTypeEnum, float]:
    """Calculates the energy needs of machines in given household over given period

    Args:
        machine (MachineEnum): the machine
        machine_info (MachineInfoMap): info about the machine's energy use per day and its fuel type
        occupancy (int, optional): The number of people in the household. Defaults to None.
        period (PeriodEnum, optional): the period over which to calculate the energy use. Defaults to PeriodEnum.DAILY.
        location (LocationEnum, optional): The location of the machine (for determining heating needs)

    Returns:
        Dict[FuelTypeEnum, float]: energy needs per fuel type of operating machine over given period in kWh
    """
    e_daily = get_energy_per_day(machine, machine_info, location, occupancy)
    e_daily_scaled = {
        fuel_type: scale_daily_to_period(e, period) for fuel_type, e in e_daily.items()
    }
    return e_daily_scaled


def get_total_appliance_energy(
    household: Household,
    period: PeriodEnum,
    location: LocationEnum,
) -> Dict[FuelTypeEnum, float]:

    if household.space_heating == SpaceHeatingEnum.NONE:
        space_heating_energy = {FuelTypeEnum.NONE: 0}

    else:
        space_heating_energy = get_energy_per_period(
            household.space_heating,
            SPACE_HEATING_INFO,
            location,
            household.occupancy,
            period,
        )
    water_heating_energy = get_energy_per_period(
        household.water_heating,
        WATER_HEATING_INFO,
        location,
        household.occupancy,
        period,
    )
    cooktop_energy = get_energy_per_period(
        household.cooktop,
        COOKTOP_INFO,
        location,
        household.occupancy,
        period,
    )
    energy_dict = {}
    for fuel in FuelTypeEnum:
        if fuel == FuelTypeEnum.NONE: # Exclude none fuel type coming from "no space heating" option
            continue
        # Exclude solar because the energy consumed from solar is calculated separately
        if fuel != FuelTypeEnum.SOLAR:
            energy_dict[fuel] = energy_dict.get(fuel, 0) + space_heating_energy.get(
                fuel, 0
            )
            energy_dict[fuel] += water_heating_energy.get(fuel, 0)
            energy_dict[fuel] += cooktop_energy.get(fuel, 0)

    return energy_dict


def get_vehicle_energy(
    vehicles: List[Vehicle],
    location: LocationEnum,
    period: PeriodEnum = PeriodEnum.DAILY,
) -> float:
    """Calculates the energy of a list of vehicles

    Args:
        vehicles (List[Vehicle]): the list of vehicles
        period (PeriodEnum, optional): the period over which to calculate the energy. Calculations over a longer period of time (e.g. 15 years) should use this feature, as there may be external economic factors which impact the result, making it different to simply multiplying the daily energy value. Defaults to PeriodEnum.DAILY.

    Returns:
        Dict[FuelTypeEnum, float]: total energy required from vehicles over given period per fuel type
    """
    total_energy = {}
    for vehicle in vehicles:
        avg_e_daily = get_energy_per_day(
            vehicle.fuel_type,
            VEHICLE_INFO,
            location,
        )

        # Weight the energy based on how much they use the vehicle compared to average
        weighting_factor = vehicle.kms_per_week / VEHICLE_AVG_KMS_PER_WEEK[location]
        weighted_e_daily = {
            fuel_type: e * weighting_factor for fuel_type, e in avg_e_daily.items()
        }

        # Convert to given period
        weighted_e_daily_scaled = {
            fuel_type: scale_daily_to_period(e, period)
            for fuel_type, e in weighted_e_daily.items()
        }

        # Add to totals
        total_energy = sum_dicts([total_energy, weighted_e_daily_scaled])
    return total_energy


def get_other_appliances_energy_per_period(
    location: LocationEnum,
    occupancy: Optional[int] = None,
    period: PeriodEnum = PeriodEnum.DAILY,
) -> Dict[FuelTypeEnum, float]:
    """Calculates the energy of other appliances in a household
    These may include space cooling (fans, aircon), refrigeration, laundry, lighting, etc.
    We assume that these are all electric.

    Args:
        occupancy (int, optional): The number of people in the household. Defaults to None.
        period (PeriodEnum, optional): the period over which to calculate the energy. Calculations over a longer period of time (e.g. 15 years) should use this feature, as there may be external economic factors which impact the result, making it different to simply multiplying the daily energy value. Defaults to PeriodEnum.DAILY.

    Returns:
        Dict[FuelTypeEnum, float]: energy of operating other appliances over given period per fuel type
    """
    e_daily = {
        FuelTypeEnum.ELECTRICITY: scale_energy_by_occupancy(
            ENERGY_NEEDS_OTHER_MACHINES_PER_DAY[location]["kwh_per_day"], occupancy
        )
    }
    e_daily_scaled = {
        fuel_type: scale_daily_to_period(e, period) for fuel_type, e in e_daily.items()
    }
    return e_daily_scaled
