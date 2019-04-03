# PostBillingPreviewRunParam

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assume_renewal** | **str** | Indicates whether to generate a preview of future invoice items and credit memo items with the assumption that the subscriptions are renewed.  Set one of the following values in this field to decide how the assumption is applied in the billing preview.    * **All:** The assumption is applied to all the subscriptions. Zuora generates preview invoice item data and credit memo item data from the first day of the customer&#39;s next billing period to the target date.      * **None:** (Default) The assumption is not applied to the subscriptions. Zuora generates preview invoice item data and credit memo item data based on the current term end date and the target date.        * If the target date is later than the current term end date, Zuora generates preview invoice item data and credit memo item data from the first day of the customer&#39;s next billing period to the current term end date.      * If the target date is earlier than the current term end date, Zuora generates preview invoice item data and credit memeo item data from the first day of the customer&#39;s next billing period to the target date.    * **Autorenew:** The assumption is applied to the subscriptions that have auto-renew enabled. Zuora generates preview invoice item data and credit memo item data from the first day of the customer&#39;s next billing period to the target date.    **Note:**    - This field can only be used if the subscription renewal term is not set to 0.           - The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).      | [optional] 
**batch** | **str** | The customer batch to include in the billing preview run. If not specified, all customer batches are included.  | [optional] 
**charge_type_to_exclude** | **str** | The charge types to exclude from the forecast run.  **Possible values:** OneTime, Recurring, Usage, and any comma-separated combination of these values.  | [optional] 
**including_evergreen_subscription** | **bool** | Indicates if evergreen subscriptions are included in the billing preview run. By default, evergreen subscriptions are not included.  | [optional] 
**target_date** | **date** | The target date for the billing preview run. The billing preview run generates preview invoice item data and credit memo item data from the first day of the customer&#39;s next billing period to the TargetDate.   If the TargetDate is later than the subscription current term end date, the preview invoice item data and credit memo item data is generated from the first day of the customer&#39;s next billing period to the current term end date. If you want to generate preview invoice item data and credit memo item data past the end of the subscription current term, specify the AssumeRenewal field in the request.  **Note:** The credit memo item data is only available if you have Invoice Settlement feature enabled. The Invoice Settlement feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

