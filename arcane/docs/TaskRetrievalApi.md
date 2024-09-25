# arcane.TaskRetrievalApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_list**](TaskRetrievalApi.md#tasks_list) | **GET** /api/tasks/ | 
[**tasks_retrieve**](TaskRetrievalApi.md#tasks_retrieve) | **GET** /api/tasks/{id}/ | 


# **tasks_list**
> List[Task] tasks_list()



List the last 10 tasks created by you.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import arcane
from arcane.models.task import Task
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
    api_instance = arcane.TaskRetrievalApi(api_client)

    try:
        api_response = api_instance.tasks_list()
        print("The response of TaskRetrievalApi->tasks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskRetrievalApi->tasks_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Task]**](Task.md)

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

# **tasks_retrieve**
> Task tasks_retrieve(id)



Retrieve a task by ID.

### Example

* Api Key Authentication (apiKeyAuth):

```python
import arcane
from arcane.models.task import Task
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
    api_instance = arcane.TaskRetrievalApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.tasks_retrieve(id)
        print("The response of TaskRetrievalApi->tasks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskRetrievalApi->tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | The specified task does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

