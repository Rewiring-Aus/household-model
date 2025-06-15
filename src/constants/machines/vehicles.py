from constants.fuel_stats import FuelTypeEnum
from constants.machines.machine_info import MachineInfoMap
from openapi_client.models.location_enum import LocationEnum
from openapi_client.models.vehicle_fuel_type_enum import VehicleFuelTypeEnum


# Vehicles kWh/day per vehicle from 'Location data'!B83:L102
VEHICLE_INFO: MachineInfoMap = {
    VehicleFuelTypeEnum.PETROL: {
        "fuel_type": FuelTypeEnum.PETROL,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 35.9,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 36.7,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 38.6,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 33.5,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 33.6,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 35.8,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 33.2,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 37.2,
            },
        },
    },
    VehicleFuelTypeEnum.DIESEL: {
        "fuel_type": FuelTypeEnum.DIESEL,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 28,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 29,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 30,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 26,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 26,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 28,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 26,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 29,
            },
        },
    },
    VehicleFuelTypeEnum.HYBRID: [
        # Assume 70% petrol, 30% electric
        {
            "fuel_type": FuelTypeEnum.PETROL,
            "per_location": {
                LocationEnum.VICTORIA: {
                    "kwh_per_day": 35.9 * 0.7,
                },
                LocationEnum.NEW_SOUTH_WALES: {
                    "kwh_per_day": 36.7 * 0.7,
                },
                LocationEnum.NORTHERN_TERRITORY: {
                    "kwh_per_day": 38.6 * 0.7,
                },
                LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                    "kwh_per_day": 33.5 * 0.7,
                },
                LocationEnum.TASMANIA: {
                    "kwh_per_day": 33.6 * 0.7,
                },
                LocationEnum.WESTERN_AUSTRALIA: {
                    "kwh_per_day": 35.8 * 0.7,
                },
                LocationEnum.SOUTH_AUSTRALIA: {
                    "kwh_per_day": 33.2 * 0.7,
                },
                LocationEnum.QUEENSLAND: {
                    "kwh_per_day": 37.2 * 0.7,
                },
            },
        },
        {
            "fuel_type": FuelTypeEnum.ELECTRICITY,
            "per_location": {
                LocationEnum.VICTORIA: {
                    "kwh_per_day": 9.2 * 0.3,
                },
                LocationEnum.NEW_SOUTH_WALES: {
                    "kwh_per_day": 9.4 * 0.3,
                },
                LocationEnum.NORTHERN_TERRITORY: {
                    "kwh_per_day": 9.9 * 0.3,
                },
                LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                    "kwh_per_day": 8.6 * 0.3,
                },
                LocationEnum.TASMANIA: {
                    "kwh_per_day": 8.6 * 0.3,
                },
                LocationEnum.WESTERN_AUSTRALIA: {
                    "kwh_per_day": 9.2 * 0.3,
                },
                LocationEnum.SOUTH_AUSTRALIA: {
                    "kwh_per_day": 8.5 * 0.3,
                },
                LocationEnum.QUEENSLAND: {
                    "kwh_per_day": 9.6 * 0.3,
                },
            },
        },
    ],
    VehicleFuelTypeEnum.PLUG_IN_HYBRID: [
        # Assume 60% petrol, 40% electric
        {
            "fuel_type": FuelTypeEnum.PETROL,
            "per_location": {
                LocationEnum.VICTORIA: {
                    "kwh_per_day": 35.9 * 0.6,
                },
                LocationEnum.NEW_SOUTH_WALES: {
                    "kwh_per_day": 36.7 * 0.6,
                },
                LocationEnum.NORTHERN_TERRITORY: {
                    "kwh_per_day": 38.6 * 0.6,
                },
                LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                    "kwh_per_day": 33.5 * 0.6,
                },
                LocationEnum.TASMANIA: {
                    "kwh_per_day": 33.6 * 0.6,
                },
                LocationEnum.WESTERN_AUSTRALIA: {
                    "kwh_per_day": 35.8 * 0.6,
                },
                LocationEnum.SOUTH_AUSTRALIA: {
                    "kwh_per_day": 33.2 * 0.6,
                },
                LocationEnum.QUEENSLAND: {
                    "kwh_per_day": 37.2 * 0.6,
                },
            },
        },
        {
            "fuel_type": FuelTypeEnum.ELECTRICITY,
            "per_location": {
                LocationEnum.VICTORIA: {
                    "kwh_per_day": 9.2 * 0.4,
                },
                LocationEnum.NEW_SOUTH_WALES: {
                    "kwh_per_day": 9.4 * 0.4,
                },
                LocationEnum.NORTHERN_TERRITORY: {
                    "kwh_per_day": 9.9 * 0.4,
                },
                LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                    "kwh_per_day": 8.6 * 0.4,
                },
                LocationEnum.TASMANIA: {
                    "kwh_per_day": 8.6 * 0.4,
                },
                LocationEnum.WESTERN_AUSTRALIA: {
                    "kwh_per_day": 9.2 * 0.4,
                },
                LocationEnum.SOUTH_AUSTRALIA: {
                    "kwh_per_day": 8.5 * 0.4,
                },
                LocationEnum.QUEENSLAND: {
                    "kwh_per_day": 9.6 * 0.4,
                },  
            },
        },
    ],
    VehicleFuelTypeEnum.ELECTRIC: {
        "fuel_type": FuelTypeEnum.ELECTRICITY,
        "per_location": {
            LocationEnum.VICTORIA: {
                "kwh_per_day": 9.2,
            },
            LocationEnum.NEW_SOUTH_WALES: {
                "kwh_per_day": 9.4,
            },
            LocationEnum.NORTHERN_TERRITORY: {
                "kwh_per_day": 9.9,
            },
            LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
                "kwh_per_day": 8.6,
            },
            LocationEnum.TASMANIA: {
                "kwh_per_day": 8.6,
            },
            LocationEnum.WESTERN_AUSTRALIA: {
                "kwh_per_day": 9.2,
            },
            LocationEnum.SOUTH_AUSTRALIA: {
                "kwh_per_day": 8.5,
            },
            LocationEnum.QUEENSLAND: {
                "kwh_per_day": 9.6,
            },
        },
    },
}

# From 'Machines'!B390:L390 * 7
VEHICLE_AVG_KMS_PER_WEEK = {
    LocationEnum.VICTORIA: 38.0 * 7,
    LocationEnum.NEW_SOUTH_WALES: 36.2 * 7,
    LocationEnum.NORTHERN_TERRITORY: 35.9 * 7,
    LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 35.1 * 7,
    LocationEnum.TASMANIA: 33.1 * 7,
    LocationEnum.WESTERN_AUSTRALIA: 33.8 * 7,
    LocationEnum.SOUTH_AUSTRALIA: 35.0 * 7,
    LocationEnum.QUEENSLAND: 36.9 * 7,
}