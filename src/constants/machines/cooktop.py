from openapi_client.models import CooktopEnum
from constants.fuel_stats import FuelTypeEnum
from constants.machines.machine_info import MachineInfoMap
from openapi_client.models.location_enum import LocationEnum

# kwh_per_day are from values in Machines!B263:L266
COOKTOP_INFO: MachineInfoMap = {
    CooktopEnum.GAS: {
        "fuel_type": FuelTypeEnum.NATURAL_GAS,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 2.20,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 2.14,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 2.21,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 2.32,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 2.07,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 2.34,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 2.26,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 2.35,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 2.17,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
    CooktopEnum.LPG: {
        "fuel_type": FuelTypeEnum.LPG,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 2.20,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 2.14,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 2.21,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 2.32,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 2.07,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 2.34,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 2.26,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 2.35,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 2.17,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
    CooktopEnum.ELECTRIC_RESISTANCE: {
        "fuel_type": FuelTypeEnum.ELECTRICITY,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 0.94,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 0.92,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 0.95,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 0.99,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 0.88,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 1.00,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 0.97,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 1.00,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 0.93,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
    CooktopEnum.ELECTRIC_INDUCTION: {
        "fuel_type": FuelTypeEnum.ELECTRICITY,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 0.85,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 0.83,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 0.86,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 0.90,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 0.80,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 0.91,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 0.87,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 0.91,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 0.84,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
}

# From 'Product prices'!B22:F26
COOKTOP_UPFRONT_COST = {
    CooktopEnum.GAS: {
        "item_price": 700,
        "install_cost": 400,
    },
    CooktopEnum.LPG: {
        "item_price": 700,
        "install_cost": 400,
    },
    CooktopEnum.ELECTRIC_RESISTANCE: {
        "item_price": 600,
        "install_cost": 400,
    },
    CooktopEnum.ELECTRIC_INDUCTION: {
        "item_price": 1400,
        "install_cost": 600,
    },
}
