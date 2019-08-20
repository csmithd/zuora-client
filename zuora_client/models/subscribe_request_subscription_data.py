# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.rate_plan_data import RatePlanData  # noqa: F401,E501
from zuora_client.models.subscribe_request_subscription_data_subscription import SubscribeRequestSubscriptionDataSubscription  # noqa: F401,E501


class SubscribeRequestSubscriptionData(object):
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
        'rate_plan_data': 'list[RatePlanData]',
        'subscription': 'SubscribeRequestSubscriptionDataSubscription'
    }

    attribute_map = {
        'rate_plan_data': 'RatePlanData',
        'subscription': 'Subscription'
    }

    def __init__(self, rate_plan_data=None, subscription=None):  # noqa: E501
        """SubscribeRequestSubscriptionData - a model defined in Swagger"""  # noqa: E501

        self._rate_plan_data = None
        self._subscription = None
        self.discriminator = None

        self.rate_plan_data = rate_plan_data
        self.subscription = subscription

    @property
    def rate_plan_data(self):
        """Gets the rate_plan_data of this SubscribeRequestSubscriptionData.  # noqa: E501

          # noqa: E501

        :return: The rate_plan_data of this SubscribeRequestSubscriptionData.  # noqa: E501
        :rtype: list[RatePlanData]
        """
        return self._rate_plan_data

    @rate_plan_data.setter
    def rate_plan_data(self, rate_plan_data):
        """Sets the rate_plan_data of this SubscribeRequestSubscriptionData.

          # noqa: E501

        :param rate_plan_data: The rate_plan_data of this SubscribeRequestSubscriptionData.  # noqa: E501
        :type: list[RatePlanData]
        """
        if rate_plan_data is None:
            raise ValueError("Invalid value for `rate_plan_data`, must not be `None`")  # noqa: E501

        self._rate_plan_data = rate_plan_data

    @property
    def subscription(self):
        """Gets the subscription of this SubscribeRequestSubscriptionData.  # noqa: E501


        :return: The subscription of this SubscribeRequestSubscriptionData.  # noqa: E501
        :rtype: SubscribeRequestSubscriptionDataSubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscribeRequestSubscriptionData.


        :param subscription: The subscription of this SubscribeRequestSubscriptionData.  # noqa: E501
        :type: SubscribeRequestSubscriptionDataSubscription
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")  # noqa: E501

        self._subscription = subscription

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
        if issubclass(SubscribeRequestSubscriptionData, dict):
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
        if not isinstance(other, SubscribeRequestSubscriptionData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other