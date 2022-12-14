# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account_product import AccountProduct  # noqa: F401,E501
from swagger_server import util


class AccountProductResponseData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, product: AccountProduct=None):  # noqa: E501
        """AccountProductResponseData - a model defined in Swagger

        :param product: The product of this AccountProductResponseData.  # noqa: E501
        :type product: AccountProduct
        """
        self.swagger_types = {
            'product': AccountProduct
        }

        self.attribute_map = {
            'product': 'Product'
        }
        self._product = product

    @classmethod
    def from_dict(cls, dikt) -> 'AccountProductResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccountProductResponse_Data of this AccountProductResponseData.  # noqa: E501
        :rtype: AccountProductResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def product(self) -> AccountProduct:
        """Gets the product of this AccountProductResponseData.


        :return: The product of this AccountProductResponseData.
        :rtype: AccountProduct
        """
        return self._product

    @product.setter
    def product(self, product: AccountProduct):
        """Sets the product of this AccountProductResponseData.


        :param product: The product of this AccountProductResponseData.
        :type product: AccountProduct
        """

        self._product = product
