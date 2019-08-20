# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.product_feature_object_custom_fields import ProductFeatureObjectCustomFields  # noqa: F401,E501


class GetProductFeatureType(object):
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
        'code': 'str',
        'description': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'id': 'id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, code=None, description=None, id=None, name=None, status=None):  # noqa: E501
        """GetProductFeatureType - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._description = None
        self._id = None
        self._name = None
        self._status = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def code(self):
        """Gets the code of this GetProductFeatureType.  # noqa: E501

        Feature code, up to 255 characters long.   # noqa: E501

        :return: The code of this GetProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GetProductFeatureType.

        Feature code, up to 255 characters long.   # noqa: E501

        :param code: The code of this GetProductFeatureType.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this GetProductFeatureType.  # noqa: E501

        Feature description.   # noqa: E501

        :return: The description of this GetProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetProductFeatureType.

        Feature description.   # noqa: E501

        :param description: The description of this GetProductFeatureType.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this GetProductFeatureType.  # noqa: E501

        Feature ID.   # noqa: E501

        :return: The id of this GetProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetProductFeatureType.

        Feature ID.   # noqa: E501

        :param id: The id of this GetProductFeatureType.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetProductFeatureType.  # noqa: E501

        Feature name, up to 255 characters long.   # noqa: E501

        :return: The name of this GetProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetProductFeatureType.

        Feature name, up to 255 characters long.   # noqa: E501

        :param name: The name of this GetProductFeatureType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this GetProductFeatureType.  # noqa: E501

          # noqa: E501

        :return: The status of this GetProductFeatureType.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetProductFeatureType.

          # noqa: E501

        :param status: The status of this GetProductFeatureType.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(GetProductFeatureType, dict):
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
        if not isinstance(other, GetProductFeatureType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other