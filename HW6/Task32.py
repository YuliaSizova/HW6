# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
# больше заданного максимума)

from random import randint

list_1=[randint(-10,20)for i in range(20)]
print(list_1)
min_number = int(input('Введите минимальное число '))
max_number = int(input('введите максимально число '))
for i in range(len(list_1)):
  if min_number <= list_1[i] <= max_number:
     print(i)

