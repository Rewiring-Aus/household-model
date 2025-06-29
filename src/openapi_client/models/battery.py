# coding: utf-8

"""
    Household savings

    This is the API for a household savings model. You can provide details about a household's energy use, and receive information about the household's potential emissions & cost savings from electrifying their fossil fuel machines, as well as the upfront costs of switching.

    The version of the OpenAPI document: 0.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt

class Battery(BaseModel):
    """
    The household's home battery system. To have or want to install a battery, you must have or want to install solar. The model does not accept households with battery but no solar.  # noqa: E501
    """
    has_battery: StrictBool = Field(default=..., alias="hasBattery", description="Whether the household has battery")
    capacity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The capacity of the battery system in kWh. Should be null if hasBattery is False and installBattery is False.")
    power_output: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="powerOutput", description="The continuous power output of the battery system in kW. Should be null if hasBattery is False and installBattery is False.")
    peak_power_output: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="peakPowerOutput", description="The peak power output of the battery system in kW. Should be null if hasBattery is False and installBattery is False.")
    install_battery: Optional[StrictBool] = Field(default=None, alias="installBattery", description="Whether the household wants to install a battery. Should be null is hasBattery is True.")
    __properties = ["hasBattery", "capacity", "powerOutput", "peakPowerOutput", "installBattery"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Battery:
        """Create an instance of Battery from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Battery:
        """Create an instance of Battery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Battery.parse_obj(obj)

        _obj = Battery.parse_obj({
            "has_battery": obj.get("hasBattery"),
            "capacity": obj.get("capacity"),
            "power_output": obj.get("powerOutput"),
            "peak_power_output": obj.get("peakPowerOutput"),
            "install_battery": obj.get("installBattery")
        })
        return _obj


