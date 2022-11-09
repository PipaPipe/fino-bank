# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.balance_response import BalanceResponse  # noqa: E501
from swagger_server.models.obru_error_response import OBRUErrorResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBalancesController(BaseTestCase):
    """BalancesController integration test stubs"""

    def test_get_accountsaccount_id_balances(self):
        """Test case for get_accountsaccount_id_balances

        Баланс банковского счета по идентификатору accountId
        """
        headers = [('x_fapi_auth_date', 'x_fapi_auth_date_example'),
                   ('x_fapi_customer_ip_address', 'x_fapi_customer_ip_address_example'),
                   ('x_fapi_interaction_id', 'x_fapi_interaction_id_example'),
                   ('x_customer_user_agent', 'x_customer_user_agent_example')]
        response = self.client.open(
            '/open-banking/v1.3/aisp/accounts/{accountId}/balances'.format(account_id='account_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_balances(self):
        """Test case for get_balances

        Балансы всех счетов
        """
        query_string = [('page', 0)]
        headers = [('x_fapi_auth_date', 'x_fapi_auth_date_example'),
                   ('x_fapi_customer_ip_address', 'x_fapi_customer_ip_address_example'),
                   ('x_fapi_interaction_id', 'x_fapi_interaction_id_example'),
                   ('x_customer_user_agent', 'x_customer_user_agent_example')]
        response = self.client.open(
            '/open-banking/v1.3/aisp/balances',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
