
#Домашнее задание №2

#Работа csv

#1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
#   В списке нужно создать не менее 4-х словарей
#2. Запишите содержимое списка словарей в файл в формате csv

#"""

def main():
 #   """
  #  Эта функция вызывается автоматически при запуске скрипта в консоли
   # В ней надо заменить pass на ваш код
    #"""
    #pass
    import csv

    job_list = [
        {'name': 'Вася', 'age': '25', 'job': 'Водитель'},
        {'name': 'Петя', 'age': '35', 'job': 'Повар'},
        {'name': 'Алина', 'age': '20', 'job': 'Директор'},
        {'name': 'Сергей', 'age': '19', 'job': 'Курьер'},
        {'name': 'Володя', 'age': '65', 'job': 'Президент'},
        {'name': 'Дима', 'age': '50', 'job': 'Пенсионер'},
    ]
    
    with open('job_list.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        job = csv.DictWriter(f, fields, delimiter=';')
        job.writeheader()
        for i in job_list:
            job.writerow(i)


if __name__ == "__main__":
    main()
