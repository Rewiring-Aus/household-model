from aenum import Enum
from openapi_client.models.location_enum import LocationEnum


class FuelTypeEnum(str, Enum):
    ELECTRICITY = "electricity"
    NATURAL_GAS = "natural_gas"
    LPG = "lpg"
    WOOD = "wood"
    PETROL = "petrol"
    DIESEL = "diesel"
    SOLAR = "solar"  # this is direct solar, e.g. roof solar water heaters


# From 'Location data'!A187:J193
# Unit: kgCO2e/kWh
# Shared defaults for all fuel types except electricity
EMISSIONS_FACTORS = {
    FuelTypeEnum.NATURAL_GAS: 0.19,
    FuelTypeEnum.LPG: 0.22,
    FuelTypeEnum.WOOD: 0.40,
    FuelTypeEnum.PETROL: 0.24,
    FuelTypeEnum.DIESEL: 0.25,
    FuelTypeEnum.SOLAR: 0,
    FuelTypeEnum.ELECTRICITY: {
        LocationEnum.VICTORIA: 0.96,
        LocationEnum.NEW_SOUTH_WALES: 0.79,
        LocationEnum.NORTHERN_TERRITORY: 0.57,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.79,
        LocationEnum.TASMANIA: 0.16,
        LocationEnum.WESTERN_AUSTRALIA: 0.63,
        LocationEnum.SOUTH_AUSTRALIA: 0.35,
        LocationEnum.QUEENSLAND: 0.80,
    }
}

# From 'Grid'!A4:K14,
# 'Gas & LPG'!B9:K14, B47:K54,
# 'Wood'!A3:J13,
# 'Petrol & diesel'!B4:K13

# Unit: $/kWh
COST_PER_FUEL_KWH_TODAY = {
FuelTypeEnum.ELECTRICITY: {
        LocationEnum.VICTORIA: {
            "volume_rate": 0.27,
            "off_peak": 0.18,
        },
        LocationEnum.NEW_SOUTH_WALES: {
            "volume_rate": 0.34,
            "off_peak": 0.22,
        },
        LocationEnum.NORTHERN_TERRITORY: {
            "volume_rate": 0.28,
            "off_peak": 0.19,
        },
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: {
            "volume_rate": 0.26,
            "off_peak": 0.17,
        },  
        LocationEnum.TASMANIA: {
            "volume_rate": 0.30,
            "off_peak": 0.20,
        },
        LocationEnum.WESTERN_AUSTRALIA: {
            "volume_rate": 0.31,
            "off_peak": 0.21,
        },
        LocationEnum.SOUTH_AUSTRALIA: {
            "volume_rate": 0.44,
            "off_peak": 0.29,
        },
        LocationEnum.QUEENSLAND: {
            "volume_rate": 0.32,
            "off_peak": 0.21,
        },
    },
    FuelTypeEnum.NATURAL_GAS: {
        LocationEnum.VICTORIA: 0.133,
        LocationEnum.NEW_SOUTH_WALES: 0.153,
        LocationEnum.NORTHERN_TERRITORY: 0.146,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.159,
        LocationEnum.TASMANIA: 0.194,
        LocationEnum.WESTERN_AUSTRALIA: 0.115,
        LocationEnum.SOUTH_AUSTRALIA: 0.202,
        LocationEnum.QUEENSLAND: 0.209,
    },
    FuelTypeEnum.LPG: {
        LocationEnum.VICTORIA: 0.26,
        LocationEnum.NEW_SOUTH_WALES: 0.31,
        LocationEnum.NORTHERN_TERRITORY: 0.40,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.28,
        LocationEnum.TASMANIA: 0.24,
        LocationEnum.WESTERN_AUSTRALIA: 0.22,
        LocationEnum.SOUTH_AUSTRALIA: 0.30,
        LocationEnum.QUEENSLAND: 0.30,
    },
    FuelTypeEnum.WOOD: {
        LocationEnum.VICTORIA: 0.110,
        LocationEnum.NEW_SOUTH_WALES: 0.140,
        LocationEnum.NORTHERN_TERRITORY: 0.151,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.094,
        LocationEnum.TASMANIA: 0.067,
        LocationEnum.WESTERN_AUSTRALIA: 0.140,
        LocationEnum.SOUTH_AUSTRALIA: 0.111,
        LocationEnum.QUEENSLAND: 0.151,
    },
    FuelTypeEnum.PETROL: {
        LocationEnum.VICTORIA: 0.199,
        LocationEnum.NEW_SOUTH_WALES: 0.200,
        LocationEnum.NORTHERN_TERRITORY: 0.208,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.200,
        LocationEnum.TASMANIA: 0.199,
        LocationEnum.WESTERN_AUSTRALIA: 0.192,
        LocationEnum.SOUTH_AUSTRALIA: 0.193,
        LocationEnum.QUEENSLAND: 0.202,
    },
    FuelTypeEnum.DIESEL: {
        LocationEnum.VICTORIA: 0.18,
        LocationEnum.NEW_SOUTH_WALES: 0.18,
        LocationEnum.NORTHERN_TERRITORY: 0.20,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.18,
        LocationEnum.TASMANIA: 0.18,
        LocationEnum.WESTERN_AUSTRALIA: 0.17,
        LocationEnum.SOUTH_AUSTRALIA: 0.18,
        LocationEnum.QUEENSLAND: 0.18,
    },
    FuelTypeEnum.SOLAR: {
        LocationEnum.VICTORIA: 0,
        LocationEnum.NEW_SOUTH_WALES: 0,
        LocationEnum.NORTHERN_TERRITORY: 0,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0,
        LocationEnum.TASMANIA: 0,
        LocationEnum.WESTERN_AUSTRALIA: 0,
        LocationEnum.SOUTH_AUSTRALIA: 0,
        LocationEnum.QUEENSLAND: 0,
    },
}

