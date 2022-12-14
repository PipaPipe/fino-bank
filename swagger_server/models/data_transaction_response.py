# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.transaction import Transaction  # noqa: F401,E501
from swagger_server import util


class DataTransactionResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, transaction: List[Transaction]=None):  # noqa: E501
        """DataTransactionResponse - a model defined in Swagger

        :param transaction: The transaction of this DataTransactionResponse.  # noqa: E501
        :type transaction: List[Transaction]
        """
        self.swagger_types = {
            'transaction': List[Transaction]
        }

        self.attribute_map = {
            'transaction': 'Transaction'
        }
        self._transaction = transaction

    @classmethod
    def from_dict(cls, dikt) -> 'DataTransactionResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DataTransactionResponse of this DataTransactionResponse.  # noqa: E501
        :rtype: DataTransactionResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transaction(self) -> List[Transaction]:
        """Gets the transaction of this DataTransactionResponse.

        Список операций по счету  # noqa: E501

        :return: The transaction of this DataTransactionResponse.
        :rtype: List[Transaction]
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction: List[Transaction]):
        """Sets the transaction of this DataTransactionResponse.

        Список операций по счету  # noqa: E501

        :param transaction: The transaction of this DataTransactionResponse.
        :type transaction: List[Transaction]
        """

        self._transaction = transaction
