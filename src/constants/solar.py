from openapi_client.models.location_enum import LocationEnum

# % of solar that is self-consumed
MACHINE_CATEGORY_TO_SELF_CONSUMPTION_RATE = {
    "appliances": 0.5,
    "vehicles": 0.5,
    "other_appliances": 0.5,
}

# $/kWh

# 'Location data'!B120
SOLAR_FEEDIN_TARIFF_2024 = 0.06

# 'Forward pricing'!B121
SOLAR_FEEDIN_TARIFF_AVG_15_YEARS = {
    LocationEnum.OTHER_TERRITORIES: 0.08,
    LocationEnum.VICTORIA: 0.06,
    LocationEnum.NEW_SOUTH_WALES: 0.10,
    LocationEnum.NORTHERN_TERRITORY: 0.10,
    LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.12,
    LocationEnum.TASMANIA: 0.11,
    LocationEnum.WESTERN_AUSTRALIA: 0.04,
    LocationEnum.SOUTH_AUSTRALIA: 0.09,
    LocationEnum.QUEENSLAND: 0.12,
    LocationEnum.OVERSEAS: 0,
}

# % of max capacity that it generates on average over 30 years, taking into account degradation
SOLAR_AVG_DEGRADED_PERFORMANCE_30_YRS = 0.9308

# Solar capacity factor
SOLAR_CAPACITY_FACTOR = {
    LocationEnum.OTHER_TERRITORIES: 0.1715,
    LocationEnum.VICTORIA: 0.1537,
    LocationEnum.NEW_SOUTH_WALES: 0.1629,
    LocationEnum.NORTHERN_TERRITORY: 0.1898,
    LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.1632,
    LocationEnum.TASMANIA: 0.1586,
    LocationEnum.WESTERN_AUSTRALIA: 0.2104,
    LocationEnum.SOUTH_AUSTRALIA: 0.1788,
    LocationEnum.QUEENSLAND: 0.1868,
    LocationEnum.OVERSEAS: 0,
}
