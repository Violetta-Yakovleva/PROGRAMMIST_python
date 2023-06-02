# Задача 2 .Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали ```S``` журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Примеры/Тесты:
# 6 >>>  1  4  1
# 24 >>> 4  16  4
# 60 >>> 10  40  10

# petr = x
# serg  = x
# kate = (x+x)*2
# sum = x + x + (x + x) * 2 = 2x + 2x + 2x = 6x

sum = int(input('Сколько всего журавликов сделали ребята: '))

if sum % 6 == 0:
    petr = sum  // 6
    serg = sum // 6
    kate = (sum // 6)*4
    print(f'Петя сделал {petr} журавликов, Сережа сделал {serg} журавликов, Катя сделала {kate} журавликов.')
else:
    petr = sum  // 6
    serg = sum // 6
    kate = (sum // 6)*4
    teacher = sum - petr - serg - kate
    print(f'Петя сделал {petr} журавликов, Сережа сделал {serg} журавликов, Катя сделала {kate} журавликов, а учитель сделал {teacher}.')