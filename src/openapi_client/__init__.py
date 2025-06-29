# coding: utf-8

# flake8: noqa

"""
    Household savings

    This is the API for a household savings model. You can provide details about a household's energy use, and receive information about the household's potential emissions & cost savings from electrifying their fossil fuel machines, as well as the upfront costs of switching.

    The version of the OpenAPI document: 0.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.savings_api import SavingsApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.battery import Battery
from openapi_client.models.cooktop_enum import CooktopEnum
from openapi_client.models.emissions import Emissions
from openapi_client.models.emissions_values import EmissionsValues
from openapi_client.models.household import Household
from openapi_client.models.location_enum import LocationEnum
from openapi_client.models.opex import Opex
from openapi_client.models.opex_values import OpexValues
from openapi_client.models.opex_weekly import OpexWeekly
from openapi_client.models.opex_weekly_fixed_costs_by_fuel_type import OpexWeeklyFixedCostsByFuelType
from openapi_client.models.opex_weekly_other_energy_costs_by_fuel_type import OpexWeeklyOtherEnergyCostsByFuelType
from openapi_client.models.recommendation import Recommendation
from openapi_client.models.recommendation_action_enum import RecommendationActionEnum
from openapi_client.models.savings import Savings
from openapi_client.models.solar import Solar
from openapi_client.models.space_heating_enum import SpaceHeatingEnum
from openapi_client.models.upfront_cost import UpfrontCost
from openapi_client.models.vehicle import Vehicle
from openapi_client.models.vehicle_fuel_type_enum import VehicleFuelTypeEnum
from openapi_client.models.water_heating_enum import WaterHeatingEnum
