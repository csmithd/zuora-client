# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.rate_plan_object_custom_fields import RatePlanObjectCustomFields  # noqa: F401,E501


class RatePlanDataRatePlan(object):
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
        'amendment_id': 'str',
        'amendment_subscription_rate_plan_id': 'str',
        'amendment_type': 'str',
        'created_by_id': 'str',
        'created_date': 'datetime',
        'name': 'str',
        'product_rate_plan_id': 'str',
        'subscription_id': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'amendment_id': 'AmendmentId',
        'amendment_subscription_rate_plan_id': 'AmendmentSubscriptionRatePlanId',
        'amendment_type': 'AmendmentType',
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'name': 'Name',
        'product_rate_plan_id': 'ProductRatePlanId',
        'subscription_id': 'SubscriptionId',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, amendment_id=None, amendment_subscription_rate_plan_id=None, amendment_type=None, created_by_id=None, created_date=None, name=None, product_rate_plan_id=None, subscription_id=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """RatePlanDataRatePlan - a model defined in Swagger"""  # noqa: E501

        self._amendment_id = None
        self._amendment_subscription_rate_plan_id = None
        self._amendment_type = None
        self._created_by_id = None
        self._created_date = None
        self._name = None
        self._product_rate_plan_id = None
        self._subscription_id = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if amendment_id is not None:
            self.amendment_id = amendment_id
        if amendment_subscription_rate_plan_id is not None:
            self.amendment_subscription_rate_plan_id = amendment_subscription_rate_plan_id
        if amendment_type is not None:
            self.amendment_type = amendment_type
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if name is not None:
            self.name = name
        self.product_rate_plan_id = product_rate_plan_id
        if subscription_id is not None:
            self.subscription_id = subscription_id
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def amendment_id(self):
        """Gets the amendment_id of this RatePlanDataRatePlan.  # noqa: E501

         The ID of the amendment associated with the rate plan. This field only applies to amendment rate plans.   **Character limit**: 32   **Values**: a valid amendment ID   # noqa: E501

        :return: The amendment_id of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._amendment_id

    @amendment_id.setter
    def amendment_id(self, amendment_id):
        """Sets the amendment_id of this RatePlanDataRatePlan.

         The ID of the amendment associated with the rate plan. This field only applies to amendment rate plans.   **Character limit**: 32   **Values**: a valid amendment ID   # noqa: E501

        :param amendment_id: The amendment_id of this RatePlanDataRatePlan.  # noqa: E501
        :type: str
        """

        self._amendment_id = amendment_id

    @property
    def amendment_subscription_rate_plan_id(self):
        """Gets the amendment_subscription_rate_plan_id of this RatePlanDataRatePlan.  # noqa: E501

        The ID of the subscription rate plan modified by the amendment. This field only applies to amendment rate plans.  **Character limit**: 32   **Values**: a valid rate plan ID   # noqa: E501

        :return: The amendment_subscription_rate_plan_id of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._amendment_subscription_rate_plan_id

    @amendment_subscription_rate_plan_id.setter
    def amendment_subscription_rate_plan_id(self, amendment_subscription_rate_plan_id):
        """Sets the amendment_subscription_rate_plan_id of this RatePlanDataRatePlan.

        The ID of the subscription rate plan modified by the amendment. This field only applies to amendment rate plans.  **Character limit**: 32   **Values**: a valid rate plan ID   # noqa: E501

        :param amendment_subscription_rate_plan_id: The amendment_subscription_rate_plan_id of this RatePlanDataRatePlan.  # noqa: E501
        :type: str
        """

        self._amendment_subscription_rate_plan_id = amendment_subscription_rate_plan_id

    @property
    def amendment_type(self):
        """Gets the amendment_type of this RatePlanDataRatePlan.  # noqa: E501

        The type of amendment associated with the rate plan. This field only applies to amendment rate plans.  **Character limit**: 18   **Values**: inherited from `Amendment.Type`   # noqa: E501

        :return: The amendment_type of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._amendment_type

    @amendment_type.setter
    def amendment_type(self, amendment_type):
        """Sets the amendment_type of this RatePlanDataRatePlan.

        The type of amendment associated with the rate plan. This field only applies to amendment rate plans.  **Character limit**: 18   **Values**: inherited from `Amendment.Type`   # noqa: E501

        :param amendment_type: The amendment_type of this RatePlanDataRatePlan.  # noqa: E501
        :type: str
        """

        self._amendment_type = amendment_type

    @property
    def created_by_id(self):
        """Gets the created_by_id of this RatePlanDataRatePlan.  # noqa: E501

        The ID of the Zuora user who created the RatePlan object.  **Character limit**: 32   **Values**: automatically generated   # noqa: E501

        :return: The created_by_id of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this RatePlanDataRatePlan.

        The ID of the Zuora user who created the RatePlan object.  **Character limit**: 32   **Values**: automatically generated   # noqa: E501

        :param created_by_id: The created_by_id of this RatePlanDataRatePlan.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this RatePlanDataRatePlan.  # noqa: E501

        The date when the `RatePlan` object was last updated.  **Character limit**: 29   **Values**: automatically generated   # noqa: E501

        :return: The created_date of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this RatePlanDataRatePlan.

        The date when the `RatePlan` object was last updated.  **Character limit**: 29   **Values**: automatically generated   # noqa: E501

        :param created_date: The created_date of this RatePlanDataRatePlan.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def name(self):
        """Gets the name of this RatePlanDataRatePlan.  # noqa: E501

        The name of the rate plan. Leave this null in a subscribe call to inherited the `ProductRatePlan.Name` field value.  **Character limit**: 100   **Values**: a string of 100 characters or fewer or inherited from ProductRatePlan.Name   # noqa: E501

        :return: The name of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RatePlanDataRatePlan.

        The name of the rate plan. Leave this null in a subscribe call to inherited the `ProductRatePlan.Name` field value.  **Character limit**: 100   **Values**: a string of 100 characters or fewer or inherited from ProductRatePlan.Name   # noqa: E501

        :param name: The name of this RatePlanDataRatePlan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def product_rate_plan_id(self):
        """Gets the product_rate_plan_id of this RatePlanDataRatePlan.  # noqa: E501

        The ID of the associated product rate plan.  **Character limit**: 32   **Values**: a valid product rate plan ID   # noqa: E501

        :return: The product_rate_plan_id of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._product_rate_plan_id

    @product_rate_plan_id.setter
    def product_rate_plan_id(self, product_rate_plan_id):
        """Sets the product_rate_plan_id of this RatePlanDataRatePlan.

        The ID of the associated product rate plan.  **Character limit**: 32   **Values**: a valid product rate plan ID   # noqa: E501

        :param product_rate_plan_id: The product_rate_plan_id of this RatePlanDataRatePlan.  # noqa: E501
        :type: str
        """
        if product_rate_plan_id is None:
            raise ValueError("Invalid value for `product_rate_plan_id`, must not be `None`")  # noqa: E501

        self._product_rate_plan_id = product_rate_plan_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this RatePlanDataRatePlan.  # noqa: E501

        The ID of the subscription that the rate plan belongs to.  **Character limit**: 32   **Values**: a valid subscription ID   # noqa: E501

        :return: The subscription_id of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this RatePlanDataRatePlan.

        The ID of the subscription that the rate plan belongs to.  **Character limit**: 32   **Values**: a valid subscription ID   # noqa: E501

        :param subscription_id: The subscription_id of this RatePlanDataRatePlan.  # noqa: E501
        :type: str
        """

        self._subscription_id = subscription_id

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this RatePlanDataRatePlan.  # noqa: E501

         The ID of the user who last updated the rate plan.   **Character limit**: 32   **Values**: automatically generated   # noqa: E501

        :return: The updated_by_id of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this RatePlanDataRatePlan.

         The ID of the user who last updated the rate plan.   **Character limit**: 32   **Values**: automatically generated   # noqa: E501

        :param updated_by_id: The updated_by_id of this RatePlanDataRatePlan.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this RatePlanDataRatePlan.  # noqa: E501

         The date when the rate plan was last updated.   **Character limit**: 29   **Values**: automatically generated   # noqa: E501

        :return: The updated_date of this RatePlanDataRatePlan.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this RatePlanDataRatePlan.

         The date when the rate plan was last updated.   **Character limit**: 29   **Values**: automatically generated   # noqa: E501

        :param updated_date: The updated_date of this RatePlanDataRatePlan.  # noqa: E501
        :type: datetime
        """

        self._updated_date = updated_date

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
        if issubclass(RatePlanDataRatePlan, dict):
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
        if not isinstance(other, RatePlanDataRatePlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
