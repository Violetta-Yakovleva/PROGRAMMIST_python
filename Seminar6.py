'''Задача 1. Даны два списка чисел. Требуется вывести те элементы первого списка , которых нет во втором списке.
Создайте функцию.
Аргументы: два списка целых чисел
Возвращает: список элементов (смотри условие)
Примеры/Тесты:
<function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]
<function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]
[*] Усложнение. Элементы необходимо возвращать в том порядке, в котором они находятся в первом списке, с учетом повторений
Примеры/Тесты:
<function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]
<function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]'''

# def defference_list(list1: list, list2: list) -> list:
#     set_list2 = set(list2)
#     new_list = []
#     for item in list1:
#         if item not in set_list2:
#             new_list.append(item)
#     return new_list
#
# print(defference_list([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))
# print(defference_list([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]))

# from time import perf_counter
# from random import randint
#
# def difference_set(list1: list, list2: list) -> list:
#     t1 = perf_counter()
#     set_list2 = set(list2)
#     res = [item for item in list1 if item not in set_list2]
#     t2 = perf_counter()
#     return t2 - t1
#
# def difference_list(list1: list, list2: list) -> list:
#     t1 = perf_counter()
#     res = [item for item in list1 if item not in list2]
#     t2 = perf_counter()
#     return t2 - t1
#
# n = 10000
# lst1 = [randint(0, n) for i in range(n)]
# lst2 = [randint(0, n) for i in range(n)]
#
# print(f" SET: {difference_set(lst1, lst2):3e}")
# print(f"LIST: {difference_list(lst1, lst2):3e}")



'''Задача 2. Дан список, целых чисел.
Напишите функцию, которая определит те элементы списка, у которых два соседних и, при этом, оба соседних элемента меньше данного.
Функция
Аргументы: список целых чисел
Возвращает: список элементов (смотри условие)
Примеры/Тесты:
<function_name>([1, 3, 3, 3, 5]) -> [5]
<function_name>([1, 5, 1, 6, 1]) -> [5,6]
<function_name>([7, 5, 1, 6, 8]) -> [8]
<function_name>([8, 1, 5, 4, 5]) -> [8,5]'''

# def neibours (list1: list) -> list:
#     result_list = list()
#     for idx in range(len(list1)-1):
#         if list1[idx-1]<list1[idx]>list1[idx+1]:
#             result_list.append(list1[idx])
#     idx =  len(list1)-1
#     if list1[idx-1]<list1[idx] and list1[0]<list1[idx]:
#             result_list.append(list1[idx])
#     return result_list
#
# print(neibours([1, 3, 3, 3, 5]))
# print(neibours([1, 5, 1, 6, 1]))
# print(neibours([7, 5, 1, 6, 8]))
# print(neibours([8, 1, 5, 4, 5]))

'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
Напишите функцию
Аргументы: список целых чисел
Возвращает: кол-во пар
Примеры/Тесты:
<function_name>([1, 2, 3, 2, 3]) -> 2
<function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6'''

# list1 = [1, 2, 3, 2, 3]
# list2 = [1, 2, 3, 2, 3, 3, 2, 4]
#
# # def count_pairs(lst1:list):
# #     result=0
# #     for idx in range(len(lst1)):
# #         for idx2 in range(idx+1,len(lst1)):
# #             if lst1[idx]==lst1[idx2]:
# #                 result+=1
# #     return result
#
# def count_pairs(lst1:list):
#     result=0
#     for idx in range(len(lst1)):
#         result+=lst1[idx+1:].count(lst1[idx])
#     return result
#
# totalResult1 = count_pairs(list1)
# totalResult2 = count_pairs(list2)
# print(totalResult1)
# print(totalResult2)


'''Задача 4. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
Например, 220 и 284 – дружественные числа.
220: 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, — их сумма равна 284.
284: 1, 2, 4, 71 и 142, — их сумма равна 220.
Первые пары дружественных чисел:
220, 284; 1184, 1210; 2620, 2924; 5020, 5564; 6232, 6368
Для заданного числа number выведите все пары дружественных чисел, каждое из которых не превосходит number.
Напишите функцию:
Аргументы: целое число
Печатает все пары дружественных чисел, не превосходящих аргумент.
Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
Примечание:
1. Выделите значимые куски алгоритма и оформите их в виде функций
2. Задокументируйте созданные функции
3. Используйте type hinting
Примеры/Тесты:
<function_name>(300)
220 284
<function_name>(10000)
220 284
1184 1210
2620 2924
5020 5564
6232 6368'''

def delitel(number: int)-> int:
    sum_del = 0
    for el in range(1, number):
        if number % el == 0:
            sum_del += el
    return sum_del

def frendly(number: int) -> None:
    for el in range(number + 1):
        second_number = delitel(el)
        if el < second_number and el == delitel(second_number):
            print(el, second_number)

frendly(10000)