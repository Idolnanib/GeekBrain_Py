# my_list = [1, 'jopa', 76, 'when', 87]
#
# print(my_list[::-1])
#
# print(dir(my_list))
#
#
# for num in reversed(my_list):
#     print(num)

# Задача. Написать программу, определяющую, что число
# трёхзначное и средняя цифра равна 5.

# number = int(input('Введи трехзначное число, а среднюю цифру напиши 5, чтобы по задаче подходило ахах/'
#                    'я то думал надо среднее значение вычислять...мда '))
# if number > 999 or number < 100:
#     print('Число не трехзначное facepalm')
# else:
#     if number // 100 > 0:
#         spare = number // 100 * 100
#         number = number - spare
#         print('количество сотен в числе равно ', spare // 100)
#
#     if number // 10 > 0:
#         spare = number // 10 * 10
#         number = number - spare
#         print('Десятки в числе равны ', spare // 10)
#         print('Количество единиц', number)

# 1. Реализовать вывод информации о промежутке времени в зависимости /
# от его продолжительности duration в секундах: до минуты: <s> сек; до часа:/
# <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
# Примеры:
#
# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек


# duration = int(input('Введи количество секунд всего: '))
#
# minute = 0
# hour = 0
# day = 0
# second = 0
#
# if duration // 86400 > 0:
#     day = duration // 86400
#     duration = duration - day * 86400
#     if duration // 3600 > 0:
#         hour = duration // 3600
#         duration = duration - hour * 3600
#         if duration // 60 > 0:
#             minute = duration // 60
#             duration = duration - minute * 60
#             second = duration
#             print('day = ', day)
#             print('hour = ', hour)
#             print('minute = ', minute)
#             print('second = ', second)
#         else:
#             second = duration
#             print('day = ', day)
#             print('hour = ', hour)
#             print('minute = ', minute)
#             print('second = ', second)
#     else:
#         if duration // 60 > 0:
#             minute = duration // 60
#             duration = duration - minute * 60
#             second = duration
#             print('day = ', day)
#             print('hour = ', hour)
#             print('minute = ', minute)
#             print('second = ', second)
#         else:
#             second = duration
#             print('day = ', day)
#             print('hour = ', hour)
#             print('minute = ', minute)
#             print('second = ', second)
#
#
# elif duration // 3600 > 0:
#     hour = duration // 3600
#     duration = duration - hour * 3600
#     if duration // 60 > 0:
#         minute = duration // 60
#         duration = duration - minute * 60
#         second = duration
#         print('hour = ', hour)
#         print('minute = ', minute)
#         print('second = ', second)
#     else:
#         second = duration
#         print('hour = ', hour)
#         print('minute = ', minute)
#         print('second = ', second)
# elif duration // 60 > 0:
#     minute = duration // 60
#     duration = duration - minute * 60
#     second = duration
#     print('minute = ', minute)
#     print('second = ', second)
# else:
#     second = duration
#     print('second = ', second)

# import datetime
# duration= 10000000
# time_format = str(datetime.timedelta(seconds = duration))
# print("Time in preferred format :-",time_format)




# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

# list_of_numbers = []
# sum_in_list_of_dismemberments = 0
# sum_in_list_of_numbers = 0
#
# for num in range(1, 1001):
#     if num % 2 > 0:
#         list_of_numbers.append(num ** 3)
#
# for num in list_of_numbers:
#     list_of_dismemberments = [int(n_num) for n_num in str(num)]
#     for n_num in list_of_dismemberments:
#         sum_in_list_of_dismemberments = sum_in_list_of_dismemberments + n_num
#     if sum_in_list_of_dismemberments % 7 == 0:
#         sum_in_list_of_numbers = sum_in_list_of_numbers + num
#
# print(sum_in_list_of_numbers)
#
# for num in range(1, 1001):
#     if num % 2 > 0:
#         list_of_numbers.append(num ** 3 + 17)
#
# for num in list_of_numbers:
#     list_of_dismemberments = [int(n_num) for n_num in str(num)]
#     for n_num in list_of_dismemberments:
#         sum_in_list_of_dismemberments = sum_in_list_of_dismemberments + n_num
#     if sum_in_list_of_dismemberments % 7 == 0:
#         sum_in_list_of_numbers = sum_in_list_of_numbers + num
#
# print(sum_in_list_of_numbers)


