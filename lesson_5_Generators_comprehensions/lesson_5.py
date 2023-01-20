# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово
# yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...


# def odd_nums(max_value):
#     n = 1
#     while n != max_value:
#         yield n
#         n += 2
#
# odd_to_15 = odd_nums(15)
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))
# print(next(odd_to_15))



# 2. *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое слово yield.
# max_value = 3
# odd_nums_gen = (n for n in range(1, max_value + 1, 2))
# print(next(odd_nums_gen))
# print(next(odd_nums_gen))
#

# 3. Есть два списка:
# tutors = [
# 'Иван', 'Анастасия', 'Петр', 'Сергей',
# 'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
# '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>),
# например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
# списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние
# кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.

# tutors = [
# 'Иван', 'Анастасия', 'Петр', 'Сергей',
# 'Дмитрий', 'Борис', 'Елена'
# ]
#
# klasses = [
# '9А', '7В', '9Б', '9В', '8Б', '10А'
# ]
#
# gen = ((tutor, klasse) for tutor, klasse in zip(tutors, klasses))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# from itertools import zip_longest
#
# gen = ((tutor, klasse) for tutor, klasse in zip_longest(tutors, klasses))
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше
# предыдущего, например:
# © geekbrains.ru 13
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
#
# result_list = [num for i, num in enumerate(src) if num > src[i - 1] and i != 0]
#
# print(enumerate(src))
# print(result_list)

# Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно
# сделать оптимизацию кода по памяти, по скорости.
# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result_list = [num for num in src if src.count(num) == 1]

print(result_list)