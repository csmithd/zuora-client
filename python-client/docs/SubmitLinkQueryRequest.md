# SubmitLinkQueryRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression** | **str** | Specifies whether Zuora compresses the query results.  | 
**encryption_key** | **str** | Base-64 encoded public key of an RSA key-pair.  If you set this field, Zuora encrypts the query results using the provided public key. You must use the corresponding private key to decrypt the query results.  | [optional] 
**output** | [**SubmitLinkQueryRequestOutput**](SubmitLinkQueryRequestOutput.md) |  | 
**output_format** | **str** | Specifies the format of the query results.  * &#x60;JSON&#x60; - Each row in the query results will be a JSON object. The query results will not be wrapped in a JSON array. * &#x60;CSV&#x60; - Each row in the query results will be a comma-separated list of values.  | 
**query** | **str** | The query to perform. See [SQL Queries in Zuora Link](https://knowledgecenter.zuora.com/DC_Developers/BA_Zuora_Link/BA_SQL_Queries_in_Zuora_Link) for more information.  In addition to SQL queries, Zuora Link supports [Export ZOQL](https://knowledgecenter.zuora.com/DC_Developers/BB_Export_ZOQL) queries. To perform an Export ZOQL query, set the &#x60;queryType&#x60; field to &#x60;ZOQL&#x60;.  | 
**query_type** | **str** | Specifies the format of the query.  * &#x60;SQL&#x60; - The query is a SQL query. See [SQL Queries in Zuora Link](https://knowledgecenter.zuora.com/DC_Developers/BA_Zuora_Link/BA_SQL_Queries_in_Zuora_Link) for more information. * &#x60;ZOQL&#x60; - The query is an Export ZOQL query. See [Export ZOQL](https://knowledgecenter.zuora.com/DC_Developers/BB_Export_ZOQL) for more information.  | [optional] [default to 'SQL']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


