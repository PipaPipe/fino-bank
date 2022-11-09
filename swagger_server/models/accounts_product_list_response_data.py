# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account_product import AccountProduct  # noqa: F401,E501
from swagger_server import util


class AccountsProductListResponseData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, products: List[AccountProduct]=None):  # noqa: E501
        """AccountsProductListResponseData - a model defined in Swagger

        :param products: The products of this AccountsProductListResponseData.  # noqa: E501
        :type products: List[AccountProduct]
        """
        self.swagger_types = {
            'products': List[AccountProduct]
        }

        self.attribute_map = {
            'products': 'Products'
        }
        self._products = products

    @classmethod
    def from_dict(cls, dikt) -> 'AccountsProductListResponseData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccountsProductListResponse_Data of this AccountsProductListResponseData.  # noqa: E501
        :rtype: AccountsProductListResponseData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def products(self) -> List[AccountProduct]:
        """Gets the products of this AccountsProductListResponseData.

        Информация о продуктах по счетам Пользователя  # noqa: E501

        :return: The products of this AccountsProductListResponseData.
        :rtype: List[AccountProduct]
        """
        return self._products

    @products.setter
    def products(self, products: List[AccountProduct]):
        """Sets the products of this AccountsProductListResponseData.

        Информация о продуктах по счетам Пользователя  # noqa: E501

        :param products: The products of this AccountsProductListResponseData.
        :type products: List[AccountProduct]
        """

        self._products = products