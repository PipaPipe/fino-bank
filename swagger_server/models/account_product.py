# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.brand import Brand  # noqa: F401,E501
from swagger_server.models.other_fees_charges import OtherFeesCharges  # noqa: F401,E501
from swagger_server.models.payment_cards4 import PaymentCards4  # noqa: F401,E501
from swagger_server.models.product_details import ProductDetails  # noqa: F401,E501
from swagger_server.models.product_type import ProductType  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class AccountProduct(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, account_id: str=None, product_id: str=None, product_name: str=None, product_type: ProductType=None, product_version: str=None, brand: Brand=None, product_details: ProductDetails=None, fees_charges: List[OtherFeesCharges]=None, supplementary_data: PaymentCards4=None):  # noqa: E501
        """AccountProduct - a model defined in Swagger

        :param account_id: The account_id of this AccountProduct.  # noqa: E501
        :type account_id: str
        :param product_id: The product_id of this AccountProduct.  # noqa: E501
        :type product_id: str
        :param product_name: The product_name of this AccountProduct.  # noqa: E501
        :type product_name: str
        :param product_type: The product_type of this AccountProduct.  # noqa: E501
        :type product_type: ProductType
        :param product_version: The product_version of this AccountProduct.  # noqa: E501
        :type product_version: str
        :param brand: The brand of this AccountProduct.  # noqa: E501
        :type brand: Brand
        :param product_details: The product_details of this AccountProduct.  # noqa: E501
        :type product_details: ProductDetails
        :param fees_charges: The fees_charges of this AccountProduct.  # noqa: E501
        :type fees_charges: List[OtherFeesCharges]
        :param supplementary_data: The supplementary_data of this AccountProduct.  # noqa: E501
        :type supplementary_data: PaymentCards4
        """
        self.swagger_types = {
            'account_id': str,
            'product_id': str,
            'product_name': str,
            'product_type': ProductType,
            'product_version': str,
            'brand': Brand,
            'product_details': ProductDetails,
            'fees_charges': List[OtherFeesCharges],
            'supplementary_data': PaymentCards4
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'product_id': 'productId',
            'product_name': 'productName',
            'product_type': 'productType',
            'product_version': 'productVersion',
            'brand': 'Brand',
            'product_details': 'ProductDetails',
            'fees_charges': 'FeesCharges',
            'supplementary_data': 'SupplementaryData'
        }
        self._account_id = account_id
        self._product_id = product_id
        self._product_name = product_name
        self._product_type = product_type
        self._product_version = product_version
        self._brand = brand
        self._product_details = product_details
        self._fees_charges = fees_charges
        self._supplementary_data = supplementary_data

    @classmethod
    def from_dict(cls, dikt) -> 'AccountProduct':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AccountProduct of this AccountProduct.  # noqa: E501
        :rtype: AccountProduct
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_id(self) -> str:
        """Gets the account_id of this AccountProduct.

        ???????????????????? ?? ???????????????????? ??????????????????????????, ???????????????????????? ?????? ?????????????????????????? ?????????????? ??????????  # noqa: E501

        :return: The account_id of this AccountProduct.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this AccountProduct.

        ???????????????????? ?? ???????????????????? ??????????????????????????, ???????????????????????? ?????? ?????????????????????????? ?????????????? ??????????  # noqa: E501

        :param account_id: The account_id of this AccountProduct.
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def product_id(self) -> str:
        """Gets the product_id of this AccountProduct.

        ???????????????????? ??????????????????????????, ?????????????????????? ???????????????????? ?????????????????????? ???????????? ???????????????? ?????????????? ???? ????????????????????  ??????????????????  # noqa: E501

        :return: The product_id of this AccountProduct.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id: str):
        """Sets the product_id of this AccountProduct.

        ???????????????????? ??????????????????????????, ?????????????????????? ???????????????????? ?????????????????????? ???????????? ???????????????? ?????????????? ???? ????????????????????  ??????????????????  # noqa: E501

        :param product_id: The product_id of this AccountProduct.
        :type product_id: str
        """

        self._product_id = product_id

    @property
    def product_name(self) -> str:
        """Gets the product_name of this AccountProduct.

        ???????????????? ????????????????, ?????????????????????????? ?? ?????????????????????????? ??????????  # noqa: E501

        :return: The product_name of this AccountProduct.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name: str):
        """Sets the product_name of this AccountProduct.

        ???????????????? ????????????????, ?????????????????????????? ?? ?????????????????????????? ??????????  # noqa: E501

        :param product_name: The product_name of this AccountProduct.
        :type product_name: str
        """
        if product_name is None:
            raise ValueError("Invalid value for `product_name`, must not be `None`")  # noqa: E501

        self._product_name = product_name

    @property
    def product_type(self) -> ProductType:
        """Gets the product_type of this AccountProduct.


        :return: The product_type of this AccountProduct.
        :rtype: ProductType
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type: ProductType):
        """Sets the product_type of this AccountProduct.


        :param product_type: The product_type of this AccountProduct.
        :type product_type: ProductType
        """
        if product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

    @property
    def product_version(self) -> str:
        """Gets the product_version of this AccountProduct.

        ???????????? ????????????????  # noqa: E501

        :return: The product_version of this AccountProduct.
        :rtype: str
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version: str):
        """Sets the product_version of this AccountProduct.

        ???????????? ????????????????  # noqa: E501

        :param product_version: The product_version of this AccountProduct.
        :type product_version: str
        """

        self._product_version = product_version

    @property
    def brand(self) -> Brand:
        """Gets the brand of this AccountProduct.


        :return: The brand of this AccountProduct.
        :rtype: Brand
        """
        return self._brand

    @brand.setter
    def brand(self, brand: Brand):
        """Sets the brand of this AccountProduct.


        :param brand: The brand of this AccountProduct.
        :type brand: Brand
        """

        self._brand = brand

    @property
    def product_details(self) -> ProductDetails:
        """Gets the product_details of this AccountProduct.


        :return: The product_details of this AccountProduct.
        :rtype: ProductDetails
        """
        return self._product_details

    @product_details.setter
    def product_details(self, product_details: ProductDetails):
        """Sets the product_details of this AccountProduct.


        :param product_details: The product_details of this AccountProduct.
        :type product_details: ProductDetails
        """

        self._product_details = product_details

    @property
    def fees_charges(self) -> List[OtherFeesCharges]:
        """Gets the fees_charges of this AccountProduct.

        ???????????????????? ?? ?????????????????? ?? ????????????, ?? ?????? ?????????? ???? ???????????? ????????????????????????  # noqa: E501

        :return: The fees_charges of this AccountProduct.
        :rtype: List[OtherFeesCharges]
        """
        return self._fees_charges

    @fees_charges.setter
    def fees_charges(self, fees_charges: List[OtherFeesCharges]):
        """Sets the fees_charges of this AccountProduct.

        ???????????????????? ?? ?????????????????? ?? ????????????, ?? ?????? ?????????? ???? ???????????? ????????????????????????  # noqa: E501

        :param fees_charges: The fees_charges of this AccountProduct.
        :type fees_charges: List[OtherFeesCharges]
        """

        self._fees_charges = fees_charges

    @property
    def supplementary_data(self) -> PaymentCards4:
        """Gets the supplementary_data of this AccountProduct.


        :return: The supplementary_data of this AccountProduct.
        :rtype: PaymentCards4
        """
        return self._supplementary_data

    @supplementary_data.setter
    def supplementary_data(self, supplementary_data: PaymentCards4):
        """Sets the supplementary_data of this AccountProduct.


        :param supplementary_data: The supplementary_data of this AccountProduct.
        :type supplementary_data: PaymentCards4
        """

        self._supplementary_data = supplementary_data
