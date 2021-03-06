# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.link_query_job_common import LinkQueryJobCommon  # noqa: F401,E501


class LinkQueryJob(object):
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
        'id': 'str',
        'query': 'str',
        'remaining_retries': 'int',
        'updated_on': 'datetime',
        'data_file': 'str',
        'output_rows': 'int',
        'processing_time': 'int',
        'query_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'query': 'query',
        'remaining_retries': 'remainingRetries',
        'updated_on': 'updatedOn',
        'data_file': 'dataFile',
        'output_rows': 'outputRows',
        'processing_time': 'processingTime',
        'query_status': 'queryStatus'
    }

    def __init__(self, id=None, query=None, remaining_retries=None, updated_on=None, data_file=None, output_rows=None, processing_time=None, query_status=None):  # noqa: E501
        """LinkQueryJob - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._query = None
        self._remaining_retries = None
        self._updated_on = None
        self._data_file = None
        self._output_rows = None
        self._processing_time = None
        self._query_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if query is not None:
            self.query = query
        if remaining_retries is not None:
            self.remaining_retries = remaining_retries
        if updated_on is not None:
            self.updated_on = updated_on
        if data_file is not None:
            self.data_file = data_file
        if output_rows is not None:
            self.output_rows = output_rows
        if processing_time is not None:
            self.processing_time = processing_time
        if query_status is not None:
            self.query_status = query_status

    @property
    def id(self):
        """Gets the id of this LinkQueryJob.  # noqa: E501

        Internal identifier of the query job.   # noqa: E501

        :return: The id of this LinkQueryJob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LinkQueryJob.

        Internal identifier of the query job.   # noqa: E501

        :param id: The id of this LinkQueryJob.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def query(self):
        """Gets the query of this LinkQueryJob.  # noqa: E501

        The query that was submitted.   # noqa: E501

        :return: The query of this LinkQueryJob.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this LinkQueryJob.

        The query that was submitted.   # noqa: E501

        :param query: The query of this LinkQueryJob.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def remaining_retries(self):
        """Gets the remaining_retries of this LinkQueryJob.  # noqa: E501

        The number of times that Zuora will retry the query if Zuora is unable to perform the query.   # noqa: E501

        :return: The remaining_retries of this LinkQueryJob.  # noqa: E501
        :rtype: int
        """
        return self._remaining_retries

    @remaining_retries.setter
    def remaining_retries(self, remaining_retries):
        """Sets the remaining_retries of this LinkQueryJob.

        The number of times that Zuora will retry the query if Zuora is unable to perform the query.   # noqa: E501

        :param remaining_retries: The remaining_retries of this LinkQueryJob.  # noqa: E501
        :type: int
        """

        self._remaining_retries = remaining_retries

    @property
    def updated_on(self):
        """Gets the updated_on of this LinkQueryJob.  # noqa: E501

        Date and time when the query job was last updated, in ISO 8601 format.   # noqa: E501

        :return: The updated_on of this LinkQueryJob.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this LinkQueryJob.

        Date and time when the query job was last updated, in ISO 8601 format.   # noqa: E501

        :param updated_on: The updated_on of this LinkQueryJob.  # noqa: E501
        :type: datetime
        """

        self._updated_on = updated_on

    @property
    def data_file(self):
        """Gets the data_file of this LinkQueryJob.  # noqa: E501

        The URL of the query results. Only applicable if the value of the `queryStatus` field is `completed`.   # noqa: E501

        :return: The data_file of this LinkQueryJob.  # noqa: E501
        :rtype: str
        """
        return self._data_file

    @data_file.setter
    def data_file(self, data_file):
        """Sets the data_file of this LinkQueryJob.

        The URL of the query results. Only applicable if the value of the `queryStatus` field is `completed`.   # noqa: E501

        :param data_file: The data_file of this LinkQueryJob.  # noqa: E501
        :type: str
        """

        self._data_file = data_file

    @property
    def output_rows(self):
        """Gets the output_rows of this LinkQueryJob.  # noqa: E501

        The number of rows the query results. Only applicable if the value of the `queryStatus` field is `completed`.   # noqa: E501

        :return: The output_rows of this LinkQueryJob.  # noqa: E501
        :rtype: int
        """
        return self._output_rows

    @output_rows.setter
    def output_rows(self, output_rows):
        """Sets the output_rows of this LinkQueryJob.

        The number of rows the query results. Only applicable if the value of the `queryStatus` field is `completed`.   # noqa: E501

        :param output_rows: The output_rows of this LinkQueryJob.  # noqa: E501
        :type: int
        """

        self._output_rows = output_rows

    @property
    def processing_time(self):
        """Gets the processing_time of this LinkQueryJob.  # noqa: E501

        Processing time of the query job, in milliseconds. Only applicable if the value of the `queryStatus` field is `completed`.   # noqa: E501

        :return: The processing_time of this LinkQueryJob.  # noqa: E501
        :rtype: int
        """
        return self._processing_time

    @processing_time.setter
    def processing_time(self, processing_time):
        """Sets the processing_time of this LinkQueryJob.

        Processing time of the query job, in milliseconds. Only applicable if the value of the `queryStatus` field is `completed`.   # noqa: E501

        :param processing_time: The processing_time of this LinkQueryJob.  # noqa: E501
        :type: int
        """

        self._processing_time = processing_time

    @property
    def query_status(self):
        """Gets the query_status of this LinkQueryJob.  # noqa: E501

        Status of the query job.  If the value of this field is `completed`, the `dataFile` field contains the location of the query results.  If the value of this field is `accepted` or `in_progress`, you can use [Cancel Link query job](#operation/DELETE_LinkQueryJob) to prevent Zuora from performing the query. Zuora then sets the status of the query job to `cancelled`.   # noqa: E501

        :return: The query_status of this LinkQueryJob.  # noqa: E501
        :rtype: str
        """
        return self._query_status

    @query_status.setter
    def query_status(self, query_status):
        """Sets the query_status of this LinkQueryJob.

        Status of the query job.  If the value of this field is `completed`, the `dataFile` field contains the location of the query results.  If the value of this field is `accepted` or `in_progress`, you can use [Cancel Link query job](#operation/DELETE_LinkQueryJob) to prevent Zuora from performing the query. Zuora then sets the status of the query job to `cancelled`.   # noqa: E501

        :param query_status: The query_status of this LinkQueryJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["accepted", "in_progress", "completed", "failed", "cancelled"]  # noqa: E501
        if query_status not in allowed_values:
            raise ValueError(
                "Invalid value for `query_status` ({0}), must be one of {1}"  # noqa: E501
                .format(query_status, allowed_values)
            )

        self._query_status = query_status

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
        if issubclass(LinkQueryJob, dict):
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
        if not isinstance(other, LinkQueryJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
