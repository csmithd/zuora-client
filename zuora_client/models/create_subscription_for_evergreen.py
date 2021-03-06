# coding: utf-8




import pprint
import re  # noqa: F401

import six

from zuora_client.models.create_subscription_new_subscription_owner_account import CreateSubscriptionNewSubscriptionOwnerAccount  # noqa: F401,E501
from zuora_client.models.create_subscription_terms import CreateSubscriptionTerms  # noqa: F401,E501
from zuora_client.models.rate_plan_override_for_evergreen import RatePlanOverrideForEvergreen  # noqa: F401,E501


class CreateSubscriptionForEvergreen(object):
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
        'invoice_separately': 'bool',
        'new_subscription_owner_account': 'CreateSubscriptionNewSubscriptionOwnerAccount',
        'notes': 'str',
        'subscribe_to_rate_plans': 'list[RatePlanOverrideForEvergreen]',
        'subscription_number': 'str',
        'subscription_owner_account_number': 'str',
        'terms': 'CreateSubscriptionTerms'
    }

    attribute_map = {
        'invoice_separately': 'invoiceSeparately',
        'new_subscription_owner_account': 'newSubscriptionOwnerAccount',
        'notes': 'notes',
        'subscribe_to_rate_plans': 'subscribeToRatePlans',
        'subscription_number': 'subscriptionNumber',
        'subscription_owner_account_number': 'subscriptionOwnerAccountNumber',
        'terms': 'terms'
    }

    def __init__(self, invoice_separately=None, new_subscription_owner_account=None, notes=None, subscribe_to_rate_plans=None, subscription_number=None, subscription_owner_account_number=None, terms=None):  # noqa: E501
        """CreateSubscriptionForEvergreen - a model defined in Swagger"""  # noqa: E501

        self._invoice_separately = None
        self._new_subscription_owner_account = None
        self._notes = None
        self._subscribe_to_rate_plans = None
        self._subscription_number = None
        self._subscription_owner_account_number = None
        self._terms = None
        self.discriminator = None

        if invoice_separately is not None:
            self.invoice_separately = invoice_separately
        if new_subscription_owner_account is not None:
            self.new_subscription_owner_account = new_subscription_owner_account
        if notes is not None:
            self.notes = notes
        if subscribe_to_rate_plans is not None:
            self.subscribe_to_rate_plans = subscribe_to_rate_plans
        if subscription_number is not None:
            self.subscription_number = subscription_number
        if subscription_owner_account_number is not None:
            self.subscription_owner_account_number = subscription_owner_account_number
        if terms is not None:
            self.terms = terms

    @property
    def invoice_separately(self):
        """Gets the invoice_separately of this CreateSubscriptionForEvergreen.  # noqa: E501

        Specifies whether the subscription appears on a separate invoice when Zuora generates invoices.   # noqa: E501

        :return: The invoice_separately of this CreateSubscriptionForEvergreen.  # noqa: E501
        :rtype: bool
        """
        return self._invoice_separately

    @invoice_separately.setter
    def invoice_separately(self, invoice_separately):
        """Sets the invoice_separately of this CreateSubscriptionForEvergreen.

        Specifies whether the subscription appears on a separate invoice when Zuora generates invoices.   # noqa: E501

        :param invoice_separately: The invoice_separately of this CreateSubscriptionForEvergreen.  # noqa: E501
        :type: bool
        """

        self._invoice_separately = invoice_separately

    @property
    def new_subscription_owner_account(self):
        """Gets the new_subscription_owner_account of this CreateSubscriptionForEvergreen.  # noqa: E501


        :return: The new_subscription_owner_account of this CreateSubscriptionForEvergreen.  # noqa: E501
        :rtype: CreateSubscriptionNewSubscriptionOwnerAccount
        """
        return self._new_subscription_owner_account

    @new_subscription_owner_account.setter
    def new_subscription_owner_account(self, new_subscription_owner_account):
        """Sets the new_subscription_owner_account of this CreateSubscriptionForEvergreen.


        :param new_subscription_owner_account: The new_subscription_owner_account of this CreateSubscriptionForEvergreen.  # noqa: E501
        :type: CreateSubscriptionNewSubscriptionOwnerAccount
        """

        self._new_subscription_owner_account = new_subscription_owner_account

    @property
    def notes(self):
        """Gets the notes of this CreateSubscriptionForEvergreen.  # noqa: E501

        Notes about the subscription. These notes are only visible to Zuora users.   # noqa: E501

        :return: The notes of this CreateSubscriptionForEvergreen.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CreateSubscriptionForEvergreen.

        Notes about the subscription. These notes are only visible to Zuora users.   # noqa: E501

        :param notes: The notes of this CreateSubscriptionForEvergreen.  # noqa: E501
        :type: str
        """
        if notes is not None and len(notes) > 500:
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `500`")  # noqa: E501

        self._notes = notes

    @property
    def subscribe_to_rate_plans(self):
        """Gets the subscribe_to_rate_plans of this CreateSubscriptionForEvergreen.  # noqa: E501

        List of rate plans associated with the subscription.   # noqa: E501

        :return: The subscribe_to_rate_plans of this CreateSubscriptionForEvergreen.  # noqa: E501
        :rtype: list[RatePlanOverrideForEvergreen]
        """
        return self._subscribe_to_rate_plans

    @subscribe_to_rate_plans.setter
    def subscribe_to_rate_plans(self, subscribe_to_rate_plans):
        """Sets the subscribe_to_rate_plans of this CreateSubscriptionForEvergreen.

        List of rate plans associated with the subscription.   # noqa: E501

        :param subscribe_to_rate_plans: The subscribe_to_rate_plans of this CreateSubscriptionForEvergreen.  # noqa: E501
        :type: list[RatePlanOverrideForEvergreen]
        """

        self._subscribe_to_rate_plans = subscribe_to_rate_plans

    @property
    def subscription_number(self):
        """Gets the subscription_number of this CreateSubscriptionForEvergreen.  # noqa: E501

        Subscription number of the subscription. For example, A-S00000001.  If you do not set this field, Zuora will generate the subscription number.   # noqa: E501

        :return: The subscription_number of this CreateSubscriptionForEvergreen.  # noqa: E501
        :rtype: str
        """
        return self._subscription_number

    @subscription_number.setter
    def subscription_number(self, subscription_number):
        """Sets the subscription_number of this CreateSubscriptionForEvergreen.

        Subscription number of the subscription. For example, A-S00000001.  If you do not set this field, Zuora will generate the subscription number.   # noqa: E501

        :param subscription_number: The subscription_number of this CreateSubscriptionForEvergreen.  # noqa: E501
        :type: str
        """
        if subscription_number is not None and len(subscription_number) > 100:
            raise ValueError("Invalid value for `subscription_number`, length must be less than or equal to `100`")  # noqa: E501

        self._subscription_number = subscription_number

    @property
    def subscription_owner_account_number(self):
        """Gets the subscription_owner_account_number of this CreateSubscriptionForEvergreen.  # noqa: E501

        Account number of an existing account that will own the subscription. For example, A00000001.  If you do not set this field or the `newSubscriptionOwnerAccount` field, the account that owns the order will also own the subscription. Zuora will return an error if you set this field and the `newSubscriptionOwnerAccount` field.   # noqa: E501

        :return: The subscription_owner_account_number of this CreateSubscriptionForEvergreen.  # noqa: E501
        :rtype: str
        """
        return self._subscription_owner_account_number

    @subscription_owner_account_number.setter
    def subscription_owner_account_number(self, subscription_owner_account_number):
        """Sets the subscription_owner_account_number of this CreateSubscriptionForEvergreen.

        Account number of an existing account that will own the subscription. For example, A00000001.  If you do not set this field or the `newSubscriptionOwnerAccount` field, the account that owns the order will also own the subscription. Zuora will return an error if you set this field and the `newSubscriptionOwnerAccount` field.   # noqa: E501

        :param subscription_owner_account_number: The subscription_owner_account_number of this CreateSubscriptionForEvergreen.  # noqa: E501
        :type: str
        """
        if subscription_owner_account_number is not None and len(subscription_owner_account_number) > 70:
            raise ValueError("Invalid value for `subscription_owner_account_number`, length must be less than or equal to `70`")  # noqa: E501

        self._subscription_owner_account_number = subscription_owner_account_number

    @property
    def terms(self):
        """Gets the terms of this CreateSubscriptionForEvergreen.  # noqa: E501


        :return: The terms of this CreateSubscriptionForEvergreen.  # noqa: E501
        :rtype: CreateSubscriptionTerms
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """Sets the terms of this CreateSubscriptionForEvergreen.


        :param terms: The terms of this CreateSubscriptionForEvergreen.  # noqa: E501
        :type: CreateSubscriptionTerms
        """

        self._terms = terms

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
        if issubclass(CreateSubscriptionForEvergreen, dict):
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
        if not isinstance(other, CreateSubscriptionForEvergreen):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
