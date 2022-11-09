# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Brand(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, brand_name: str=None, application_uri: str=None):  # noqa: E501
        """Brand - a model defined in Swagger

        :param brand_name: The brand_name of this Brand.  # noqa: E501
        :type brand_name: str
        :param application_uri: The application_uri of this Brand.  # noqa: E501
        :type application_uri: str
        """
        self.swagger_types = {
            'brand_name': str,
            'application_uri': str
        }

        self.attribute_map = {
            'brand_name': 'brandName',
            'application_uri': 'applicationUri'
        }
        self._brand_name = brand_name
        self._application_uri = application_uri

    @classmethod
    def from_dict(cls, dikt) -> 'Brand':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Brand of this Brand.  # noqa: E501
        :rtype: Brand
        """
        return util.deserialize_model(dikt, cls)

    @property
    def brand_name(self) -> str:
        """Gets the brand_name of this Brand.

        Наименование собственного брэнда продукта или брэнд организации, который используется для продвижения продукта  # noqa: E501

        :return: The brand_name of this Brand.
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name: str):
        """Sets the brand_name of this Brand.

        Наименование собственного брэнда продукта или брэнд организации, который используется для продвижения продукта  # noqa: E501

        :param brand_name: The brand_name of this Brand.
        :type brand_name: str
        """
        if brand_name is None:
            raise ValueError("Invalid value for `brand_name`, must not be `None`")  # noqa: E501

        self._brand_name = brand_name

    @property
    def application_uri(self) -> str:
        """Gets the application_uri of this Brand.

        URL-адрес для получения информации об условиях приобретения продукта  # noqa: E501

        :return: The application_uri of this Brand.
        :rtype: str
        """
        return self._application_uri

    @application_uri.setter
    def application_uri(self, application_uri: str):
        """Sets the application_uri of this Brand.

        URL-адрес для получения информации об условиях приобретения продукта  # noqa: E501

        :param application_uri: The application_uri of this Brand.
        :type application_uri: str
        """
        if application_uri is None:
            raise ValueError("Invalid value for `application_uri`, must not be `None`")  # noqa: E501

        self._application_uri = application_uri
