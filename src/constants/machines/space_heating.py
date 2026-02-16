from openapi_client.models import SpaceHeatingEnum
from constants.fuel_stats import FuelTypeEnum
from constants.machines.machine_info import MachineInfoMap
from openapi_client.models.location_enum import LocationEnum

# kwh_per_day are from values in Machines!B54:L60

SPACE_HEATING_INFO: MachineInfoMap = {
    SpaceHeatingEnum.WOOD: {
        "fuel_type": FuelTypeEnum.WOOD,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 35.91,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 13.99,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 1.71,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 48.00,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 41.42,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 12.12,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 16.89,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 7.93,
            },
        },
    },
    SpaceHeatingEnum.GAS: {
        "fuel_type": FuelTypeEnum.NATURAL_GAS,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 29.18,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 11.36,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 1.39,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 39.00,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 33.65,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 9.84,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 13.72,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 6.44,
            },
        },
    },
    SpaceHeatingEnum.LPG: {
        "fuel_type": FuelTypeEnum.LPG,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 29.18,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 11.36,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 1.39,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 39.00,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 33.65,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 9.84,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 13.72,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 6.44,
            },
        },
    },
    SpaceHeatingEnum.DIESEL: {
        "fuel_type": FuelTypeEnum.DIESEL,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 0,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 0,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 0,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 0,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 0,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 0,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 0,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 0,
            },
        },
    },
    SpaceHeatingEnum.ELECTRIC_RESISTANCE: {
        "fuel_type": FuelTypeEnum.ELECTRICITY,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 23.34,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 9.09,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 1.11,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 31.20,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 26.92,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 7.87,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 10.98,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 5.16,
            },
        },
    },
    SpaceHeatingEnum.ELECTRIC_HEAT_PUMP: {
        "fuel_type": FuelTypeEnum.ELECTRICITY,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 6.007,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 2.273,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 0.263,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 8.531,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 7.362,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 1.969,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 2.745,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 1.253,
            },
        },
    },
}

# From 'Product Prices'!B7:F13
SPACE_HEATING_UPFRONT_COST = {
    SpaceHeatingEnum.ELECTRIC_HEAT_PUMP: {
        "item_price": 1700,
        "install_cost": 900,
    },
    # Everything else below here is kind of irrelevant, since we'll only ever be recommending heat pumps
    SpaceHeatingEnum.GAS: {
        "item_price": 1740,
        "install_cost": 500,
    },
    SpaceHeatingEnum.LPG: {
        "item_price": 1740,
        "install_cost": 500,
    },
    SpaceHeatingEnum.WOOD: {
        "item_price": 1400,
        "install_cost": 1000,
    },
    SpaceHeatingEnum.ELECTRIC_RESISTANCE: {
        # Need to update, but low priority because we'd never recommend it over heat pumps
        "item_price": 220,
        "install_cost": 0,
    },
}

# From 'Location data'!A2:J2
N_HEAT_PUMPS_NEEDED_PER_LOCATION = {
    LocationEnum.VICTORIA: 3,
    LocationEnum.NEW_SOUTH_WALES: 2,
    LocationEnum.NORTHERN_TERRITORY: 1,
    LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 3,
    LocationEnum.TASMANIA: 3,
    LocationEnum.WESTERN_AUSTRALIA: 2,
    LocationEnum.SOUTH_AUSTRALIA: 2,
    LocationEnum.QUEENSLAND: 1,
}
