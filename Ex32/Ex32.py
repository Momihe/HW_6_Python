# Задача 32: Определить индексы элементов массива (списка), значения
# которых принадлежат заданному диапазону 
# т.е. не меньше заданного минимума и не больше заданного максимума)


import random
n = int(input('Введите длинну исходного массива: '))
min = int(input('Введите минимальное число: '))
max = int(input('Введите максимальное число: '))
list1 = [random.randint(0, 10) for i in  range(n)]
list2 = [i for i in range(len(list1)) if min <= list1[i] <= max]
print('Исходный массив: ')
print(list1)
print('Массив индексов: ')
print(list2)
