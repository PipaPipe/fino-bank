# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.account_product_response import AccountProductResponse  # noqa: E501
from swagger_server.models.accounts_product_list_response import AccountsProductListResponse  # noqa: E501
from swagger_server.models.obru_error_response import OBRUErrorResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_get_account_account_id_product(self):
        """Test case for get_account_account_id_product

        Информация о финансовом продукте по идентификатору счета
        """
        query_string = [('page', 0)]
        headers = [('x_fapi_auth_date', 'x_fapi_auth_date_example'),
                   ('x_fapi_customer_ip_address', 'x_fapi_customer_ip_address_example'),
                   ('x_fapi_interaction_id', 'x_fapi_interaction_id_example'),
                   ('x_customer_user_agent', 'x_customer_user_agent_example')]
        response = self.client.open(
            '/open-banking/v1.3/aisp/accounts/{accountId}/product'.format(account_id='account_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_accounts_product_list(self):
        """Test case for get_accounts_product_list

        Список приобретенных финансовых продуктов
        """
        query_string = [('page', 0)]
        headers = [('x_fapi_auth_date', 'x_fapi_auth_date_example'),
                   ('x_fapi_customer_ip_address', 'x_fapi_customer_ip_address_example'),
                   ('x_fapi_interaction_id', 'x_fapi_interaction_id_example'),
                   ('x_customer_user_agent', 'x_customer_user_agent_example')]
        response = self.client.open(
            '/open-banking/v1.3/aisp/products',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
