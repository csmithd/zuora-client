# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.common_response_type import CommonResponseType  # noqa: F401,E501
from zuora_client.models.post_payment_method_response_reasons import POSTPaymentMethodResponseReasons  # noqa: F401,E501


class POSTPaymentMethodResponse(object):
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
        'success': 'bool',
        'id': 'str',
        'reasons': 'list[POSTPaymentMethodResponseReasons]'
    }

    attribute_map = {
        'success': 'success',
        'id': 'id',
        'reasons': 'reasons'
    }

    def __init__(self, success=None, id=None, reasons=None):  # noqa: E501
        """POSTPaymentMethodResponse - a model defined in Swagger"""  # noqa: E501

        self._success = None
        self._id = None
        self._reasons = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if id is not None:
            self.id = id
        if reasons is not None:
            self.reasons = reasons

    @property
    def success(self):
        """Gets the success of this POSTPaymentMethodResponse.  # noqa: E501

        Indicates whether the call succeeded.   # noqa: E501

        :return: The success of this POSTPaymentMethodResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this POSTPaymentMethodResponse.

        Indicates whether the call succeeded.   # noqa: E501

        :param success: The success of this POSTPaymentMethodResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def id(self):
        """Gets the id of this POSTPaymentMethodResponse.  # noqa: E501

        Internal ID of the payment method that was created.   # noqa: E501

        :return: The id of this POSTPaymentMethodResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this POSTPaymentMethodResponse.

        Internal ID of the payment method that was created.   # noqa: E501

        :param id: The id of this POSTPaymentMethodResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def reasons(self):
        """Gets the reasons of this POSTPaymentMethodResponse.  # noqa: E501


        :return: The reasons of this POSTPaymentMethodResponse.  # noqa: E501
        :rtype: list[POSTPaymentMethodResponseReasons]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this POSTPaymentMethodResponse.


        :param reasons: The reasons of this POSTPaymentMethodResponse.  # noqa: E501
        :type: list[POSTPaymentMethodResponseReasons]
        """

        self._reasons = reasons

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
        if issubclass(POSTPaymentMethodResponse, dict):
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
        if not isinstance(other, POSTPaymentMethodResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other