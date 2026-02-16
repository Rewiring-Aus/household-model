# OpexWeeklyFixedCostsByFuelType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gas** | **float** |  | [optional] 
**lpg** | **float** |  | [optional] 
**electricity** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.opex_weekly_fixed_costs_by_fuel_type import OpexWeeklyFixedCostsByFuelType

# TODO update the JSON string below
json = "{}"
# create an instance of OpexWeeklyFixedCostsByFuelType from a JSON string
opex_weekly_fixed_costs_by_fuel_type_instance = OpexWeeklyFixedCostsByFuelType.from_json(json)
# print the JSON string representation of the object
print OpexWeeklyFixedCostsByFuelType.to_json()

# convert the object into a dict
opex_weekly_fixed_costs_by_fuel_type_dict = opex_weekly_fixed_costs_by_fuel_type_instance.to_dict()
# create an instance of OpexWeeklyFixedCostsByFuelType from a dict
opex_weekly_fixed_costs_by_fuel_type_from_dict = OpexWeeklyFixedCostsByFuelType.from_dict(opex_weekly_fixed_costs_by_fuel_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