FIXED_COSTS_PER_YEAR_2024 = {
    FuelTypeEnum.ELECTRICITY: {
        LocationEnum.VICTORIA: 396,
        LocationEnum.NEW_SOUTH_WALES: 465,
        LocationEnum.NORTHERN_TERRITORY: 210,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 441,
        LocationEnum.TASMANIA: 435,
        LocationEnum.WESTERN_AUSTRALIA: 414,
        LocationEnum.SOUTH_AUSTRALIA: 415,
        LocationEnum.QUEENSLAND: 450,
    },
    FuelTypeEnum.NATURAL_GAS: {
        LocationEnum.VICTORIA: 296,
        LocationEnum.NEW_SOUTH_WALES: 244,
        LocationEnum.NORTHERN_TERRITORY: 247,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 260,
        LocationEnum.TASMANIA: 235,
        LocationEnum.WESTERN_AUSTRALIA: 80,
        LocationEnum.SOUTH_AUSTRALIA: 297,
        LocationEnum.QUEENSLAND: 247,
    },
    FuelTypeEnum.LPG: {
        LocationEnum.VICTORIA: 96.0,
        LocationEnum.NEW_SOUTH_WALES: 96.0,
        LocationEnum.NORTHERN_TERRITORY: 105.0,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 96.0,
        LocationEnum.TASMANIA: 96.0,
        LocationEnum.WESTERN_AUSTRALIA: 90.0,
        LocationEnum.SOUTH_AUSTRALIA: 99.0,
        LocationEnum.QUEENSLAND: 95.0,
    },
}

