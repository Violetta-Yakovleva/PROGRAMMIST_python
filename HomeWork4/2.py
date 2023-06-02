# Задача 2. В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста
# и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их
# с клавиатуры, можно задать непосредственно в коде программы
# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7
#
# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

# bushes = int(input("Введите количество кустов: "))
# number_berries = []

# for i in range(bushes):
#     number_berries.append(int(input(f'Введите количество ягод на {i+1} кусте: ')))
# print(number_berries)

bushes = 8
num_berries = [11, 92, 1, 42, 15, 12, 11, 81]

for i in range(len(num_berries)-1):
    max_sum = 0
    bush = 0

    if i == 0:
        berries_sum = num_berries[i] + num_berries[i+1] + num_berries[len(num_berries)-1]
        if berries_sum > max_sum:
            max_sum = berries_sum
            bush = i
    if i == (len(num_berries)-1):
        berries_sum = num_berries[i] + num_berries[i-1] + num_berries[0]
        if berries_sum > max_sum:
            max_sum = berries_sum
            bush = i
    else:
        berries_sum = num_berries[i] + num_berries[i-1] + num_berries[i+1]
        if berries_sum > max_sum:
            max_sum = berries_sum
            bush = i

print(f'Максимальное количество ягод {max_sum} будет собрано с {i+1} куста')