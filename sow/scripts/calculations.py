from decimal import Decimal, ROUND_UP
from datetime import date

from dateutil.relativedelta import relativedelta
from workalendar.europe import UnitedKingdom

cal = UnitedKingdom()


def calculate_contract_length(parsed_start, parsed_end):
    return relativedelta(parsed_end, parsed_start)


def calculate_number_of_payments(number_of_months, number_of_days):
    if number_of_days > 0:
        return number_of_months + 1
    return number_of_months


def calculate_working_days(parsed_start, parsed_end):
    return cal.get_working_days_delta(
        # need to move start date back one day as the
        # get_working_day_delta calculation doesn't include the first day.
        # A simple +1 wouldn't work if the first day is a holiday.
        parsed_start + relativedelta(days=-1),
        parsed_end,
    )


def calculate_contract_fee(day_rate, working_days):
    return Decimal(day_rate * working_days).quantize(
        Decimal('0.01'), rounding=ROUND_UP
    )


def calculate_retention_fee(contract_fee):
    retention_fee_percentage = Decimal(0.05)

    return Decimal(contract_fee * retention_fee_percentage).quantize(
        Decimal('0.01'), rounding=ROUND_UP
    )


def calculate_base_monthly_payment(contract_fee, number_of_payments):
    return Decimal(
        (contract_fee / number_of_payments) * Decimal(0.95)
    ).quantize(Decimal('0.01'), rounding=ROUND_UP)


def calculate_last_payment(base_monthly_payment, retention_fee):
    return base_monthly_payment + retention_fee
