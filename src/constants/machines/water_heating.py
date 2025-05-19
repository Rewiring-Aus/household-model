from openapi_client.models import WaterHeatingEnum
from constants.fuel_stats import FuelTypeEnum
from constants.machines.machine_info import MachineInfoMap
from openapi_client.models.location_enum import LocationEnum

# kwh_per_day are from values in 'Location data'!A34:J63

WATER_HEATING_INFO: MachineInfoMap = {
    WaterHeatingEnum.GAS: {
        "fuel_type": FuelTypeEnum.NATURAL_GAS,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 7.93,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 8.70,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 7.69,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 5.86,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 7.99,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 7.59,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 8.04,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 7.93,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 7.38,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
    WaterHeatingEnum.LPG: {
        "fuel_type": FuelTypeEnum.LPG,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 7.93,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 8.70,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 7.69,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 5.86,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 7.99,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 7.59,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 8.04,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 7.93,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 7.38,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
    WaterHeatingEnum.ELECTRIC_RESISTANCE: {
        "fuel_type": FuelTypeEnum.ELECTRICITY,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 6.75,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 7.41,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 6.54,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 4.99,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 6.80,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 6.46,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 6.84,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 6.75,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 6.28,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
    WaterHeatingEnum.ELECTRIC_HEAT_PUMP: {
        "fuel_type": FuelTypeEnum.ELECTRICITY,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 1.83,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 2.05,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 1.76,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 1.27,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 2.00,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 1.90,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 1.84,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 1.81,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 1.64,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
    WaterHeatingEnum.SOLAR: {
        # This is not solar panels but pure solar, rooftop direct heating of water with sun heat e.g. Solahart
        # uses heat pump numbers for now 
        "fuel_type": FuelTypeEnum.SOLAR,
        "per_location": {
            LocationEnum.OTHER_TERRITORIES: {
                "kwh_per_day": 1.83,
            },
            LocationEnum.VICTORIA: {
                "kwh_per_day": 2.05,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 1.76,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 1.27,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 2.00,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 1.90,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 1.84,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 1.81,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 1.64,
            },
            LocationEnum.OVERSEAS: {
                "kwh_per_day": 0,
            },
        },
    },
}

# From 'Product prices'!B15:F20
WATER_HEATING_UPFRONT_COST = {
    WaterHeatingEnum.ELECTRIC_RESISTANCE: {
        "item_price": 1400,  # assuming med/large
        "install_cost": 700,  
    },
    WaterHeatingEnum.GAS: {
        "item_price": 1600,  # assuming storage
        "install_cost": 600,  
    },
    WaterHeatingEnum.LPG: {
        "item_price": 1600,  # assuming storage
        "install_cost": 600,  
    },
    WaterHeatingEnum.ELECTRIC_HEAT_PUMP: {
        "item_price": 3000,  
        "install_cost": 0,  # Note: Because of subsidies $700 install cost is not added to total, the total already includes install as shown in the sources provided. Subsidies for heat pumps lower the install cost.
    },
    WaterHeatingEnum.SOLAR: {
        # Not sure on price but also low priority because we don't recommend switching to rooftop direct-solar water heating (like Solahart)
        "item_price": None,
        "install_cost": None,
    },
}
