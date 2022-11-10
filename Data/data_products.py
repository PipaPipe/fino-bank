import enum
import random
import string

from swagger_server.models import AccountsProductListResponseData, AccountsProductListResponse, AccountProduct, Brand, \
    ProductDetails, PeriodUnit


class ProductNames(enum.Enum):
    DEPOSITINDIVIDUAL_ = "depositIndividual | Депозит физического лица"
    DEPOSITLEGALENTITY_ = "depositlegalEntity | Депозит юридического лица"
    CAINDIVIDUAL_ = "CAindividual | Текущий счет физического лица"
    CALEGALENTITY_ = "CALegalEntity | Расчетный счет юридического лица"
    DEBITCARD_ = "debitCard | Дебетовая карта"
    CREDITCARD_ = "creditCard | Кредитная карта"
    LOANCAR_ = "loanCar | Автокредит"
    LOANINDIVIDUAL_ = "loanIndividual | Кредит физическому лицу"
    LOANLEGALENTITY_ = "loanLegalEntity | Кредит юридического лица"
    MORTAGE_ = "mortage | Ипотека"
    INVESTMENT_ = "investment | Инвестиционный продукт"
    OTHER_ = "Other | Другой продукт"


class BrandNames(enum.Enum):
    PROMOBOT = 'Промобот'
    SIMPL = 'Симпл'
    TINKOFF = 'Тинькофф'
    SBER = 'Сбербанк'
    ALPHA = 'Альфа банк'
    INNOTEH = 'Иннотех'


class ProductVersions(enum.Enum):
    ALPHA = 'Альфа версия'
    BETA = 'Бета версия'


class ProductUnitEnum(enum.Enum):
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    QUARTER = "Quarter"
    HALFYEAR = "HalfYear"
    YEAR = "Year"
    ACADEMICTERM = "AcademicTerm"


def get_product_version():
    return random.choice(list(ProductVersions))


def gen_product_id():
    return ''.join([random.choice(string.digits) for _ in range(20)])


def get_product_name():
    return random.choice(list(ProductNames))


def get_product_brand():
    brand = Brand()
    brand.brand_name = random.choice(list(BrandNames))
    brand.application_uri = 'None'
    return brand


def get_product_details():
    details = ProductDetails()
    details.active = random.choice([True, False])
    details.fee_free_length = 0
    details.fee_free_length_period = random.choice(list(ProductUnitEnum))
    details.comments = ''
    return details

def gen_products(num_products=10):
    DataProdResp = AccountsProductListResponseData()
    DataProdResp.products = []
    pr = AccountsProductListResponse()
    for n in range(num_products):
        prod = AccountProduct()
        prod.account_id = n+1
        prod.product_id = gen_product_id()
        prod.product_name = get_product_name()
        prod.product_type = prod.product_name
        prod.product_version = get_product_version()
        prod.brand = get_product_brand()
        prod.product_details = get_product_details()
        prod.fees_charges = None
        prod.supplementary_data = None
        DataProdResp.products.append(prod)
    pr.data = DataProdResp
    return pr


def get_product_id(in_id):
    DataProdResp = AccountsProductListResponseData()
    DataProdResp.products = []

    pr = AccountsProductListResponse()

    for i in list_products.data.products:
        if str(i.account_id) == in_id:
            DataProdResp.products.append(i)
            pr.data = DataProdResp
            return pr

list_products = gen_products()
