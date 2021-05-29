
from datetime import date, datetime, timedelta
from time import strftime

def print_days():
    dt = date.today()
    delta = timedelta(days=1)
    dt_yesterday = dt - delta
    dt_30days = dt - 30*delta
    print(f'Вчера было {dt_yesterday}, сегодня - {dt}, а 30 дней назад было {dt_30days}')


def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    
if __name__ == "__main__":
    print_days()
    print(str_2_datetime('01/01/20 12:10:03.234567'))