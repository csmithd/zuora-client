# swagger_client.LinkQueriesApi

All URIs are relative to *https://rest.zuora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_link_query_job**](LinkQueriesApi.md#d_elete_link_query_job) | **DELETE** /query/jobs/{job-id} | Cancel Link query job
[**g_et_link_query_job**](LinkQueriesApi.md#g_et_link_query_job) | **GET** /query/jobs/{job-id} | Get Link query job
[**g_et_link_query_jobs**](LinkQueriesApi.md#g_et_link_query_jobs) | **GET** /query/jobs | Get Link query jobs
[**p_ost_link_query_job**](LinkQueriesApi.md#p_ost_link_query_job) | **POST** /query/jobs | Submit Link query


# **d_elete_link_query_job**
> DeleteLinkQueryJobResponse d_elete_link_query_job(authorization, job_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Cancel Link query job

Cancels a [Zuora Link](https://knowledgecenter.zuora.com/DC_Developers/BA_Zuora_Link) query job, which prevents Zuora from performing the query. This operation is only applicable if the status of the query job is `accepted` or `in_progress`. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkQueriesApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
job_id = 'job_id_example' # str | Internal identifier of the query job. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Cancel Link query job
    api_response = api_instance.d_elete_link_query_job(authorization, job_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkQueriesApi->d_elete_link_query_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **job_id** | [**str**](.md)| Internal identifier of the query job.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**DeleteLinkQueryJobResponse**](DeleteLinkQueryJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_link_query_job**
> GetLinkQueryJobResponse g_et_link_query_job(authorization, job_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Get Link query job

Retrieves a [Zuora Link](https://knowledgecenter.zuora.com/DC_Developers/BA_Zuora_Link) query job. You can use this operation to track the status of the query job and obtain the URL of the query results. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkQueriesApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
job_id = 'job_id_example' # str | Internal identifier of the query job. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Get Link query job
    api_response = api_instance.g_et_link_query_job(authorization, job_id, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkQueriesApi->g_et_link_query_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **job_id** | [**str**](.md)| Internal identifier of the query job.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**GetLinkQueryJobResponse**](GetLinkQueryJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_link_query_jobs**
> GetLinkQueryJobsResponse g_et_link_query_jobs(authorization, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, query_status=query_status, page_size=page_size)

Get Link query jobs

Returns a list of [Zuora Link](https://knowledgecenter.zuora.com/DC_Developers/BA_Zuora_Link) query jobs that have been created in your Zuora tenant. You can filter the list by status. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkQueriesApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)
query_status = 'query_status_example' # str | Filters the list of query jobs by status.  (optional)
page_size = 20 # int | Specifies the maximum number of query jobs to return.  (optional) (default to 20)

try:
    # Get Link query jobs
    api_response = api_instance.g_et_link_query_jobs(authorization, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id, query_status=query_status, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkQueriesApi->g_et_link_query_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 
 **query_status** | **str**| Filters the list of query jobs by status.  | [optional] 
 **page_size** | **int**| Specifies the maximum number of query jobs to return.  | [optional] [default to 20]

### Return type

[**GetLinkQueryJobsResponse**](GetLinkQueryJobsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_link_query_job**
> SubmitLinkQueryResponse p_ost_link_query_job(authorization, body, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)

Submit Link query

Submits a [Zuora Link](https://knowledgecenter.zuora.com/DC_Developers/BA_Zuora_Link) query to be performed by Zuora and creates a query job. You can use [Get Link query job](#operation/GET_LinkQueryJob) to track the status of the query job and obtain the URL of the query results. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkQueriesApi()
authorization = 'authorization_example' # str | `Bearer {token}` for a valid OAuth token. 
body = swagger_client.SubmitLinkQueryRequest() # SubmitLinkQueryRequest | 
zuora_entity_ids = 'zuora_entity_ids_example' # str | An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  (optional)
zuora_track_id = 'zuora_track_id_example' # str | A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (`:`), semicolon (`;`), double quote (`\"`), and quote (`'`).  (optional)

try:
    # Submit Link query
    api_response = api_instance.p_ost_link_query_job(authorization, body, zuora_entity_ids=zuora_entity_ids, zuora_track_id=zuora_track_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkQueriesApi->p_ost_link_query_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| &#x60;Bearer {token}&#x60; for a valid OAuth token.  | 
 **body** | [**SubmitLinkQueryRequest**](SubmitLinkQueryRequest.md)|  | 
 **zuora_entity_ids** | **str**| An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.  | [optional] 
 **zuora_track_id** | **str**| A custom identifier for tracing the API call. If you set a value for this header, Zuora returns the same value in the response headers. This header enables you to associate your system process identifiers with Zuora API calls, to assist with troubleshooting in the event of an issue.  The value of this field must use the US-ASCII character set and must not include any of the following characters: colon (&#x60;:&#x60;), semicolon (&#x60;;&#x60;), double quote (&#x60;\&quot;&#x60;), and quote (&#x60;&#39;&#x60;).  | [optional] 

### Return type

[**SubmitLinkQueryResponse**](SubmitLinkQueryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

