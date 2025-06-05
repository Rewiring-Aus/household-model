from constants.utils import PeriodEnum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.electrify_household import electrify_household
from openapi_client.models import (
    Household,
    OpexWeekly,
    Savings,
)
from savings.emissions.calculate_emissions import calculate_emissions
from savings.energy.get_electricity_consumption import get_electricity_consumption
from savings.energy.get_machine_energy import get_total_energy_needs
from savings.energy.get_other_energy_consumption import get_other_energy_consumption
from savings.opex.calculate_opex import calculate_opex, get_grid_volume_cost, get_solar_feedin_tariff
from savings.opex.get_fixed_costs import get_fixed_costs, get_fixed_costs_by_fuel_type
from savings.opex.get_other_energy_costs import get_other_energy_costs, get_other_energy_costs_by_fuel_type
from savings.upfront_cost.calculate_upfront_cost import calculate_upfront_cost
from models.recommend_next_action import recommend_next_action
from utils.clean_household import clean_household
from utils.validate_household import validate_household
import json

app = FastAPI()

origins = [
    "*"
    # TODO: Lock this down to just the deployed frontend app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/savings")
def calculate_household_savings(current_household: Household) -> Savings:

    validate_household(current_household)
    current_household = clean_household(current_household)
    electrified_household = electrify_household(current_household)

    emissions = calculate_emissions(current_household, electrified_household)
    opex = calculate_opex(current_household, electrified_household)
    upfront_cost = calculate_upfront_cost(current_household, electrified_household)
    recommendation = recommend_next_action(current_household)

    opex_before = calculate_raw_opex(current_household)
    opex_after = calculate_raw_opex(electrified_household)

    savings = Savings(
        emissions=emissions,
        opex=opex,
        upfrontCost=upfront_cost,
        recommendation=recommendation,

        opexBefore=opex_before,
        opexAfter=opex_after
    )
    return savings


def calculate_raw_opex(household: Household) -> OpexWeekly:
    energy_needs = get_total_energy_needs(household, PeriodEnum.YEARLY, household.location)
    electricity_consumption = get_electricity_consumption(
        energy_needs, household.solar, household.battery, household.location, PeriodEnum.YEARLY
    )
    other_energy_consumption = get_other_energy_consumption(energy_needs)


    grid_volume_costs = get_grid_volume_cost(
        electricity_consumption["consumed_from_grid"],
        electricity_consumption["consumed_from_battery"],
        PeriodEnum.YEARLY,
        household.location,
    )

    other_energy_costs = get_other_energy_costs(
        other_energy_consumption, PeriodEnum.YEARLY, household.location
    )
    other_energy_costs_by_fuel_type = get_other_energy_costs_by_fuel_type(
        other_energy_consumption, PeriodEnum.YEARLY, household.location
    )

    print(f"other_energy_costs_by_fuel_type: {json.dumps(other_energy_costs_by_fuel_type, indent=4)}")

    fixed_costs = get_fixed_costs(household, PeriodEnum.YEARLY)
    fixed_costs_by_fuel_type = get_fixed_costs_by_fuel_type(household, PeriodEnum.YEARLY)

    print(f"fixed_costs_by_fuel_type: {json.dumps(fixed_costs_by_fuel_type, indent=4)}")

    revenue_from_solar_export = get_solar_feedin_tariff(
        electricity_consumption["exported_to_grid"], PeriodEnum.YEARLY, household.location
    )

    return OpexWeekly(
        gridVolumeCosts=grid_volume_costs,
        otherEnergyCosts=other_energy_costs,
        otherEnergyCostsByFuelType=other_energy_costs_by_fuel_type,
        fixedCosts=fixed_costs,
        fixedCostsByFuelType=fixed_costs_by_fuel_type,
        revenueFromSolarExport=revenue_from_solar_export
    )
