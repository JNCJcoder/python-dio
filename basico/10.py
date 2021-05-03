from datetime import date, time, datetime

def trabalhando_com_date():
    data_atual = date.today().strftime('%d/%m/%Y')
    print(data_atual)

def trabalhando_com_time():
    horario = time(hour = 15, minute = 18, second = 30)
    print(horario.strftime('%H:%M:%S'))

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M'))
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])

if __name__ == '__main__':
    trabalhando_com_datetime()