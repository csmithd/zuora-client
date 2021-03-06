# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_account_summary_invoice_type import GETAccountSummaryInvoiceType  # noqa: F401,E501
from zuora_client.models.get_account_summary_payment_type import GETAccountSummaryPaymentType  # noqa: F401,E501
from zuora_client.models.get_account_summary_subscription_type import GETAccountSummarySubscriptionType  # noqa: F401,E501
from zuora_client.models.get_account_summary_type_basic_info import GETAccountSummaryTypeBasicInfo  # noqa: F401,E501
from zuora_client.models.get_account_summary_type_bill_to_contact import GETAccountSummaryTypeBillToContact  # noqa: F401,E501
from zuora_client.models.get_account_summary_type_sold_to_contact import GETAccountSummaryTypeSoldToContact  # noqa: F401,E501
from zuora_client.models.get_account_summary_type_tax_info import GETAccountSummaryTypeTaxInfo  # noqa: F401,E501
from zuora_client.models.get_account_summary_usage_type import GETAccountSummaryUsageType  # noqa: F401,E501


class GETAccountSummaryType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'basic_info': 'GETAccountSummaryTypeBasicInfo',
        'bill_to_contact': 'GETAccountSummaryTypeBillToContact',
        'invoices': 'list[GETAccountSummaryInvoiceType]',
        'payments': 'list[GETAccountSummaryPaymentType]',
        'sold_to_contact': 'GETAccountSummaryTypeSoldToContact',
        'subscriptions': 'list[GETAccountSummarySubscriptionType]',
        'success': 'bool',
        'tax_info': 'GETAccountSummaryTypeTaxInfo',
        'usage': 'list[GETAccountSummaryUsageType]'
    }

    attribute_map = {
        'basic_info': 'basicInfo',
        'bill_to_contact': 'billToContact',
        'invoices': 'invoices',
        'payments': 'payments',
        'sold_to_contact': 'soldToContact',
        'subscriptions': 'subscriptions',
        'success': 'success',
        'tax_info': 'taxInfo',
        'usage': 'usage'
    }

    def __init__(self, basic_info=None, bill_to_contact=None, invoices=None, payments=None, sold_to_contact=None, subscriptions=None, success=None, tax_info=None, usage=None):  # noqa: E501
        """GETAccountSummaryType - a model defined in Swagger"""  # noqa: E501

        self._basic_info = None
        self._bill_to_contact = None
        self._invoices = None
        self._payments = None
        self._sold_to_contact = None
        self._subscriptions = None
        self._success = None
        self._tax_info = None
        self._usage = None
        self.discriminator = None

        if basic_info is not None:
            self.basic_info = basic_info
        if bill_to_contact is not None:
            self.bill_to_contact = bill_to_contact
        if invoices is not None:
            self.invoices = invoices
        if payments is not None:
            self.payments = payments
        if sold_to_contact is not None:
            self.sold_to_contact = sold_to_contact
        if subscriptions is not None:
            self.subscriptions = subscriptions
        if success is not None:
            self.success = success
        if tax_info is not None:
            self.tax_info = tax_info
        if usage is not None:
            self.usage = usage

    @property
    def basic_info(self):
        """Gets the basic_info of this GETAccountSummaryType.  # noqa: E501


        :return: The basic_info of this GETAccountSummaryType.  # noqa: E501
        :rtype: GETAccountSummaryTypeBasicInfo
        """
        return self._basic_info

    @basic_info.setter
    def basic_info(self, basic_info):
        """Sets the basic_info of this GETAccountSummaryType.


        :param basic_info: The basic_info of this GETAccountSummaryType.  # noqa: E501
        :type: GETAccountSummaryTypeBasicInfo
        """

        self._basic_info = basic_info

    @property
    def bill_to_contact(self):
        """Gets the bill_to_contact of this GETAccountSummaryType.  # noqa: E501


        :return: The bill_to_contact of this GETAccountSummaryType.  # noqa: E501
        :rtype: GETAccountSummaryTypeBillToContact
        """
        return self._bill_to_contact

    @bill_to_contact.setter
    def bill_to_contact(self, bill_to_contact):
        """Sets the bill_to_contact of this GETAccountSummaryType.


        :param bill_to_contact: The bill_to_contact of this GETAccountSummaryType.  # noqa: E501
        :type: GETAccountSummaryTypeBillToContact
        """

        self._bill_to_contact = bill_to_contact

    @property
    def invoices(self):
        """Gets the invoices of this GETAccountSummaryType.  # noqa: E501

        Container for invoices. Only returns the last 6 invoices.   # noqa: E501

        :return: The invoices of this GETAccountSummaryType.  # noqa: E501
        :rtype: list[GETAccountSummaryInvoiceType]
        """
        return self._invoices

    @invoices.setter
    def invoices(self, invoices):
        """Sets the invoices of this GETAccountSummaryType.

        Container for invoices. Only returns the last 6 invoices.   # noqa: E501

        :param invoices: The invoices of this GETAccountSummaryType.  # noqa: E501
        :type: list[GETAccountSummaryInvoiceType]
        """

        self._invoices = invoices

    @property
    def payments(self):
        """Gets the payments of this GETAccountSummaryType.  # noqa: E501

        Container for payments. Only returns the last 6 payments.   # noqa: E501

        :return: The payments of this GETAccountSummaryType.  # noqa: E501
        :rtype: list[GETAccountSummaryPaymentType]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this GETAccountSummaryType.

        Container for payments. Only returns the last 6 payments.   # noqa: E501

        :param payments: The payments of this GETAccountSummaryType.  # noqa: E501
        :type: list[GETAccountSummaryPaymentType]
        """

        self._payments = payments

    @property
    def sold_to_contact(self):
        """Gets the sold_to_contact of this GETAccountSummaryType.  # noqa: E501


        :return: The sold_to_contact of this GETAccountSummaryType.  # noqa: E501
        :rtype: GETAccountSummaryTypeSoldToContact
        """
        return self._sold_to_contact

    @sold_to_contact.setter
    def sold_to_contact(self, sold_to_contact):
        """Sets the sold_to_contact of this GETAccountSummaryType.


        :param sold_to_contact: The sold_to_contact of this GETAccountSummaryType.  # noqa: E501
        :type: GETAccountSummaryTypeSoldToContact
        """

        self._sold_to_contact = sold_to_contact

    @property
    def subscriptions(self):
        """Gets the subscriptions of this GETAccountSummaryType.  # noqa: E501

        Container for subscriptions.   # noqa: E501

        :return: The subscriptions of this GETAccountSummaryType.  # noqa: E501
        :rtype: list[GETAccountSummarySubscriptionType]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this GETAccountSummaryType.

        Container for subscriptions.   # noqa: E501

        :param subscriptions: The subscriptions of this GETAccountSummaryType.  # noqa: E501
        :type: list[GETAccountSummarySubscriptionType]
        """

        self._subscriptions = subscriptions

    @property
    def success(self):
        """Gets the success of this GETAccountSummaryType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GETAccountSummaryType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GETAccountSummaryType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GETAccountSummaryType.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def tax_info(self):
        """Gets the tax_info of this GETAccountSummaryType.  # noqa: E501


        :return: The tax_info of this GETAccountSummaryType.  # noqa: E501
        :rtype: GETAccountSummaryTypeTaxInfo
        """
        return self._tax_info

    @tax_info.setter
    def tax_info(self, tax_info):
        """Sets the tax_info of this GETAccountSummaryType.


        :param tax_info: The tax_info of this GETAccountSummaryType.  # noqa: E501
        :type: GETAccountSummaryTypeTaxInfo
        """

        self._tax_info = tax_info

    @property
    def usage(self):
        """Gets the usage of this GETAccountSummaryType.  # noqa: E501

        Container for usage data. Only returns the last 6 months of usage.  **Note:** If the [Active Rating](https://knowledgecenter.zuora.com/CB_Billing/J_Billing_Operations/H_Active_Rating) feature is enabled, no usage data is returned in the response body field. To retrive usage data information, you can use the [Usage (with Active Rating)](https://www.zuora.com/developer/active-rating-api/#tag/Usage-(with-Active-Rating)) operations.   # noqa: E501

        :return: The usage of this GETAccountSummaryType.  # noqa: E501
        :rtype: list[GETAccountSummaryUsageType]
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this GETAccountSummaryType.

        Container for usage data. Only returns the last 6 months of usage.  **Note:** If the [Active Rating](https://knowledgecenter.zuora.com/CB_Billing/J_Billing_Operations/H_Active_Rating) feature is enabled, no usage data is returned in the response body field. To retrive usage data information, you can use the [Usage (with Active Rating)](https://www.zuora.com/developer/active-rating-api/#tag/Usage-(with-Active-Rating)) operations.   # noqa: E501

        :param usage: The usage of this GETAccountSummaryType.  # noqa: E501
        :type: list[GETAccountSummaryUsageType]
        """

        self._usage = usage

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GETAccountSummaryType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GETAccountSummaryType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
