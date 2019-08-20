# coding: utf-8




from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from zuora_client.api_client import ApiClient


class CustomExchangeRatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_custom_exchange_rates(self, currency, start_date, end_date, **kwargs):  # noqa: E501
        """Get custom foreign currency exchange rates  # noqa: E501

        This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   This reference describes how to query custom foreign exchange rates from Zuora. You can use this API method to query exchange rates only if you use a custom exchange rate provider and upload rates with the Import Foreign Exchange Rates mass action.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_exchange_rates(currency, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The target base currency of the tenant. The exchange rates in the response are calculated in relation to the target currency.  The value must be a three-letter currency code, for example, USD.   (required)
        :param str start_date: Start date of the date range for which you want to get exchange rates.  The date must be in yyyy-mm-dd format, for example, 2016-01-15. The start date cannot be later than the end date.  (required)
        :param str end_date: End date of the date range for which you want to get exchange rates.  The date must be in yyyy-mm-dd format, for example, 2016-01-16. The end date can be a maximum of 90 days after the start date.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: GETCustomExchangeRatesType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_custom_exchange_rates_with_http_info(currency, start_date, end_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_custom_exchange_rates_with_http_info(currency, start_date, end_date, **kwargs)  # noqa: E501
            return data

    def get_custom_exchange_rates_with_http_info(self, currency, start_date, end_date, **kwargs):  # noqa: E501
        """Get custom foreign currency exchange rates  # noqa: E501

        This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   This reference describes how to query custom foreign exchange rates from Zuora. You can use this API method to query exchange rates only if you use a custom exchange rate provider and upload rates with the Import Foreign Exchange Rates mass action.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_custom_exchange_rates_with_http_info(currency, start_date, end_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: The target base currency of the tenant. The exchange rates in the response are calculated in relation to the target currency.  The value must be a three-letter currency code, for example, USD.   (required)
        :param str start_date: Start date of the date range for which you want to get exchange rates.  The date must be in yyyy-mm-dd format, for example, 2016-01-15. The start date cannot be later than the end date.  (required)
        :param str end_date: End date of the date range for which you want to get exchange rates.  The date must be in yyyy-mm-dd format, for example, 2016-01-16. The end date can be a maximum of 90 days after the start date.  (required)
        :param str zuora_entity_ids: An entity ID. If you have [Zuora Multi-entity](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/Multi-entity) enabled and the OAuth token is valid for more than one entity, you must use this header to specify which entity to perform the operation in. If the OAuth token is only valid for a single entity, or you do not have Zuora Multi-entity enabled, you do not need to set this header.
        :return: GETCustomExchangeRatesType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency', 'start_date', 'end_date', 'zuora_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_custom_exchange_rates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `get_custom_exchange_rates`")  # noqa: E501
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params or
                params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_custom_exchange_rates`")  # noqa: E501
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params or
                params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_custom_exchange_rates`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'currency' in params:
            path_params['currency'] = params['currency']  # noqa: E501

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501

        header_params = {}
        if 'zuora_entity_ids' in params:
            header_params['Zuora-Entity-Ids'] = params['zuora_entity_ids']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=utf-8'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/custom-exchange-rates/{currency}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GETCustomExchangeRatesType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)