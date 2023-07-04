# def f(x):
#     return x*x;

# # print(f(5))
# print(type(f))

# a = f
# print(type(a))
# print(a(5)) # переменная а хранит в себе ссылку на переменную f


# def calk1(a, b):
#     return a+b

# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a, b: a + b, 5, 45)
    

# Задача. В списке хранятся числа. Нужно выбратаь толко четные числа и составить список пар (число; квадрат числа).

# date = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in date:
#     if i % 2 == 0:
#         res.append((i, i**2))
# print(res)


# date = [1, 2, 3, 5, 8, 15, 23, 38]

# res = map(int, date)
# res = filter(lambda x: x % 2 == 0, res)
# res =  list(map(lambda x: (x, x**2), res))
# print(res)


# Функция MAP

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x+10, list_1))
# print(list_1)

# Задача. С клавиатуры вводится некий набор чисел. в качестве разелителя используется пробел. 
# Этот набор чисел будет считан в качестве строки.Как превратить list строк в list чисел.

# date = '14 123 342 12 4 0 123'
# print(date)

# # date = date.split()
# # print(date)

# date = list(map(int, date.split()))
# print(date)


# Функция filter
# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# Функция Zip

# zip([1, 2, 3], ['o', 'l', 'd'], ['о', 'д', 'т'])
# [(1, 'o', 'о'), (2, 'l', 'д'), (3, 'd', 'т')]



# ФАЙЛЫ

# colors = ['red', '765', 'blue']
# data = open('file.txt', 'a', encoding= 'UTF-8') # мы хотим открыть file.txt в режиме а
# data.writelines(colors) # записываем в наш файл список red, разделителей не будет
# data.close()

# with open("file.txt", "w", encoding="UTF-8") as data:
#     data.write("line 1\n")
#     data.write("line 3\n")
# print(56)

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()