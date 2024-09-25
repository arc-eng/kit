# arcane.PRRetrievalApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resolve_pr_create**](PRRetrievalApi.md#resolve_pr_create) | **POST** /api/resolve-pr/ | 


# **resolve_pr_create**
> PRNumberResponse resolve_pr_create(repo_branch_input)



Retrieve the PR number for a given repo and branch.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import arcane
from arcane.models.pr_number_response import PRNumberResponse
from arcane.models.repo_branch_input import RepoBranchInput
from arcane.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = arcane.Configuration(
    host = "http://localhost:8000"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyAuth
configuration.api_key['apiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with arcane.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = arcane.PRRetrievalApi(api_client)
    repo_branch_input = arcane.RepoBranchInput() # RepoBranchInput | 

    try:
        api_response = api_instance.resolve_pr_create(repo_branch_input)
        print("The response of PRRetrievalApi->resolve_pr_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PRRetrievalApi->resolve_pr_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_branch_input** | [**RepoBranchInput**](RepoBranchInput.md)|  | 

### Return type

[**PRNumberResponse**](PRNumberResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | No PR found for the specified branch. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

