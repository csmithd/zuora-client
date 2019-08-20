# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.get_accounting_period_without_success_type import GETAccountingPeriodWithoutSuccessType  # noqa: F401,E501


class GETAccountingPeriodsType(object):
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
        'accounting_periods': 'list[GETAccountingPeriodWithoutSuccessType]',
        'next_page': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'accounting_periods': 'accountingPeriods',
        'next_page': 'nextPage',
        'success': 'success'
    }

    def __init__(self, accounting_periods=None, next_page=None, success=None):  # noqa: E501
        """GETAccountingPeriodsType - a model defined in Swagger"""  # noqa: E501

        self._accounting_periods = None
        self._next_page = None
        self._success = None
        self.discriminator = None

        if accounting_periods is not None:
            self.accounting_periods = accounting_periods
        if next_page is not None:
            self.next_page = next_page
        if success is not None:
            self.success = success

    @property
    def accounting_periods(self):
        """Gets the accounting_periods of this GETAccountingPeriodsType.  # noqa: E501

        An array of all accounting periods on your tenant. The accounting periods are returned in ascending order of start date; that is, the latest period is returned first.   # noqa: E501

        :return: The accounting_periods of this GETAccountingPeriodsType.  # noqa: E501
        :rtype: list[GETAccountingPeriodWithoutSuccessType]
        """
        return self._accounting_periods

    @accounting_periods.setter
    def accounting_periods(self, accounting_periods):
        """Sets the accounting_periods of this GETAccountingPeriodsType.

        An array of all accounting periods on your tenant. The accounting periods are returned in ascending order of start date; that is, the latest period is returned first.   # noqa: E501

        :param accounting_periods: The accounting_periods of this GETAccountingPeriodsType.  # noqa: E501
        :type: list[GETAccountingPeriodWithoutSuccessType]
        """

        self._accounting_periods = accounting_periods

    @property
    def next_page(self):
        """Gets the next_page of this GETAccountingPeriodsType.  # noqa: E501

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :return: The next_page of this GETAccountingPeriodsType.  # noqa: E501
        :rtype: str
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this GETAccountingPeriodsType.

        URL to retrieve the next page of the response if it exists; otherwise absent.   # noqa: E501

        :param next_page: The next_page of this GETAccountingPeriodsType.  # noqa: E501
        :type: str
        """

        self._next_page = next_page

    @property
    def success(self):
        """Gets the success of this GETAccountingPeriodsType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this GETAccountingPeriodsType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this GETAccountingPeriodsType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this GETAccountingPeriodsType.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(GETAccountingPeriodsType, dict):
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
        if not isinstance(other, GETAccountingPeriodsType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other