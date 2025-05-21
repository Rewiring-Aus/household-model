from typing import Dict, List, Optional, TypedDict, Union
from constants.fuel_stats import FuelTypeEnum
from openapi_client.models.cooktop_enum import CooktopEnum
from openapi_client.models.space_heating_enum import SpaceHeatingEnum
from openapi_client.models.vehicle_fuel_type_enum import VehicleFuelTypeEnum
from openapi_client.models.water_heating_enum import WaterHeatingEnum
from openapi_client.models.location_enum import LocationEnum 

MachineEnum = SpaceHeatingEnum | WaterHeatingEnum | CooktopEnum | VehicleFuelTypeEnum

class MachineLocationInfo(TypedDict):
    kwh_per_day: Optional[float]  # kWh/day
    emissions_factor: Optional[float]  # kgCO2e/kWh

class MachineInfo(TypedDict):
    fuel_type: FuelTypeEnum  
    per_location: Dict[LocationEnum, MachineLocationInfo]

MachineInfoMap = Dict[MachineEnum, Union[MachineInfo, List[MachineInfo]]]