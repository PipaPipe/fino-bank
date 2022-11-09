# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.obru_error import OBRUError  # noqa: F401,E501
from swagger_server import util


class OBRUErrorResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: str=None, id: str=None, message: object=None, errors: List[OBRUError]=None):  # noqa: E501
        """OBRUErrorResponse - a model defined in Swagger

        :param code: The code of this OBRUErrorResponse.  # noqa: E501
        :type code: str
        :param id: The id of this OBRUErrorResponse.  # noqa: E501
        :type id: str
        :param message: The message of this OBRUErrorResponse.  # noqa: E501
        :type message: object
        :param errors: The errors of this OBRUErrorResponse.  # noqa: E501
        :type errors: List[OBRUError]
        """
        self.swagger_types = {
            'code': str,
            'id': str,
            'message': object,
            'errors': List[OBRUError]
        }

        self.attribute_map = {
            'code': 'code',
            'id': 'id',
            'message': 'message',
            'errors': 'Errors'
        }
        self._code = code
        self._id = id
        self._message = message
        self._errors = errors

    @classmethod
    def from_dict(cls, dikt) -> 'OBRUErrorResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OBRUErrorResponse of this OBRUErrorResponse.  # noqa: E501
        :rtype: OBRUErrorResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this OBRUErrorResponse.

        Высокоуровневый текстовый код ошибки, необходимый для классификации  # noqa: E501

        :return: The code of this OBRUErrorResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this OBRUErrorResponse.

        Высокоуровневый текстовый код ошибки, необходимый для классификации  # noqa: E501

        :param code: The code of this OBRUErrorResponse.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def id(self) -> str:
        """Gets the id of this OBRUErrorResponse.

        Уникальный идентификатор ошибки, для целей аудита, в случае неизвестных / не классифицированных ошибок  # noqa: E501

        :return: The id of this OBRUErrorResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this OBRUErrorResponse.

        Уникальный идентификатор ошибки, для целей аудита, в случае неизвестных / не классифицированных ошибок  # noqa: E501

        :param id: The id of this OBRUErrorResponse.
        :type id: str
        """

        self._id = id

    @property
    def message(self) -> object:
        """Gets the message of this OBRUErrorResponse.

        Краткое сообщение об ошибке. Например, «что-то не так с предоставленными параметрами запроса»  # noqa: E501

        :return: The message of this OBRUErrorResponse.
        :rtype: object
        """
        return self._message

    @message.setter
    def message(self, message: object):
        """Sets the message of this OBRUErrorResponse.

        Краткое сообщение об ошибке. Например, «что-то не так с предоставленными параметрами запроса»  # noqa: E501

        :param message: The message of this OBRUErrorResponse.
        :type message: object
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def errors(self) -> List[OBRUError]:
        """Gets the errors of this OBRUErrorResponse.


        :return: The errors of this OBRUErrorResponse.
        :rtype: List[OBRUError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List[OBRUError]):
        """Sets the errors of this OBRUErrorResponse.


        :param errors: The errors of this OBRUErrorResponse.
        :type errors: List[OBRUError]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors