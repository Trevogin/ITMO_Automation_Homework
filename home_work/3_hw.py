#Задача 1

print('Задача 1')
def task1(a: int, b: int) -> int:
    if a > b:
        print(a)
    else:
        print(b)

task1(20, 10)

#Задача 2

print('Задача 2')
def task2(a: int, b: int) -> str:
    if a - b == 135 or b - a == 135:
        print('YES')
    else:
        print('NO')

task2(145, 10)


#Задача 3

print('Задача 3')
def task3(month):
    if month >= 1 and (month == 1 or month == 2 or month == 12):
        print('Зима')
    elif month >= 1 and month in range(3, 6):
        print('Весна')
    elif month >= 1 and month in range(6, 9):
        print('Лето')
    elif month >= 1 and month in range(9, 12):
        print('Осень')

task3(9)


#Задача 4

print('Задача 4')
def task4(a: int, b: int, c: int) -> str:
    if a > 10 and b > 10 and c > 10:
        print('YES')
    else:
        print('NO')

task4(11, 11, 11)


#Задача 5

print('Задача 5')
def task5(a: int, b: int, c: int, d: int, e: int) -> int:
    if a > 0:
        print(a)
    elif b > 0:
        print(b)
    elif c > 0:
        print(c)
    elif d > 0:
        print(d)
    elif e > 0:
        print(e)

task5(1, 2, 3, 4, 5)
# Вижу, что решение неверное.
# Но даже при верном решении я не знаю, как посчитать ответы и вывести их количество.
# Так что эту задачу я завалю в любом случае.


#Задача 6

print('Задача 6')
# def task6(years: int, months: int) -> int:

# Здесь я даже не знаю, с чего начать. Как указать, сколько дней в месяце, и сколько месяцев в году?
# А потом их ещё и сложить надо будет.
# Ещё один провал.