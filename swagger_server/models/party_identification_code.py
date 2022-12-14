# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PartyIdentificationCode(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    TXID = "RU.CBR.TXID"
    LEI = "RU.CBR.LEI"
    PASP = "RU.CBR.PASP"
    CLID = "RU.CBR.CLID"
    QRST = "RU.CBR.QRST"
    TAXT = "RU.CBR.TAXT"
    OGRN = "RU.CBR.OGRN"
    SNILS = "RU.CBR.SNILS"
    PAN = "RU.CBR.PAN"
    MTEL = "RU.CBR.MTEL"
    def __init__(self):  # noqa: E501
        """PartyIdentificationCode - a model defined in Swagger

        """
        self.swagger_types = {
        }

        self.attribute_map = {
        }

    @classmethod
    def from_dict(cls, dikt) -> 'PartyIdentificationCode':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PartyIdentificationCode of this PartyIdentificationCode.  # noqa: E501
        :rtype: PartyIdentificationCode
        """
        return util.deserialize_model(dikt, cls)
