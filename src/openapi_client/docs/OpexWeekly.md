# OpexWeekly


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grid_volume_costs** | **float** |  | [optional] 
**other_energy_costs** | **float** |  | [optional] 
**other_energy_costs_by_fuel_type** | [**OpexWeeklyOtherEnergyCostsByFuelType**](OpexWeeklyOtherEnergyCostsByFuelType.md) |  | [optional] 
**fixed_costs** | **float** |  | [optional] 
**fixed_costs_by_fuel_type** | [**OpexWeeklyFixedCostsByFuelType**](OpexWeeklyFixedCostsByFuelType.md) |  | [optional] 
**revenue_from_solar_export** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.opex_weekly import OpexWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of OpexWeekly from a JSON string
opex_weekly_instance = OpexWeekly.from_json(json)
# print the JSON string representation of the object
print OpexWeekly.to_json()

# convert the object into a dict
opex_weekly_dict = opex_weekly_instance.to_dict()
# create an instance of OpexWeekly from a dict
opex_weekly_from_dict = OpexWeekly.from_dict(opex_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


