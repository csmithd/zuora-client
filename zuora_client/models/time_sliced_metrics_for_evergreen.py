# coding: utf-8




import pprint
import re  # noqa: F401

import six


class TimeSlicedMetricsForEvergreen(object):
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
        'amount': 'float',
        'end_date': 'date',
        'invoice_owner': 'str',
        'start_date': 'date',
        'subscription_owner': 'str',
        'term_number': 'float'
    }

    attribute_map = {
        'amount': 'amount',
        'end_date': 'endDate',
        'invoice_owner': 'invoiceOwner',
        'start_date': 'startDate',
        'subscription_owner': 'subscriptionOwner',
        'term_number': 'termNumber'
    }

    def __init__(self, amount=None, end_date=None, invoice_owner=None, start_date=None, subscription_owner=None, term_number=None):  # noqa: E501
        """TimeSlicedMetricsForEvergreen - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._end_date = None
        self._invoice_owner = None
        self._start_date = None
        self._subscription_owner = None
        self._term_number = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if end_date is not None:
            self.end_date = end_date
        if invoice_owner is not None:
            self.invoice_owner = invoice_owner
        if start_date is not None:
            self.start_date = start_date
        if subscription_owner is not None:
            self.subscription_owner = subscription_owner
        if term_number is not None:
            self.term_number = term_number

    @property
    def amount(self):
        """Gets the amount of this TimeSlicedMetricsForEvergreen.  # noqa: E501


        :return: The amount of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TimeSlicedMetricsForEvergreen.


        :param amount: The amount of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def end_date(self):
        """Gets the end_date of this TimeSlicedMetricsForEvergreen.  # noqa: E501


        :return: The end_date of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :rtype: date
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this TimeSlicedMetricsForEvergreen.


        :param end_date: The end_date of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :type: date
        """

        self._end_date = end_date

    @property
    def invoice_owner(self):
        """Gets the invoice_owner of this TimeSlicedMetricsForEvergreen.  # noqa: E501

        The acount number of the billing account that is billed for the subscription.  # noqa: E501

        :return: The invoice_owner of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :rtype: str
        """
        return self._invoice_owner

    @invoice_owner.setter
    def invoice_owner(self, invoice_owner):
        """Sets the invoice_owner of this TimeSlicedMetricsForEvergreen.

        The acount number of the billing account that is billed for the subscription.  # noqa: E501

        :param invoice_owner: The invoice_owner of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :type: str
        """

        self._invoice_owner = invoice_owner

    @property
    def start_date(self):
        """Gets the start_date of this TimeSlicedMetricsForEvergreen.  # noqa: E501


        :return: The start_date of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this TimeSlicedMetricsForEvergreen.


        :param start_date: The start_date of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def subscription_owner(self):
        """Gets the subscription_owner of this TimeSlicedMetricsForEvergreen.  # noqa: E501

        The acount number of the billing account that owns the subscription.  # noqa: E501

        :return: The subscription_owner of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :rtype: str
        """
        return self._subscription_owner

    @subscription_owner.setter
    def subscription_owner(self, subscription_owner):
        """Sets the subscription_owner of this TimeSlicedMetricsForEvergreen.

        The acount number of the billing account that owns the subscription.  # noqa: E501

        :param subscription_owner: The subscription_owner of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :type: str
        """

        self._subscription_owner = subscription_owner

    @property
    def term_number(self):
        """Gets the term_number of this TimeSlicedMetricsForEvergreen.  # noqa: E501


        :return: The term_number of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :rtype: float
        """
        return self._term_number

    @term_number.setter
    def term_number(self, term_number):
        """Sets the term_number of this TimeSlicedMetricsForEvergreen.


        :param term_number: The term_number of this TimeSlicedMetricsForEvergreen.  # noqa: E501
        :type: float
        """

        self._term_number = term_number

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
        if issubclass(TimeSlicedMetricsForEvergreen, dict):
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
        if not isinstance(other, TimeSlicedMetricsForEvergreen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other