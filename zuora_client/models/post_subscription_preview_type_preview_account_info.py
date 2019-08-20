# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.account_object_custom_fields import AccountObjectCustomFields  # noqa: F401,E501
from zuora_client.models.account_object_ns_fields import AccountObjectNSFields  # noqa: F401,E501
from zuora_client.models.post_subscription_preview_type_preview_account_info_bill_to_contact import POSTSubscriptionPreviewTypePreviewAccountInfoBillToContact  # noqa: F401,E501


class POSTSubscriptionPreviewTypePreviewAccountInfo(object):
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
        'class__ns': 'str',
        'customer_type__ns': 'str',
        'department__ns': 'str',
        'integration_id__ns': 'str',
        'integration_status__ns': 'str',
        'location__ns': 'str',
        'subsidiary__ns': 'str',
        'sync_date__ns': 'str',
        'syncto_net_suite__ns': 'str',
        'bill_cycle_day': 'int',
        'bill_to_contact': 'POSTSubscriptionPreviewTypePreviewAccountInfoBillToContact',
        'currency': 'str'
    }

    attribute_map = {
        'class__ns': 'Class__NS',
        'customer_type__ns': 'CustomerType__NS',
        'department__ns': 'Department__NS',
        'integration_id__ns': 'IntegrationId__NS',
        'integration_status__ns': 'IntegrationStatus__NS',
        'location__ns': 'Location__NS',
        'subsidiary__ns': 'Subsidiary__NS',
        'sync_date__ns': 'SyncDate__NS',
        'syncto_net_suite__ns': 'SynctoNetSuite__NS',
        'bill_cycle_day': 'billCycleDay',
        'bill_to_contact': 'billToContact',
        'currency': 'currency'
    }

    def __init__(self, class__ns=None, customer_type__ns=None, department__ns=None, integration_id__ns=None, integration_status__ns=None, location__ns=None, subsidiary__ns=None, sync_date__ns=None, syncto_net_suite__ns=None, bill_cycle_day=None, bill_to_contact=None, currency=None):  # noqa: E501
        """POSTSubscriptionPreviewTypePreviewAccountInfo - a model defined in Swagger"""  # noqa: E501

        self._class__ns = None
        self._customer_type__ns = None
        self._department__ns = None
        self._integration_id__ns = None
        self._integration_status__ns = None
        self._location__ns = None
        self._subsidiary__ns = None
        self._sync_date__ns = None
        self._syncto_net_suite__ns = None
        self._bill_cycle_day = None
        self._bill_to_contact = None
        self._currency = None
        self.discriminator = None

        if class__ns is not None:
            self.class__ns = class__ns
        if customer_type__ns is not None:
            self.customer_type__ns = customer_type__ns
        if department__ns is not None:
            self.department__ns = department__ns
        if integration_id__ns is not None:
            self.integration_id__ns = integration_id__ns
        if integration_status__ns is not None:
            self.integration_status__ns = integration_status__ns
        if location__ns is not None:
            self.location__ns = location__ns
        if subsidiary__ns is not None:
            self.subsidiary__ns = subsidiary__ns
        if sync_date__ns is not None:
            self.sync_date__ns = sync_date__ns
        if syncto_net_suite__ns is not None:
            self.syncto_net_suite__ns = syncto_net_suite__ns
        self.bill_cycle_day = bill_cycle_day
        self.bill_to_contact = bill_to_contact
        self.currency = currency

    @property
    def class__ns(self):
        """Gets the class__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        Value of the Class field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The class__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._class__ns

    @class__ns.setter
    def class__ns(self, class__ns):
        """Sets the class__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        Value of the Class field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param class__ns: The class__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if class__ns is not None and len(class__ns) > 255:
            raise ValueError("Invalid value for `class__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._class__ns = class__ns

    @property
    def customer_type__ns(self):
        """Gets the customer_type__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        Value of the Customer Type field for the corresponding customer account in NetSuite. The Customer Type field is used when the customer account is created in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The customer_type__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._customer_type__ns

    @customer_type__ns.setter
    def customer_type__ns(self, customer_type__ns):
        """Sets the customer_type__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        Value of the Customer Type field for the corresponding customer account in NetSuite. The Customer Type field is used when the customer account is created in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param customer_type__ns: The customer_type__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Company", "Individual"]  # noqa: E501
        if customer_type__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `customer_type__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(customer_type__ns, allowed_values)
            )

        self._customer_type__ns = customer_type__ns

    @property
    def department__ns(self):
        """Gets the department__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        Value of the Department field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The department__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._department__ns

    @department__ns.setter
    def department__ns(self, department__ns):
        """Sets the department__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        Value of the Department field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param department__ns: The department__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if department__ns is not None and len(department__ns) > 255:
            raise ValueError("Invalid value for `department__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._department__ns = department__ns

    @property
    def integration_id__ns(self):
        """Gets the integration_id__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_id__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._integration_id__ns

    @integration_id__ns.setter
    def integration_id__ns(self, integration_id__ns):
        """Sets the integration_id__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        ID of the corresponding object in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_id__ns: The integration_id__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if integration_id__ns is not None and len(integration_id__ns) > 255:
            raise ValueError("Invalid value for `integration_id__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_id__ns = integration_id__ns

    @property
    def integration_status__ns(self):
        """Gets the integration_status__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        Status of the account's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The integration_status__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._integration_status__ns

    @integration_status__ns.setter
    def integration_status__ns(self, integration_status__ns):
        """Sets the integration_status__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        Status of the account's synchronization with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param integration_status__ns: The integration_status__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if integration_status__ns is not None and len(integration_status__ns) > 255:
            raise ValueError("Invalid value for `integration_status__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._integration_status__ns = integration_status__ns

    @property
    def location__ns(self):
        """Gets the location__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        Value of the Location field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The location__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._location__ns

    @location__ns.setter
    def location__ns(self, location__ns):
        """Sets the location__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        Value of the Location field for the corresponding customer account in NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param location__ns: The location__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if location__ns is not None and len(location__ns) > 255:
            raise ValueError("Invalid value for `location__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._location__ns = location__ns

    @property
    def subsidiary__ns(self):
        """Gets the subsidiary__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        Value of the Subsidiary field for the corresponding customer account in NetSuite. The Subsidiary field is required if you use NetSuite OneWorld. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The subsidiary__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._subsidiary__ns

    @subsidiary__ns.setter
    def subsidiary__ns(self, subsidiary__ns):
        """Sets the subsidiary__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        Value of the Subsidiary field for the corresponding customer account in NetSuite. The Subsidiary field is required if you use NetSuite OneWorld. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param subsidiary__ns: The subsidiary__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if subsidiary__ns is not None and len(subsidiary__ns) > 255:
            raise ValueError("Invalid value for `subsidiary__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._subsidiary__ns = subsidiary__ns

    @property
    def sync_date__ns(self):
        """Gets the sync_date__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        Date when the account was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The sync_date__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._sync_date__ns

    @sync_date__ns.setter
    def sync_date__ns(self, sync_date__ns):
        """Sets the sync_date__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        Date when the account was sychronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param sync_date__ns: The sync_date__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if sync_date__ns is not None and len(sync_date__ns) > 255:
            raise ValueError("Invalid value for `sync_date__ns`, length must be less than or equal to `255`")  # noqa: E501

        self._sync_date__ns = sync_date__ns

    @property
    def syncto_net_suite__ns(self):
        """Gets the syncto_net_suite__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        Specifies whether the account should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :return: The syncto_net_suite__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._syncto_net_suite__ns

    @syncto_net_suite__ns.setter
    def syncto_net_suite__ns(self, syncto_net_suite__ns):
        """Sets the syncto_net_suite__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        Specifies whether the account should be synchronized with NetSuite. Only available if you have installed the [Zuora Connector for NetSuite](https://www.zuora.com/connect/app/?appId=265).   # noqa: E501

        :param syncto_net_suite__ns: The syncto_net_suite__ns of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["Yes", "No"]  # noqa: E501
        if syncto_net_suite__ns not in allowed_values:
            raise ValueError(
                "Invalid value for `syncto_net_suite__ns` ({0}), must be one of {1}"  # noqa: E501
                .format(syncto_net_suite__ns, allowed_values)
            )

        self._syncto_net_suite__ns = syncto_net_suite__ns

    @property
    def bill_cycle_day(self):
        """Gets the bill_cycle_day of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        The account's bill cycle day (BCD), when bill runs generate invoices for the account. Specify any day of the month (`1`-`31`, where `31` = end-of-month), or `0` for auto-set.   # noqa: E501

        :return: The bill_cycle_day of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: int
        """
        return self._bill_cycle_day

    @bill_cycle_day.setter
    def bill_cycle_day(self, bill_cycle_day):
        """Sets the bill_cycle_day of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        The account's bill cycle day (BCD), when bill runs generate invoices for the account. Specify any day of the month (`1`-`31`, where `31` = end-of-month), or `0` for auto-set.   # noqa: E501

        :param bill_cycle_day: The bill_cycle_day of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: int
        """
        if bill_cycle_day is None:
            raise ValueError("Invalid value for `bill_cycle_day`, must not be `None`")  # noqa: E501

        self._bill_cycle_day = bill_cycle_day

    @property
    def bill_to_contact(self):
        """Gets the bill_to_contact of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501


        :return: The bill_to_contact of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: POSTSubscriptionPreviewTypePreviewAccountInfoBillToContact
        """
        return self._bill_to_contact

    @bill_to_contact.setter
    def bill_to_contact(self, bill_to_contact):
        """Sets the bill_to_contact of this POSTSubscriptionPreviewTypePreviewAccountInfo.


        :param bill_to_contact: The bill_to_contact of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: POSTSubscriptionPreviewTypePreviewAccountInfoBillToContact
        """
        if bill_to_contact is None:
            raise ValueError("Invalid value for `bill_to_contact`, must not be `None`")  # noqa: E501

        self._bill_to_contact = bill_to_contact

    @property
    def currency(self):
        """Gets the currency of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501

        A currency as defined in Billing Settings.   # noqa: E501

        :return: The currency of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this POSTSubscriptionPreviewTypePreviewAccountInfo.

        A currency as defined in Billing Settings.   # noqa: E501

        :param currency: The currency of this POSTSubscriptionPreviewTypePreviewAccountInfo.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

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
        if issubclass(POSTSubscriptionPreviewTypePreviewAccountInfo, dict):
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
        if not isinstance(other, POSTSubscriptionPreviewTypePreviewAccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other