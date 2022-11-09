import connexion
import six

from swagger_server.models.balance_response import BalanceResponse  # noqa: E501
from swagger_server.models.obru_error_response import OBRUErrorResponse  # noqa: E501
from swagger_server import util


def get_accountsaccount_id_balances(account_id, x_fapi_auth_date=None, x_fapi_customer_ip_address=None, x_fapi_interaction_id=None, x_customer_user_agent=None):  # noqa: E501
    """Баланс банковского счета по идентификатору accountId

    Конечная точка позволяет СПИУ получать информацию об остатке на счете с идентификатором accountId # noqa: E501

    :param account_id: Идентификатор счета
    :type account_id: str
    :param x_fapi_auth_date: Время последнего входа Пользователя в систему с TPP. Значение предоставляется в виде HTTP-date, как в разделе 7.1.1.1 [RFC7231]. Например, x-fapi-auth-date: Mon, 26 Aug 2019 12:23:11 GMT
    :type x_fapi_auth_date: str
    :param x_fapi_customer_ip_address: IP-адрес Пользователя, если Пользователь в данный момент подключен к Стороннему Поставщику (залогинен в приложении Стороннего Поставщика).
    :type x_fapi_customer_ip_address: str
    :param x_fapi_interaction_id: RFC4122 UID, используемый в качестве идентификатора корреляции. Если необходимо, то ППИУ передает обратно значение идентификатора корреляции в заголовке ответа x-fapi-interaction-id.
    :type x_fapi_interaction_id: str
    :param x_customer_user_agent: В заголовке указывается тип устройства (user-agent), который использует Пользователь. Сторонний Поставщик может заполнить это поле значением типа устройства (user-agent), указанным Пользователем. Если Пользователь использует мобильное приложение Стороннего Поставщика, Сторонний Поставщик проверяет, что строка типа устройства (user-agent) отличается от строки типа устройства (user-agent) на основе браузера.
    :type x_customer_user_agent: str

    :rtype: BalanceResponse
    """
    return 'do some magic!'


def get_balances(page=None, x_fapi_auth_date=None, x_fapi_customer_ip_address=None, x_fapi_interaction_id=None, x_customer_user_agent=None):  # noqa: E501
    """Балансы всех счетов

    Конечная точка позволяет СПИУ получать остаток по всем счетам, которые были авторизованы Пользователем для доступа с помощью согласия # noqa: E501

    :param page: Номер страницы
    :type page: int
    :param x_fapi_auth_date: Время последнего входа Пользователя в систему с TPP. Значение предоставляется в виде HTTP-date, как в разделе 7.1.1.1 [RFC7231]. Например, x-fapi-auth-date: Mon, 26 Aug 2019 12:23:11 GMT
    :type x_fapi_auth_date: str
    :param x_fapi_customer_ip_address: IP-адрес Пользователя, если Пользователь в данный момент подключен к Стороннему Поставщику (залогинен в приложении Стороннего Поставщика).
    :type x_fapi_customer_ip_address: str
    :param x_fapi_interaction_id: RFC4122 UID, используемый в качестве идентификатора корреляции. Если необходимо, то ППИУ передает обратно значение идентификатора корреляции в заголовке ответа x-fapi-interaction-id.
    :type x_fapi_interaction_id: str
    :param x_customer_user_agent: В заголовке указывается тип устройства (user-agent), который использует Пользователь. Сторонний Поставщик может заполнить это поле значением типа устройства (user-agent), указанным Пользователем. Если Пользователь использует мобильное приложение Стороннего Поставщика, Сторонний Поставщик проверяет, что строка типа устройства (user-agent) отличается от строки типа устройства (user-agent) на основе браузера.
    :type x_customer_user_agent: str

    :rtype: BalanceResponse
    """
    return 'do some magic!'