#
# for num in range(1, 1001):
#     if num % 2 > 0:
#         list_of_numbers.append(num ** 3 )
#
# for num in list_of_numbers:
#     for i in range(0, len(str(num))):
#         sum_in_list_of_dismemberments = sum_in_list_of_dismemberments + i
#     if sum_in_list_of_dismemberments % 7 == 0:
#         sum_in_list_of_numbers = sum_in_list_of_numbers + num
#
# print(sum_in_list_of_numbers)

# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

# user_input = 0
# while user_input != 1:
#
#     num = int(input('введи число для процента: '))
#
#     list_of_numbers = []
#
#     list_of_numbers = [int(n_num) for n_num in str(num)]
#
#     print(list_of_numbers)
#
#     if list_of_numbers[-1] == 1:
#         print(num, 'процент')
#     if list_of_numbers[-1] == 0:
#         print(num, 'процентов')
#     if list_of_numbers[-1] == 2:
#         print(num, 'процента')
#     if list_of_numbers[-1] == 3:
#         print(num, 'процента')
#     if list_of_numbers[-1] == 4:
#         print(num, 'процента')
#     if list_of_numbers[-1] == 5:
#         print(num, 'процентов')
#     if list_of_numbers[-1] == 6:
#         print(num, 'процентов')
#     if list_of_numbers[-1] == 7:
#         print(num, 'процентов')
#     if list_of_numbers[-1] == 8:
#         print(num, 'процентов')
#     if list_of_numbers[-1] == 9:
#         print(num, 'процентов')
#
#     user_input = int(input('1 - Выход. Все остальное продолжить ...'))

# Практическое задание
# 1. Выяснить тип результата выражений:
# ● 15 * 3
# ● 15 / 3
# ● 15 // 2
# ● 15 ** 2

# print(type(15 * 3))
# print(type(15 / 3))
# print(type(15 // 2))
# print(type(15 ** 2))

# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
# 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем)
# кавычками (добавить кавычку до и кавычку после элемента списка, являющегося числом) и
# дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут',
# 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как
# модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его
# реализации позже. Главное: дополнить числа до двух разрядов нулём!
#
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# new_list = []
#
# for elem in my_list:
#     if elem.isdigit():
#         new_list.extend(['"', f'{int(elem):02}', '"'])
#     elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
#         new_list.extend(['"',f'{elem[0]}{int(elem):02}', '"'])
#     else:
#         new_list.append(elem)
#
# out_info = ' '.join(new_list)
# print(out_info)
# 3. *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача
# намного серьёзнее, чем может сначала показаться.
# my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
#
#
# for elem in my_list:
#     if elem.isdigit():
#         my_list.extend(['"', f'{int(elem):02}', '"'])
#     elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
#         my_list.extend(['"',f'{elem[0]}{int(elem):02}', '"'])
#     else:
#         my_list.append(elem)
#     if elem == 'градусов':
#         break
#
#
# print(my_list)
# for elem in my_list:
#     while elem != 'градусов':
#         my_list.pop(0)
#         break
# out_info = ' '.join(my_list)
# print(out_info)
# print(my_list)
# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
# 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на
# экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов
# списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?
bad_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for elem in bad_list:
    print('Привет ',elem.split()[-1].title())


# 5. Создать вручную список, содержащий цены на товары (10–20 товаров), например:
# © geekbrains.ru 19
# [57.8, 46.51, 97, ...]
# A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде
# <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
# как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп
# или 00 коп).
# B. Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что
# объект списка после сортировки остался тот же).
# C. Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# D. Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по
# возрастанию, написав минимум кода?

# goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.05, 50.98, 9077, 1]
# for good in goods:
#     rub = int(good)
#     kk = (good - int(good)) * 100
#     print(f'{rub} руб {kk:02.0f} коп', end=', ')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой
#
#
#
# goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.5, 50.98, 9077, 1]
# print(id(goods))
# print(goods)
# goods.sort()
# print(id(goods))
# print(goods)
# for good in goods:
#     rub = int(good)
#     kk = (good - int(good)) * 100
#     print(f'{rub} руб {kk:02.0f} коп')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой
#
#
# goods = [57.8, 46.51, 97, 10, 20.14, 30.18, 40.5, 50.98, 9077, 1, 23.7]
# for good in sorted(goods)[::-1][:5]:
#     rub = int(good)
#     kk = (good - int(good)) * 100
#     print(f'{rub} руб {kk:02.0f} коп')  # 02 - добавить поле нулей 2шт,  .0f - округление 0 знаков после запятой
#
# # one line
# print([f'{int(good)} руб {(good - int(good)) * 100:02.0f} коп' for good in sorted(goods)[::-1][:5]])