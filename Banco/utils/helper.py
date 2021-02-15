from datetime import date, datetime

def date_str(data: date) -> str:
    return data.strftime('%d/%m/%Y')

def str_date(data: str) -> date:
    return datetime.strptime(data, '%d/%m/%Y')

def formatar_moeda(valor: float) -> str:
    return f'R$ {valor:,.2f}'

