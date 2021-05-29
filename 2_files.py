#"""
#Домашнее задание №2

#Работа с файлами


#1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
#2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
#3. Подсчитайте количество слов в тексте
#4. Замените точки в тексте на восклицательные знаки
#5. Сохраните результат в файл referat2.txt
#"""

def main():
#   """
# Эта функция вызывается автоматически при запуске скрипта в консоли
# В ней надо заменить pass на ваш код
#   """
  #  pass
    with open('referat.txt', 'r+', encoding='utf-8') as f:
        content = f.read()
        content_str = content.replace('\n', ' ')
        content_count = content_str.split(' ')
        words_count = 0
        for i in content_count:
            if i != '':
                words_count += 1
        content_new = content.replace('.', '!')
        referat2 = open('referat2.txt', 'w')
        referat2.write(content_new)

        print(f'Длина строки: {len(content)}, количество слов в тексте: {words_count}')
        



if __name__ == "__main__":
    main()
