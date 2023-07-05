from datetime import date, datetime


def date_para_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')

def str_para_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

def float_para_RS(valor: float) -> str:
    return f'R$ {valor:,.2f}'
