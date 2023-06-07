'''Задача 2. Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
Напишите функцию
- Аргументы: список чисел и границы диапазона
- Возвращает: список индексов элементов (смотри условие)

Примеры/Тесты:
lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
<function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
<function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
<function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]'''


# def elements_in_my_range(lst1: list, min_lst: int, max_lst: int) -> list:
#     result = []
#     for idx in range(len(lst1)):
#         if min_lst <= lst1[idx] <= max_lst:
#             result.append(idx)
#     return result

# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# print(elements_in_my_range(lst1, 2, 10))
# print(elements_in_my_range(lst1, 2, 9))
# print(elements_in_my_range(lst1, 0, 6))


'''(*) Усложнение. Для формирования списка внутри функции используйте Comprehension'''

# def elements_in_my_range(lst1: list, min_lst: int, max_lst: int) -> list:
#     result = []
#     result = [idx for idx in range(len(lst1)) if min_lst <= lst1[idx] <= max_lst]
#     return result
#
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# print(elements_in_my_range(lst1, 2, 10))
# print(elements_in_my_range(lst1, 2, 9))
# print(elements_in_my_range(lst1, 0, 6))


'''(*) Усложнение. Функция возвращает список кортежей вида: индекс, значение
Примеры/Тесты:
lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
<function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]'''

# def elements_in_my_range(lst1: list, min_lst: int, max_lst: int) -> tuple:
#     result = ()
#     result = [(idx, lst1[idx]) for idx in range(len(lst1)) if min_lst <= lst1[idx] <= max_lst]
#     return result
#
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# print(elements_in_my_range(lst1, 2, 10))
