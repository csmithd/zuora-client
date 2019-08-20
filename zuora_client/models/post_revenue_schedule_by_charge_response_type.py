# coding: utf-8




import pprint
import re  # noqa: F401

import six


class POSTRevenueScheduleByChargeResponseType(object):
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
        'revenue_schedule_number': 'str',
        'success': 'bool'
    }

    attribute_map = {
        'revenue_schedule_number': 'revenueScheduleNumber',
        'success': 'success'
    }

    def __init__(self, revenue_schedule_number=None, success=None):  # noqa: E501
        """POSTRevenueScheduleByChargeResponseType - a model defined in Swagger"""  # noqa: E501

        self._revenue_schedule_number = None
        self._success = None
        self.discriminator = None

        if revenue_schedule_number is not None:
            self.revenue_schedule_number = revenue_schedule_number
        if success is not None:
            self.success = success

    @property
    def revenue_schedule_number(self):
        """Gets the revenue_schedule_number of this POSTRevenueScheduleByChargeResponseType.  # noqa: E501

        Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".   # noqa: E501

        :return: The revenue_schedule_number of this POSTRevenueScheduleByChargeResponseType.  # noqa: E501
        :rtype: str
        """
        return self._revenue_schedule_number

    @revenue_schedule_number.setter
    def revenue_schedule_number(self, revenue_schedule_number):
        """Sets the revenue_schedule_number of this POSTRevenueScheduleByChargeResponseType.

        Revenue schedule number. The revenue schedule number is always prefixed with \"RS\", for example, \"RS-00000001\".   # noqa: E501

        :param revenue_schedule_number: The revenue_schedule_number of this POSTRevenueScheduleByChargeResponseType.  # noqa: E501
        :type: str
        """

        self._revenue_schedule_number = revenue_schedule_number

    @property
    def success(self):
        """Gets the success of this POSTRevenueScheduleByChargeResponseType.  # noqa: E501

        Returns `true` if the request was processed successfully.   # noqa: E501

        :return: The success of this POSTRevenueScheduleByChargeResponseType.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this POSTRevenueScheduleByChargeResponseType.

        Returns `true` if the request was processed successfully.   # noqa: E501

        :param success: The success of this POSTRevenueScheduleByChargeResponseType.  # noqa: E501
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
        if issubclass(POSTRevenueScheduleByChargeResponseType, dict):
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
        if not isinstance(other, POSTRevenueScheduleByChargeResponseType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other