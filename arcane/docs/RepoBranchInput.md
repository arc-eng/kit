# RepoBranchInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**github_repo** | **str** |  | 
**branch** | **str** |  | 

## Example

```python
from arcane.models.repo_branch_input import RepoBranchInput

# TODO update the JSON string below
json = "{}"
# create an instance of RepoBranchInput from a JSON string
repo_branch_input_instance = RepoBranchInput.from_json(json)
# print the JSON string representation of the object
print(RepoBranchInput.to_json())

# convert the object into a dict
repo_branch_input_dict = repo_branch_input_instance.to_dict()
# create an instance of RepoBranchInput from a dict
repo_branch_input_from_dict = RepoBranchInput.from_dict(repo_branch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


