# arcane.RepositoryInstallationApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**repositories_installation_status_retrieve**](RepositoryInstallationApi.md#repositories_installation_status_retrieve) | **GET** /api/repositories/{repo_owner}/{repo_name}/installation-status | 


# **repositories_installation_status_retrieve**
> InstallationStatus repositories_installation_status_retrieve(repo_name, repo_owner)



Check if the Arcane Engine is installed for a specified GitHub repository.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import arcane
from arcane.models.installation_status import InstallationStatus
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
    api_instance = arcane.RepositoryInstallationApi(api_client)
    repo_name = 'repo_name_example' # str | 
    repo_owner = 'repo_owner_example' # str | 

    try:
        api_response = api_instance.repositories_installation_status_retrieve(repo_name, repo_owner)
        print("The response of RepositoryInstallationApi->repositories_installation_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryInstallationApi->repositories_installation_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_name** | **str**|  | 
 **repo_owner** | **str**|  | 

### Return type

[**InstallationStatus**](InstallationStatus.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

