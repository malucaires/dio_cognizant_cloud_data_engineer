'''Utiliza biblioteca datetime para retornar data e time atual e armazenar time'''

from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A %B %Y')
    print(data_atual)
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)

trabalhando_com_date()
trabalhando_com_time()
trabalhando_com_datetime()

print('Final do programa!')
