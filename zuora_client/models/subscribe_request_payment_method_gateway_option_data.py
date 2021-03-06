# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.gateway_option import GatewayOption  # noqa: F401,E501


class SubscribeRequestPaymentMethodGatewayOptionData(object):
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
        'gateway_option': 'list[GatewayOption]'
    }

    attribute_map = {
        'gateway_option': 'GatewayOption'
    }

    def __init__(self, gateway_option=None):  # noqa: E501
        """SubscribeRequestPaymentMethodGatewayOptionData - a model defined in Swagger"""  # noqa: E501

        self._gateway_option = None
        self.discriminator = None

        self.gateway_option = gateway_option

    @property
    def gateway_option(self):
        """Gets the gateway_option of this SubscribeRequestPaymentMethodGatewayOptionData.  # noqa: E501

          # noqa: E501

        :return: The gateway_option of this SubscribeRequestPaymentMethodGatewayOptionData.  # noqa: E501
        :rtype: list[GatewayOption]
        """
        return self._gateway_option

    @gateway_option.setter
    def gateway_option(self, gateway_option):
        """Sets the gateway_option of this SubscribeRequestPaymentMethodGatewayOptionData.

          # noqa: E501

        :param gateway_option: The gateway_option of this SubscribeRequestPaymentMethodGatewayOptionData.  # noqa: E501
        :type: list[GatewayOption]
        """
        if gateway_option is None:
            raise ValueError("Invalid value for `gateway_option`, must not be `None`")  # noqa: E501

        self._gateway_option = gateway_option

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
        if issubclass(SubscribeRequestPaymentMethodGatewayOptionData, dict):
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
        if not isinstance(other, SubscribeRequestPaymentMethodGatewayOptionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
