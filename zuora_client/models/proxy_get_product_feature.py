# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.product_feature_object_custom_fields import ProductFeatureObjectCustomFields  # noqa: F401,E501


class ProxyGetProductFeature(object):
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
        'created_by_id': 'str',
        'created_date': 'datetime',
        'feature_id': 'str',
        'id': 'str',
        'product_id': 'str',
        'updated_by_id': 'str',
        'updated_date': 'datetime'
    }

    attribute_map = {
        'created_by_id': 'CreatedById',
        'created_date': 'CreatedDate',
        'feature_id': 'FeatureId',
        'id': 'Id',
        'product_id': 'ProductId',
        'updated_by_id': 'UpdatedById',
        'updated_date': 'UpdatedDate'
    }

    def __init__(self, created_by_id=None, created_date=None, feature_id=None, id=None, product_id=None, updated_by_id=None, updated_date=None):  # noqa: E501
        """ProxyGetProductFeature - a model defined in Swagger"""  # noqa: E501

        self._created_by_id = None
        self._created_date = None
        self._feature_id = None
        self._id = None
        self._product_id = None
        self._updated_by_id = None
        self._updated_date = None
        self.discriminator = None

        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_date is not None:
            self.created_date = created_date
        if feature_id is not None:
            self.feature_id = feature_id
        if id is not None:
            self.id = id
        if product_id is not None:
            self.product_id = product_id
        if updated_by_id is not None:
            self.updated_by_id = updated_by_id
        if updated_date is not None:
            self.updated_date = updated_date

    @property
    def created_by_id(self):
        """Gets the created_by_id of this ProxyGetProductFeature.  # noqa: E501

        The ID of the Zuora user who created the Account object. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The created_by_id of this ProxyGetProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this ProxyGetProductFeature.

        The ID of the Zuora user who created the Account object. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param created_by_id: The created_by_id of this ProxyGetProductFeature.  # noqa: E501
        :type: str
        """

        self._created_by_id = created_by_id

    @property
    def created_date(self):
        """Gets the created_date of this ProxyGetProductFeature.  # noqa: E501

        The date when the Account object was created. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The created_date of this ProxyGetProductFeature.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProxyGetProductFeature.

        The date when the Account object was created. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param created_date: The created_date of this ProxyGetProductFeature.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def feature_id(self):
        """Gets the feature_id of this ProxyGetProductFeature.  # noqa: E501

         Internal Zuora ID of the product feature. This field is not editable. **Character limit**: 32 **Values**: a string of 32 characters or fewer   # noqa: E501

        :return: The feature_id of this ProxyGetProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._feature_id

    @feature_id.setter
    def feature_id(self, feature_id):
        """Sets the feature_id of this ProxyGetProductFeature.

         Internal Zuora ID of the product feature. This field is not editable. **Character limit**: 32 **Values**: a string of 32 characters or fewer   # noqa: E501

        :param feature_id: The feature_id of this ProxyGetProductFeature.  # noqa: E501
        :type: str
        """

        self._feature_id = feature_id

    @property
    def id(self):
        """Gets the id of this ProxyGetProductFeature.  # noqa: E501

        Object identifier.  # noqa: E501

        :return: The id of this ProxyGetProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProxyGetProductFeature.

        Object identifier.  # noqa: E501

        :param id: The id of this ProxyGetProductFeature.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def product_id(self):
        """Gets the product_id of this ProxyGetProductFeature.  # noqa: E501

         Id of the product to which the feature belongs. This field is not editable. **Character limit**: 32 **Values**: a string of 32 characters or fewer   # noqa: E501

        :return: The product_id of this ProxyGetProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ProxyGetProductFeature.

         Id of the product to which the feature belongs. This field is not editable. **Character limit**: 32 **Values**: a string of 32 characters or fewer   # noqa: E501

        :param product_id: The product_id of this ProxyGetProductFeature.  # noqa: E501
        :type: str
        """

        self._product_id = product_id

    @property
    def updated_by_id(self):
        """Gets the updated_by_id of this ProxyGetProductFeature.  # noqa: E501

        The ID of the user who last updated the account. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :return: The updated_by_id of this ProxyGetProductFeature.  # noqa: E501
        :rtype: str
        """
        return self._updated_by_id

    @updated_by_id.setter
    def updated_by_id(self, updated_by_id):
        """Sets the updated_by_id of this ProxyGetProductFeature.

        The ID of the user who last updated the account. **Character limit**: 32 **Values**: automatically generated   # noqa: E501

        :param updated_by_id: The updated_by_id of this ProxyGetProductFeature.  # noqa: E501
        :type: str
        """

        self._updated_by_id = updated_by_id

    @property
    def updated_date(self):
        """Gets the updated_date of this ProxyGetProductFeature.  # noqa: E501

        The date when the account was last updated. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :return: The updated_date of this ProxyGetProductFeature.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_date

    @updated_date.setter
    def updated_date(self, updated_date):
        """Sets the updated_date of this ProxyGetProductFeature.

        The date when the account was last updated. **Character limit**: 29 **Values**: automatically generated   # noqa: E501

        :param updated_date: The updated_date of this ProxyGetProductFeature.  # noqa: E501
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
        if issubclass(ProxyGetProductFeature, dict):
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
        if not isinstance(other, ProxyGetProductFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other