import datetime
import random, string

from swagger_server.models import Account, AccountStatus, AccountType, DataAccountResponse, AccountResponse, \
    CashAccount, PartyIdentification, CreditDebitCode, DataBalanceResponse, BalanceResponse, Balance, \
    ActiveOrHistoricCurrencyAndAmount, ActiveOrHistoricCurrencyCode, BranchAndFinancialInstitutionIdentification, \
    FinancialInstitutionIdentificationCode


def gen_id(start=100000, stop=199999):
    return random.randint(start, stop)


def get_status():
    return random.choice([AccountStatus.DELETED, AccountStatus.DISABLED, AccountStatus.ENABLED])


def get_type():
    return random.choice([AccountType.BUSINESS, AccountType.PERSONAL])


def get_account_description(start=12):
    letters = string.ascii_uppercase
    return ''.join([random.choice(letters) for _ in range(start)])



def get_scheme_name():
    return random.choice([FinancialInstitutionIdentificationCode.BIC,
                          FinancialInstitutionIdentificationCode.BICFI])



def get_account_details():
    cash_accounts_list = []
    for _ in range(3):
        cash_account = CashAccount()
        cash_account._name = get_account_description(20)
        cash_account._scheme_name = get_scheme_name()
        cash_account._identification = gen_id()
        cash_accounts_list.append(cash_account)
    return cash_accounts_list


def get_birthday():
    day = random.randint(1, 31)
    if day < 10:
        day = '0' + str(day)
    month = random.randint(1, 12)
    if month < 10:
        month = '0' + str(month)
    year = random.randint(1970, 2022)
    if (int(datetime.datetime.now().year) - year < 18):
        return None

    return '.'.join([str(day), str(month), str(year)])


def get_owner():
    names = ["Mike", "John", 'Bob', 'ilya', 'max', 'kirill', 'grigoriy']
    countries = ['RU', 'EU', 'CH', 'UK']
    party_id = PartyIdentification()
    party_id._name = random.choice(names)
    party_id._mobile_number = ''.join([random.choice(string.digits) for _ in range(11)])
    party_id._country_of_residence = random.choice(countries)
    party_id._birth_date = get_birthday()
    party_id._identification = gen_id()
    return party_id


def get_servicer():
    pass


def gen_accounts(num_accounts=10):
    DataAcResp = DataAccountResponse()
    DataAcResp.account = []

    ar = AccountResponse()

    for n in range(num_accounts):
        acc = Account()
        acc.account_id = n + 1
        acc.status = get_status()
        acc.account_type = get_type()
        acc.account_details = get_account_details()
        acc.owner = get_owner()
        DataAcResp.account.append(acc)

    ar.data = DataAcResp
    return ar


def gen_amount():
    return round(random.uniform(0, 100000), 2)


def get_credit_debit_code():
    return random.choice([CreditDebitCode.DEBIT, CreditDebitCode.CREDIT])


def get_currency():
    return random.choice(['RUB', 'USD', 'EUR'])


def get_amount():
    amount = ActiveOrHistoricCurrencyAndAmount()
    amount._amount = gen_amount()
    amount._currency = get_currency()
    return amount


def gen_balances(num_balances=10):
    DataBalResp = DataBalanceResponse()
    DataBalResp.balance = []

    ba = BalanceResponse()

    for n in range(num_balances):
        bal = Balance()
        bal.account_id = n+1
        bal.amount = get_amount()
        bal.credit_debit_indicator = get_credit_debit_code()
        DataBalResp.balance.append(bal)

    ba.data = DataBalResp
    return ba


def get_account_id(in_id):
    DataAcResp = DataAccountResponse()
    DataAcResp.account = []

    ar = AccountResponse()

    for i in list_accounts.data.account:
        print(i.account_id)
        if str(i.account_id) == (in_id):
            DataAcResp.account.append(i)
            ar.data = DataAcResp
            return ar


def get_balance_id(in_id):
    DataBalResp = DataBalanceResponse()
    DataBalResp.balance = []

    ba = BalanceResponse()

    for i in list_balance.data.balance:
        if str(i.account_id) == (in_id):
            DataBalResp.balance.append(i)
            ba.data = DataBalResp
            return ba


list_balance = gen_balances()
list_accounts = gen_accounts()

# acc.servicer = get_servicer()
