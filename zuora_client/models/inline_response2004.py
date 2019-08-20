# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.job_result import JobResult  # noqa: F401,E501


class InlineResponse2004(object):
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
        'status': 'str',
        'errors': 'str',
        'result': 'JobResult',
        'success': 'bool'
    }

    attribute_map = {
        'status': 'status',
        'errors': 'errors',
        'result': 'result',
        'success': 'success'
    }

    def __init__(self, status=None, errors=None, result=None, success=None):  # noqa: E501
        """InlineResponse2004 - a model defined in Swagger"""  # noqa: E501

        self._status = None
        self._errors = None
        self._result = None
        self._success = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if errors is not None:
            self.errors = errors
        if result is not None:
            self.result = result
        if success is not None:
            self.success = success

    @property
    def status(self):
        """Gets the status of this InlineResponse2004.  # noqa: E501

        Type of job status.  # noqa: E501

        :return: The status of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse2004.

        Type of job status.  # noqa: E501

        :param status: The status of this InlineResponse2004.  # noqa: E501
        :type: str
        """
        allowed_values = ["Processing", "Failed", "Completed"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def errors(self):
        """Gets the errors of this InlineResponse2004.  # noqa: E501

        Error messages returned if the job failed.  # noqa: E501

        :return: The errors of this InlineResponse2004.  # noqa: E501
        :rtype: str
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this InlineResponse2004.

        Error messages returned if the job failed.  # noqa: E501

        :param errors: The errors of this InlineResponse2004.  # noqa: E501
        :type: str
        """

        self._errors = errors

    @property
    def result(self):
        """Gets the result of this InlineResponse2004.  # noqa: E501


        :return: The result of this InlineResponse2004.  # noqa: E501
        :rtype: JobResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this InlineResponse2004.


        :param result: The result of this InlineResponse2004.  # noqa: E501
        :type: JobResult
        """

        self._result = result

    @property
    def success(self):
        """Gets the success of this InlineResponse2004.  # noqa: E501

        Indicates whether the operation call succeeded.  # noqa: E501

        :return: The success of this InlineResponse2004.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse2004.

        Indicates whether the operation call succeeded.  # noqa: E501

        :param success: The success of this InlineResponse2004.  # noqa: E501
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
        if issubclass(InlineResponse2004, dict):
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
        if not isinstance(other, InlineResponse2004):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other