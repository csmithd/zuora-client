# coding: utf-8




import pprint
import re  # noqa: F401

import six


class GETSubscriptionProductFeatureType(object):
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
        'description': 'str',
        'feature_code': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'feature_code': 'featureCode',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, description=None, feature_code=None, id=None, name=None):  # noqa: E501
        """GETSubscriptionProductFeatureType - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._feature_code = None
        self._id = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if feature_code is not None:
            self.feature_code = feature_code
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this GETSubscriptionProductFeatureType.  # noqa: E501

        Feature description.   # noqa: E501

        :return: The description of this GETSubscriptionProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GETSubscriptionProductFeatureType.

        Feature description.   # noqa: E501

        :param description: The description of this GETSubscriptionProductFeatureType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def feature_code(self):
        """Gets the feature_code of this GETSubscriptionProductFeatureType.  # noqa: E501

        Feature code, up to 255 characters long.   # noqa: E501

        :return: The feature_code of this GETSubscriptionProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._feature_code

    @feature_code.setter
    def feature_code(self, feature_code):
        """Sets the feature_code of this GETSubscriptionProductFeatureType.

        Feature code, up to 255 characters long.   # noqa: E501

        :param feature_code: The feature_code of this GETSubscriptionProductFeatureType.  # noqa: E501
        :type: str
        """

        self._feature_code = feature_code

    @property
    def id(self):
        """Gets the id of this GETSubscriptionProductFeatureType.  # noqa: E501

        SubscriptionProductFeature ID.   # noqa: E501

        :return: The id of this GETSubscriptionProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GETSubscriptionProductFeatureType.

        SubscriptionProductFeature ID.   # noqa: E501

        :param id: The id of this GETSubscriptionProductFeatureType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GETSubscriptionProductFeatureType.  # noqa: E501

        Feature name, up to 255 characters long.   # noqa: E501

        :return: The name of this GETSubscriptionProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GETSubscriptionProductFeatureType.

        Feature name, up to 255 characters long.   # noqa: E501

        :param name: The name of this GETSubscriptionProductFeatureType.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(GETSubscriptionProductFeatureType, dict):
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
        if not isinstance(other, GETSubscriptionProductFeatureType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other