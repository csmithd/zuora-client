# coding: utf-8




import pprint
import re  # noqa: F401

import six


class PutInvoiceType(object):
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
        'auto_pay': 'bool',
        'due_date': 'date',
        'transferred_to_accounting': 'str'
    }

    attribute_map = {
        'auto_pay': 'autoPay',
        'due_date': 'dueDate',
        'transferred_to_accounting': 'transferredToAccounting'
    }

    def __init__(self, auto_pay=None, due_date=None, transferred_to_accounting=None):  # noqa: E501
        """PutInvoiceType - a model defined in Swagger"""  # noqa: E501

        self._auto_pay = None
        self._due_date = None
        self._transferred_to_accounting = None
        self.discriminator = None

        if auto_pay is not None:
            self.auto_pay = auto_pay
        if due_date is not None:
            self.due_date = due_date
        if transferred_to_accounting is not None:
            self.transferred_to_accounting = transferred_to_accounting

    @property
    def auto_pay(self):
        """Gets the auto_pay of this PutInvoiceType.  # noqa: E501

        Whether invoices are automatically picked up for processing in the corresponding payment run.   By default, invoices are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :return: The auto_pay of this PutInvoiceType.  # noqa: E501
        :rtype: bool
        """
        return self._auto_pay

    @auto_pay.setter
    def auto_pay(self, auto_pay):
        """Sets the auto_pay of this PutInvoiceType.

        Whether invoices are automatically picked up for processing in the corresponding payment run.   By default, invoices are automatically picked up for processing in the corresponding payment run.   # noqa: E501

        :param auto_pay: The auto_pay of this PutInvoiceType.  # noqa: E501
        :type: bool
        """

        self._auto_pay = auto_pay

    @property
    def due_date(self):
        """Gets the due_date of this PutInvoiceType.  # noqa: E501

        The date by which the payment for this invoice is due.    # noqa: E501

        :return: The due_date of this PutInvoiceType.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this PutInvoiceType.

        The date by which the payment for this invoice is due.    # noqa: E501

        :param due_date: The due_date of this PutInvoiceType.  # noqa: E501
        :type: date
        """

        self._due_date = due_date

    @property
    def transferred_to_accounting(self):
        """Gets the transferred_to_accounting of this PutInvoiceType.  # noqa: E501

        Whether the invoice was transferred to an external accounting system.   # noqa: E501

        :return: The transferred_to_accounting of this PutInvoiceType.  # noqa: E501
        :rtype: str
        """
        return self._transferred_to_accounting

    @transferred_to_accounting.setter
    def transferred_to_accounting(self, transferred_to_accounting):
        """Sets the transferred_to_accounting of this PutInvoiceType.

        Whether the invoice was transferred to an external accounting system.   # noqa: E501

        :param transferred_to_accounting: The transferred_to_accounting of this PutInvoiceType.  # noqa: E501
        :type: str
        """
        allowed_values = ["Processing", "Yes", "Error", "Ignore"]  # noqa: E501
        if transferred_to_accounting not in allowed_values:
            raise ValueError(
                "Invalid value for `transferred_to_accounting` ({0}), must be one of {1}"  # noqa: E501
                .format(transferred_to_accounting, allowed_values)
            )

        self._transferred_to_accounting = transferred_to_accounting

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
        if issubclass(PutInvoiceType, dict):
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
        if not isinstance(other, PutInvoiceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other