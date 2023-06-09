# Задача 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

# a = int(input('Введите 6-значный номер билетика для проверки его на "Счастливый билетик": '))

# if 1 <= a // 100000 <= 9:
#     a = str(a)
#     sum1 = int(a[0]) + int(a[1]) + int(a[2])
#     sum2 = int(a[3]) + int(a[4]) + int(a[5])
#     if sum1 == sum2:
#         print('Ура! Счастливый билетик!')
#     else:
#         print('Увы! Это простой билетик')
# else:
#     print('Вы ввели некорректное число')


# **Усложнение.** Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор

a = int(input('Введите 6-значный номер билетика для проверки его на "Счастливый билетик": '))

if 1 <= a // 100000 <= 9:
    a = str(a)
    sum1 = int(a[0]) + int(a[1]) + int(a[2])
    sum2 = int(a[3]) + int(a[4]) + int(a[5])
    print('Ура! Счастливый билетик!') if sum1 == sum2 else print('Увы! Это простой билетик')       
else:
    print('Вы ввели некорректное число')