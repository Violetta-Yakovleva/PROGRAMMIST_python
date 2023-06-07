'''Задача 1. Напишите программу, генерирующую элементы арифметической прогрессии
Программа принимает от пользователя три числа :
Первый элемент прогрессии, Разность (шаг) и Количество элементов
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Напишите функцию
- Аргументы: три указанных параметра
- Возвращает: список элементов арифмитической прогрессии.
Примеры/Тесты:
Ввод: 7 2 5
Вывод: [7 9 11 13 15]
Ввод: 2 3 12
Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]'''


# a1 = int(input('Введите первое число прогрессии: ')) # может быть любым
# d = int(input('Введите шаг прогресии: ')) # может быть и положительным, и отрицательным, и = 0
# n = int(input('Введите количество элементов: ')) # не может быть <= 0

# def arithmetic_progression(a1: int, d: int, n: int) -> list:
#     result = []
#     for idx in range(n):
#         element_result = a1 + idx*d
#         result.append(element_result)
#     return result
#
# print(arithmetic_progression(7, 2, 5))
# print(arithmetic_progression(2, 3, 12))


'''(*) Усложнение. Для формирования списка внутри функции используйте Comprehension'''

# def arithmetic_progression(a1: int, d: int, n: int) -> list:
#     result = []
#     result = [a1 + idx * d for idx in range(n)]
#     return result
#
# print(arithmetic_progression(7, 2, 5))
# print(arithmetic_progression(2, 3, 12))


'''(**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку,
вам понадобится распаковка и Comprehension или map'''

# input_list = input('Введите первое число, шаг арифметической прогресси и количество элементов ЧЕРЕЗ ПРОБЕЛ: ').split()
# a1, d, n = map(int, input_list)
# def arithmetic_progression(a1: int, d: int, n: int) -> list:
#     result = []
#     result = [a1 + idx * d for idx in range(n)]
#     return result
#
# print(arithmetic_progression(a1, d, n))

