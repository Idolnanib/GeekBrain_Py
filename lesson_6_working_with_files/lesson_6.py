f_obj = open('my_file.txt')
print(f_obj)

print(f_obj.read())
txt = f_obj.close()
print(f_obj.closed)








# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов
# web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>,
# <requested_resource>). Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]

# with open('nginx_logs.txt') as f:
#     data = []
#     for line in f:
#         splited = line.split()
#         data.append(splited[0], splited[5].replace('"', ''), splited[6])
# print(data)

# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов; код должен работать
# даже с файлами, размер которых превышает объем ОЗУ компьютера.

# with open('nginx_logs.txt') as f:
#     data = []
#     spam_dict = {}
#     for line in f:
#         splitted = line.split()
#         data.append(splitted[0], splitted[5].replace('"', ''), splitted[6])
#         spam_dict.setdefault(splitted[0], 0)
#         spam_dict[splitted[0]] += 1
#
# spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
# print(spam_dict[:5])
# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
# и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
# в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
# записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
# скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
# меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# © geekbrains.ru 16
# горные лыжи

# from itertools import zip_longest
# import json
#
# out_dict = {}
#
# with open ('users.csv', encoding='utf-8') as users:
#     with open('hobby.csv', encoding='utf-8') as hobby:
#         num_lines_users = sum(1 for line in users)
#         num_lines_hobby = sum(1 for line in hobby)
#
#         if num_lines_users < num_lines_hobby:
#             exit(1)
#
#         users.seek(0)
#         hobby.seek(0)
#
#         for line_user, line_user_hobby in zip_longest(users, hobby):
#             out_dict[line_user.strip()] = line_user_hobby.strip() if \
#                 line_user_hobby is not None else line_user_hobby
#
# with open('task3.json', 'w', encoding='utf-8') as f:
#     json.jump(out_dict, f, ensure_ascii=False)
# print(out_dict)

# 4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
# ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
# будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
# сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

# from itertools import zip_longest
#
#
# with open ('task.txt', 'w', encoding='utf-8') as f:
#     with open('users.csv', encoding='utf-8') as users:
#         with open('hobby.csv', encoding='utf-8') as hobby:
#             num_lines_users = sum(1 for line in users)
#             num_lines_hobby = sum(1 for line in hobby)
#
#         if num_lines_users < num_lines_hobby:
#             exit(1)
#
#         users.seek(0)
#         hobby.seek(0)
#
#         for line_user, line_user_hobby in zip_longest(users, hobby):
#             f.write(f'{line_user.strip()}: '
#                     f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')


# 5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
# задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
import sys
from itertools import zip_longest
users, hobby, out = sys.argv[1:]

with open (out, 'w', encoding='utf-8') as f:
    with open('users.csv', encoding='utf-8') as users:
        with open('hobby.csv', encoding='utf-8') as hobby:
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for line in hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)

        users.seek(0)
        hobby.seek(0)

        for line_user, line_user_hobby in zip_longest(users, hobby):
            f.write(f'{line_user.strip()}: '
                    f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')


# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два
# скрипта с интерфейсом командной строки: для записи данных и для вывода на экран
# записанных данных. При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# ● просто запуск скрипта — выводить все записи;
# ● запуск скрипта с одним параметром-числом — выводить все записи с номера, равного
# этому числу, до конца;
# ● запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
# первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
# Примеры запуска скриптов:
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# © geekbrains.ru 17
# 7879,1

import sys

nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    if len(nums) > 1:
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    elif len(nums) == 0:
        start_idx = 0
        end_idx = sum(1 for line in f)
        f.seek(0)
    else:
        start_idx = int(nums[0])
        end_idx = sum(1 for line in f)
        f.seek(0)

    for idx, line in enumerate(f):
        if start_idx <= idx + 1 <= end_idx:
            print(line.strip())

# 7. *(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
# передаём ему номер записи и новое значение. При этом файл не должен читаться целиком —
# обязательное требование. Предусмотреть ситуацию, когда пользователь вводит номер записи,
# которой не существует.
# Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.