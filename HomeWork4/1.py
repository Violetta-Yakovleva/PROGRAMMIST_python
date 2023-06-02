# Задача 1. Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Если таких чисел нет - выдать внятное диагностическое сообщение.
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
#
# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку
#
# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

# numbers_set1 = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
# numbers_set2 = [3, 6, 9, 12, 15, 18]

numbers_set1 = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
numbers_set2 = [3, 9, 12, 15, 18]

finish_set = []
new_finish_set = ()

for i in numbers_set1:
    if i in numbers_set2:
        finish_set.append(i)
        new_finish_set = set(finish_set)
        new_finish_set = list(new_finish_set)
        new_finish_set.sort()
print(*new_finish_set)













