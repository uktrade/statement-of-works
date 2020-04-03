from docxtpl import DocxTemplate
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse
from decimal import Decimal, ROUND_UP

TEMPLATE_FILENAME = 'sow_template.docx'
GENERATED_FILENAME = 'generated_doc.docx'


def calculate_contract_length(parsed_start, parsed_end):
    return relativedelta(parsed_end, parsed_start)


def calculate_number_of_payments(number_of_months, number_of_days):
    if number_of_days > 0:
        return number_of_months + 1
    return number_of_months


def calculate_prorata_for_last_payment(number_of_days):
    average_days_in_a_month = 30
    return number_of_days / average_days_in_a_month


def calculate_contract_fee(
    day_rate, number_of_months, prorata_for_last_payment
):
    paid_working_days_in_month = 20
    # work out the number of working days between the start and end date
    # also need to add an option to remove working days for leave

    if prorata_for_last_payment > 0:
        return Decimal(
            day_rate
            * paid_working_days_in_month
            * (number_of_months + prorata_for_last_payment)
        ).quantize(Decimal('0.01'), rounding=ROUND_UP)
    return Decimal(
        day_rate * paid_working_days_in_month * number_of_months
    ).quantize(Decimal('0.01'), rounding=ROUND_UP)


def calculate_retention_fee(contract_fee):
    retention_fee_percentage = Decimal(0.05)

    return Decimal(contract_fee * retention_fee_percentage).quantize(
        Decimal('0.01'), rounding=ROUND_UP
    )


def calculate_base_monthly_payment(contract_fee, number_of_payments):
    return Decimal((contract_fee / number_of_payments) * 0.95).quantize(
        Decimal('0.01'), rounding=ROUND_UP
    )


def calculate_last_payment(base_monthly_payment, retention_fee):
    return base_monthly_payment + retention_fee


def month_to_string(parsed_date):
    return (parsed_date).strftime('%B')


def generate_statement_of_works(
    company_name,
    slot_code,
    nominated_worker,
    hiring_manager,
    team,
    project_description,
    role,
    cost_code,
    programme_code,
    project_code,
    start_date,
    end_date,
    outside_IR35,
    day_rate,
):
    # prep the variables
    parsed_start_date = parse(start_date)
    parsed_end_date = parse(end_date)
    stringified_start_date = parsed_start_date.strftime('%-d %B %Y')
    stringified_end_date = parsed_end_date.strftime('%-d %B %Y')
    contract_length = calculate_contract_length(
        parsed_start_date, parsed_end_date
    )
    contract_fee = calculate_contract_fee(
        day_rate,
        contract_length.months,
        calculate_prorata_for_last_payment(contract_length.days),
    )
    retention_fee = calculate_retention_fee(contract_fee)
    contract_end_month = month_to_string(parsed_end_date)
    contract_end_month_plus_one = month_to_string(
        parsed_end_date + relativedelta(months=+1)
    )

    # now run the thing
    doc = DocxTemplate(TEMPLATE_FILENAME)
    context = {
        'company_name': company_name,
        'slot_code': slot_code,
        'nominated_worker': nominated_worker,
        # make boolean
        'hiring_manager': hiring_manager,
        'team': team,
        'project_description': project_description,
        'role': role,
        'cost_code': cost_code,
        'programme_code': programme_code,
        'project_code': project_code,
        'start_date': stringified_start_date,
        'end_date': stringified_end_date,
        'outside_IR35': outside_IR35,
        # make boolean
        'contract_fee': f'£{contract_fee:.2f}',
        'retention_fee': f'£{retention_fee:.2f}',
        'contract_end_month': contract_end_month,
        'contract_end_month_plus_one': contract_end_month_plus_one,
    }
    doc.render(context)
    doc.save(GENERATED_FILENAME)


generate_statement_of_works(
    '123 Inc',
    '1234',
    'No',
    'Christopher Sunkel',
    'Data Hub',
    'blah',
    'Developer',
    '4321',
    '9876',
    '89472',
    '2018-09-12',
    '2019-03-31',
    'Outside',
    525,
)
