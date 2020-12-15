from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from decimal import Decimal

import pytest

from sow.scripts.calculations import (
    calculate_contract_duration,
    calculate_number_of_payments,
    calculate_working_days,
    calculate_contract_fee,
    calculate_retention_fee,
    calculate_base_monthly_payment,
)


def test_calculate_contract_duration():
    """
    Test the calculation of the delta between start and end date.
    """
    assert calculate_contract_duration(
        parse('2020-01-01'), parse('2020-03-31')
    ) == relativedelta(months=+2, days=+30)


@pytest.mark.parametrize("a, b, expected", [(3, 0, 3), (3, 3, 4)])
def test_calculate_number_of_payments(a, b, expected):
    """
    Test number of payments. If there are days that
    don't add up to a whole month,
    an extra payment should be added.
    """
    assert calculate_number_of_payments(a, b) == expected


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (parse('2020-01-01'), parse('2020-03-31'), 3, 59),
        (parse('2020-01-01'), parse('2020-06-30'), 6, 115),
        (parse('2020-01-01'), parse('2020-05-31'), 5, 94),
    ],
)
def test_calculate_working_days(a, b, c, expected):
    """
    Test the calculation of working days. It should move the start date back
    by one because the working days calculation doesn't
    include the first day by default.
    """
    assert calculate_working_days(a, b, c) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(525, 32, 16800), (511.37, 32, Decimal('16363.85'))]
)
def test_calculate_contract_fee(a, b, expected):
    """
    Test calculation of contract fee. It should give it to 2
    decimal places if necessary.
    """
    assert calculate_contract_fee(a, b) == expected


def test_calculate_retention_fee():
    """
    Test the calculation of the rentention fee. It should give it to 2
    decimal places if necessary.
    """
    assert calculate_retention_fee(2578) == Decimal('128.91')


def test_calculate_base_monthly_payment():
    """
    Test the calculation of the base monthly payment. It should give
    it to 2 decimal places if necessary.
    """
    assert calculate_base_monthly_payment(2578, 5) == Decimal('489.82')