# Average over next 15 years 
# Unit: $/kWh
COST_PER_FUEL_KWH_AVG_15_YEARS = {
    FuelTypeEnum.ELECTRICITY: {
        LocationEnum.VICTORIA: 0.31,
        LocationEnum.NEW_SOUTH_WALES: 0.41,
        LocationEnum.NORTHERN_TERRITORY: 0.28,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.30,
        LocationEnum.TASMANIA: 0.36,
        LocationEnum.WESTERN_AUSTRALIA: 0.38,
        LocationEnum.SOUTH_AUSTRALIA: 0.54,
        LocationEnum.QUEENSLAND: 0.55,
    },
    FuelTypeEnum.NATURAL_GAS: {
        LocationEnum.VICTORIA: 0.22,
        LocationEnum.NEW_SOUTH_WALES: 0.19,
        LocationEnum.NORTHERN_TERRITORY: 0.19,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.21,
        LocationEnum.TASMANIA: 0.26,
        LocationEnum.WESTERN_AUSTRALIA: 0.18,
        LocationEnum.SOUTH_AUSTRALIA: 0.25,
        LocationEnum.QUEENSLAND: 0.247,
    },
    FuelTypeEnum.LPG: {
        LocationEnum.VICTORIA: 0.35,
        LocationEnum.NEW_SOUTH_WALES: 0.38,
        LocationEnum.NORTHERN_TERRITORY: 0.41,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.36,
        LocationEnum.TASMANIA: 0.27,
        LocationEnum.WESTERN_AUSTRALIA: 0.26,
        LocationEnum.SOUTH_AUSTRALIA: 0.38,
        LocationEnum.QUEENSLAND: 0.35,
    },
    FuelTypeEnum.WOOD: {
        LocationEnum.VICTORIA: 0.15,
        LocationEnum.NEW_SOUTH_WALES: 0.17,
        LocationEnum.NORTHERN_TERRITORY: 0.16,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.12,
        LocationEnum.TASMANIA: 0.08,
        LocationEnum.WESTERN_AUSTRALIA: 0.17,
        LocationEnum.SOUTH_AUSTRALIA: 0.14,
        LocationEnum.QUEENSLAND: 0.18,
    },
    FuelTypeEnum.PETROL: {
        LocationEnum.VICTORIA: 0.22,
        LocationEnum.NEW_SOUTH_WALES: 0.22,
        LocationEnum.NORTHERN_TERRITORY: 0.21,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.22,
        LocationEnum.TASMANIA: 0.21,
        LocationEnum.WESTERN_AUSTRALIA: 0.21,
        LocationEnum.SOUTH_AUSTRALIA: 0.21,
        LocationEnum.QUEENSLAND: 0.23,
    },
    FuelTypeEnum.DIESEL: {
        LocationEnum.VICTORIA: 0.20,
        LocationEnum.NEW_SOUTH_WALES: 0.20,
        LocationEnum.NORTHERN_TERRITORY: 0.20,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0.19,
        LocationEnum.TASMANIA: 0.19,
        LocationEnum.WESTERN_AUSTRALIA: 0.19,
        LocationEnum.SOUTH_AUSTRALIA: 0.19,
        LocationEnum.QUEENSLAND: 0.20,
    },
    FuelTypeEnum.SOLAR: {
        LocationEnum.VICTORIA: 0,
        LocationEnum.NEW_SOUTH_WALES: 0,
        LocationEnum.NORTHERN_TERRITORY: 0,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 0,
        LocationEnum.TASMANIA: 0,
        LocationEnum.WESTERN_AUSTRALIA: 0,
        LocationEnum.SOUTH_AUSTRALIA: 0,
        LocationEnum.QUEENSLAND: 0,
    },
}

FIXED_COSTS_PER_YEAR_AVG_15_YEARS = {
    FuelTypeEnum.ELECTRICITY: { 
        LocationEnum.VICTORIA: 446.05,
        LocationEnum.NEW_SOUTH_WALES: 562.08,
        LocationEnum.NORTHERN_TERRITORY: 205.94,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 511.12,
        LocationEnum.TASMANIA: 517.42,
        LocationEnum.WESTERN_AUSTRALIA: 509.48,
        LocationEnum.SOUTH_AUSTRALIA: 507.18,
        LocationEnum.QUEENSLAND: 777.94,
    },
    FuelTypeEnum.NATURAL_GAS: {
        LocationEnum.VICTORIA: 265.21,
        LocationEnum.NEW_SOUTH_WALES: 300.40,
        LocationEnum.NORTHERN_TERRITORY: 314.22,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 337.02,
        LocationEnum.TASMANIA: 375.07,
        LocationEnum.WESTERN_AUSTRALIA: 398.60,
        LocationEnum.SOUTH_AUSTRALIA: 291.28,
        LocationEnum.QUEENSLAND: 291.28,
    },
    FuelTypeEnum.LPG: {
        LocationEnum.VICTORIA: 129.28,
        LocationEnum.NEW_SOUTH_WALES: 118.16,
        LocationEnum.NORTHERN_TERRITORY: 108.22,
        LocationEnum.AUSTRALIAN_CAPITAL_TERRITORY: 124.58,
        LocationEnum.TASMANIA: 108.12,
        LocationEnum.WESTERN_AUSTRALIA: 108.54,
        LocationEnum.SOUTH_AUSTRALIA: 125.03,
        LocationEnum.QUEENSLAND: 112.17,
    },
}
