# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.active_currency_and_amount_simple_type import ActiveCurrencyAndAmountSimpleType  # noqa: F401,E501
from swagger_server.models.active_or_historic_currency_code import ActiveOrHistoricCurrencyCode  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class ActiveOrHistoricCurrencyAndAmount(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, amount: ActiveCurrencyAndAmountSimpleType=None, currency: ActiveOrHistoricCurrencyCode=None):  # noqa: E501
        """ActiveOrHistoricCurrencyAndAmount - a model defined in Swagger

        :param amount: The amount of this ActiveOrHistoricCurrencyAndAmount.  # noqa: E501
        :type amount: ActiveCurrencyAndAmountSimpleType
        :param currency: The currency of this ActiveOrHistoricCurrencyAndAmount.  # noqa: E501
        :type currency: ActiveOrHistoricCurrencyCode
        """
        self.swagger_types = {
            'amount': ActiveCurrencyAndAmountSimpleType,
            'currency': ActiveOrHistoricCurrencyCode
        }

        self.attribute_map = {
            'amount': 'amount',
            'currency': 'currency'
        }
        self._amount = amount
        self._currency = currency

    @classmethod
    def from_dict(cls, dikt) -> 'ActiveOrHistoricCurrencyAndAmount':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ActiveOrHistoricCurrencyAndAmount of this ActiveOrHistoricCurrencyAndAmount.  # noqa: E501
        :rtype: ActiveOrHistoricCurrencyAndAmount
        """
        return util.deserialize_model(dikt, cls)

    @property
    def amount(self) -> ActiveCurrencyAndAmountSimpleType:
        """Gets the amount of this ActiveOrHistoricCurrencyAndAmount.


        :return: The amount of this ActiveOrHistoricCurrencyAndAmount.
        :rtype: ActiveCurrencyAndAmountSimpleType
        """
        return self._amount

    @amount.setter
    def amount(self, amount: ActiveCurrencyAndAmountSimpleType):
        """Sets the amount of this ActiveOrHistoricCurrencyAndAmount.


        :param amount: The amount of this ActiveOrHistoricCurrencyAndAmount.
        :type amount: ActiveCurrencyAndAmountSimpleType
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self) -> ActiveOrHistoricCurrencyCode:
        """Gets the currency of this ActiveOrHistoricCurrencyAndAmount.


        :return: The currency of this ActiveOrHistoricCurrencyAndAmount.
        :rtype: ActiveOrHistoricCurrencyCode
        """
        return self._currency

    @currency.setter
    def currency(self, currency: ActiveOrHistoricCurrencyCode):
        """Sets the currency of this ActiveOrHistoricCurrencyAndAmount.


        :param currency: The currency of this ActiveOrHistoricCurrencyAndAmount.
        :type currency: ActiveOrHistoricCurrencyCode
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency
