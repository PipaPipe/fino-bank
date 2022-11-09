import random, string


from swagger_server.models import Account, AccountStatus, AccountType, DataAccountResponse, AccountResponse, \
    CashAccount, PartyIdentification


def gen_id(start=100000, stop=199999):
    return random.randint(start, stop)


def get_status():
    return random.choice([AccountStatus.DELETED, AccountStatus.DISABLED, AccountStatus.ENABLED])


def get_type():
    return random.choice([AccountType.BUSINESS, AccountType.PERSONAL])


def get_account_description(start=12):
    letters = string.ascii_uppercase
    return ''.join([random.choice(letters) for _ in range(start)])



def get_account_details():
    cash_accounts_list = []
    for _ in range(3):
        cash_account = CashAccount()
        cash_account._name = get_account_description(20)
        cash_account._scheme_name = get_account_description(10)
        cash_account._identification = gen_id()
        cash_accounts_list.append(cash_account)
    return cash_accounts_list


def get_owner():
    names = ["Mike", "John", 'Bob', 'ilya', 'max', 'kirill', 'grigoriy']
    countries = ['RU', 'EU', 'CH', 'UK']
    party_id = PartyIdentification()
    party_id._name = random.choice(names)
    party_id._mobile_number = ''.join([random.choice(string.digits) for _ in range(11)])
    party_id._country_of_residence = random.choice(countries)
    party_id._birth_date = 2002
    party_id._identification = gen_id()
    return party_id


def get_servicer():
    pass


def gen_accounts(num_accounts=5):
    DataAcResp = DataAccountResponse()
    DataAcResp.account = []

    ar = AccountResponse()

    for _ in range(num_accounts):
        acc = Account()
        acc.account_id = gen_id()
        acc.status = get_status()
        acc.account_type = get_type()
        acc.account_details = get_account_details()
        acc.owner = get_owner()
        DataAcResp.account.append(acc)

    ar.data = DataAcResp
    return ar




#acc.servicer = get_servicer()






