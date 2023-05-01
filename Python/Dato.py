import datetime

def date():
    n=int(input('Skriv antal dage: '))
    current= datetime.datetime.now()
    next_n= datetime.datetime.today() + datetime.timedelta(days=n)
    print(f'Datoen i dag: {current}')
    print(f'Datoen {n} dage fra i dag: {next_n}')
date()

