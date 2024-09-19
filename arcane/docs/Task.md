# Task


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**title** | **str** |  | 
**user_request** | **str** |  | [optional] 
**github_project** | **str** |  | 
**github_user** | **str** |  | 
**status** | **str** |  | 
**created** | **datetime** |  | [readonly] 
**result** | **str** |  | [optional] 
**issue_number** | **int** |  | [optional] 
**pr_number** | **int** |  | [optional] 
**gpt_model** | **str** |  | [optional] 
**branch** | **str** |  | 

## Example

```python
from arcane.models.task import Task

# TODO update the JSON string below
json = "{}"
# create an instance of Task from a JSON string
task_instance = Task.from_json(json)
# print the JSON string representation of the object
print(Task.to_json())

# convert the object into a dict
task_dict = task_instance.to_dict()
# create an instance of Task from a dict
task_from_dict = Task.from_dict(task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


