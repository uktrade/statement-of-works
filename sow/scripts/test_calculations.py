from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from decimal import Decimal

from sow.scripts.calculations import (
    calculate_contract_duration,
    calculate_number_of_payments,
    calculate_working_days,
    calculate_contract_fee,
    calculate_retention_fee,
    calculate_base_monthly_payment,
)


def test_calculate_contract_duration():
    assert calculate_contract_duration(
        parse('2020-01-01'), parse('2020-03-31')
    ) == relativedelta(months=+2, days=+30)


def test_calculate_number_of_payments():
    assert calculate_number_of_payments(3, 0) == 3
    assert calculate_number_of_payments(3, 3) == 4


def test_calculate_working_days():
    assert (
        calculate_working_days(parse('2020-01-01'), parse('2020-03-31')) == 64
    )


def test_calculate_contract_fee():
    assert calculate_contract_fee(525, 32) == 16800
    assert calculate_contract_fee(511.37, 32) == Decimal('16363.85')


def test_calculate_retention_fee():
    assert calculate_retention_fee(2578) == Decimal('128.91')


def test_calculate_base_monthly_payment():
    assert calculate_base_monthly_payment(2578, 5) == Decimal('489.82')
