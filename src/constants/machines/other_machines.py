# Other machines (space cooling, refrigeration, laundry, lighting, etc.)

from openapi_client.models.location_enum import LocationEnum

# From 'Machines'!B43:L43
ENERGY_NEEDS_SPACE_COOLING = {
    LocationEnum.VICTORIA: {
        "kwh_per_day": 0.10,
    },
    LocationEnum.NEW_SOUTH_WALES: {
        "kwh_per_day": 0.77,
    },
    LocationEnum.NORTHERN_TERRITORY: {
        "kwh_per_day": 7.58,
    },
    LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
        "kwh_per_day": 0.74,
    },
    LocationEnum.TASMANIA: {
        "kwh_per_day": 0.09,
    },
    LocationEnum.WESTERN_AUSTRALIA: {
        "kwh_per_day": 1.65,
    },
    LocationEnum.SOUTH_AUSTRALIA: {
        "kwh_per_day": 0.63,
    },
    LocationEnum.QUEENSLAND: {
        "kwh_per_day": 1.89,
    },
}

# From 'Machines'!B349:L357
# washer dryer + lighting + other appliances
ENERGY_NEEDS_OTHER_APPLIANCES = {
    LocationEnum.VICTORIA: {
        "kwh_per_day": 5.21,
    },
    LocationEnum.NEW_SOUTH_WALES: {
        "kwh_per_day": 5.32,
    },
    LocationEnum.NORTHERN_TERRITORY: {
        "kwh_per_day": 5.52,
    },
    LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
        "kwh_per_day": 5.18,
    },
    LocationEnum.TASMANIA: {
        "kwh_per_day": 5.21,
    },
    LocationEnum.WESTERN_AUSTRALIA: {
        "kwh_per_day": 5.14,
    },
    LocationEnum.SOUTH_AUSTRALIA: {
        "kwh_per_day": 5.21,
    },
    LocationEnum.QUEENSLAND: {
        "kwh_per_day": 5.09,
    },
}

# From 'Machines'!B349:L357 and 'Machines'!B232:L237
# refrigeration + dishwasher + oven + microwave + uprights
ENERGY_NEEDS_OTHER_COOKING = {
    LocationEnum.VICTORIA: {
        "kwh_per_day": 3.32,
    },
    LocationEnum.NEW_SOUTH_WALES: {
        "kwh_per_day": 3.40,
    },
    LocationEnum.NORTHERN_TERRITORY: {
        "kwh_per_day": 3.57,
    },
    LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
        "kwh_per_day": 3.20,
    },
    LocationEnum.TASMANIA: {
        "kwh_per_day": 3.65,
    },
    LocationEnum.WESTERN_AUSTRALIA: {
        "kwh_per_day": 3.47,
    },
    LocationEnum.SOUTH_AUSTRALIA: {
        "kwh_per_day": 3.62,
    },
    LocationEnum.QUEENSLAND: {
        "kwh_per_day": 3.35,
    },
}

# From 'Machines'!B356:L357 
# pool equipment electric + pool equipment natural gas
ENERGY_NEEDS_POOL_EQUIPMENT = {
    LocationEnum.VICTORIA: {
        "kwh_per_day": 0.48,
    },
    LocationEnum.NEW_SOUTH_WALES: {
        "kwh_per_day": 1.01,
    },
    LocationEnum.NORTHERN_TERRITORY: {
        "kwh_per_day": 2.0,
    },
    LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
        "kwh_per_day": 0.33,
    },
    LocationEnum.TASMANIA: {
        "kwh_per_day": 0.34,
    },
    LocationEnum.WESTERN_AUSTRALIA: {
        "kwh_per_day": 1.20,
    },
    LocationEnum.SOUTH_AUSTRALIA: {
        "kwh_per_day": 0.67,
    },
    LocationEnum.QUEENSLAND: {
        "kwh_per_day": 1.37,
    },
}



ENERGY_NEEDS_OTHER_MACHINES_PER_DAY = {}

for location in LocationEnum:
    total_kwh = (
        ENERGY_NEEDS_SPACE_COOLING.get(location, {}).get("kwh_per_day", 0) +
        ENERGY_NEEDS_OTHER_APPLIANCES.get(location, {}).get("kwh_per_day", 0) +
        ENERGY_NEEDS_OTHER_COOKING.get(location, {}).get("kwh_per_day", 0) +
        ENERGY_NEEDS_POOL_EQUIPMENT.get(location, {}).get("kwh_per_day", 0)
    )

    ENERGY_NEEDS_OTHER_MACHINES_PER_DAY[location] = {
        "kwh_per_day": total_kwh
    }
