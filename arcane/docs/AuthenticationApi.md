# arcane.AuthenticationApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exchange_github_token_create**](AuthenticationApi.md#exchange_github_token_create) | **POST** /api/exchange-github-token/ | 


# **exchange_github_token_create**
> Output exchange_github_token_create(input)



### Example

* Api Key Authentication (apiKeyAuth):

```python
import arcane
from arcane.models.input import Input
from arcane.models.output import Output
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
    api_instance = arcane.AuthenticationApi(api_client)
    input = arcane.Input() # Input | 

    try:
        api_response = api_instance.exchange_github_token_create(input)
        print("The response of AuthenticationApi->exchange_github_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->exchange_github_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | [**Input**](Input.md)|  | 

### Return type

[**Output**](Output.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
