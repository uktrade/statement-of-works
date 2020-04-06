from datetime import timedelta, datetime, date
from decimal import Decimal, ROUND_UP

from docxtpl import DocxTemplate
from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

from calculations import (
    calculate_contract_duration,
    calculate_number_of_payments,
    calculate_working_days,
    calculate_contract_fee,
    calculate_retention_fee,
    calculate_base_monthly_payment,
)

TEMPLATE_FILENAME = 'sow_template.docx'
GENERATED_FILENAME = 'generated_doc.docx'


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
    contract_length = calculate_contract_duration(
        parsed_start_date, parsed_end_date
    )
    working_days = calculate_working_days(parsed_start_date, parsed_end_date)
    contract_fee = calculate_contract_fee(day_rate, working_days)
    retention_fee = calculate_retention_fee(contract_fee)
    contract_end_month = parsed_end_date.strftime('%B')
    contract_end_month_plus_one = (
        parsed_end_date + relativedelta(months=+1)
    ).strftime('%B')
    number_of_payments = calculate_number_of_payments(
        contract_length.months, contract_length.days
    )
    base_monthly_payment = calculate_base_monthly_payment(
        contract_fee, number_of_payments
    )

    payment_schedule = []

    for i in range(number_of_payments):
        payment_schedule.append(
            {
                'date': (
                    parsed_start_date + relativedelta(months=+i)
                ).strftime('%B %Y'),
                'fee': f'£{base_monthly_payment:.2f}'
                if i < number_of_payments - 1
                else f'£{base_monthly_payment + retention_fee:.2f}',
                'payment_date': (
                    parsed_start_date + relativedelta(months=+(i + 1))
                ).strftime('%B %Y'),
            }
        )

    # now run the thing
    doc = DocxTemplate(TEMPLATE_FILENAME)
    context = {
        'company_name': company_name,
        'slot_code': slot_code,
        'nominated_worker': 'Yes' if nominated_worker else 'No',
        'hiring_manager': hiring_manager,
        'team': team,
        'project_description': project_description,
        'role': role,
        'cost_code': cost_code,
        'programme_code': programme_code,
        'project_code': project_code,
        'start_date': stringified_start_date,
        'end_date': stringified_end_date,
        'outside_IR35': 'Outside' if outside_IR35 else 'Inside',
        'contract_fee': f'£{contract_fee:.2f}',
        'retention_fee': f'£{retention_fee:.2f}',
        'contract_end_month': contract_end_month,
        'contract_end_month_plus_one': contract_end_month_plus_one,
        'payment_schedule': payment_schedule,
        'modules': [
            {
                'deliverables': [
                    'wefihwofgihwofih',
                    'feroihegiohergioeghi. ergoiheg iegheg hi',
                ],
                'completion_date': '12 March 2021',
            },
            {'deliverables': ['', '', ''], 'completion_date': '12 June 2021'},
        ],
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
