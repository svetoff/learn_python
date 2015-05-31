# !/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools


# comprehensions 
# 3 примера list comprehensions, возвращающих итератор 

    # модифицируем список 

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list_1 = [i**2 for i in list_1]
print list_1

    # содержит условие, возводим в квадрат только чётные числа

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
list_2 = [i**2 for i in list_2 if i % 2 == 0]
print list_2

    # использует 2 списка 

list_3_1 = [1, 2, 3, 4, 5, 6, 7]
list_3_2 = [8, 9, 10, 11, 12, 13, 14, 15]
list_3 = [2*i for i in itertools.chain(list_3_1, list_3_2)]
print list_3


# 3 примера list comprehensions, возвращающих генератор 

    # модифицируем список 

list_2_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
myGenerator = (i**2 for i in list_2_1)
list_2_1 = []
for i in myGenerator:
    list_2_1.append(i)
print list_2_1

    # содержит условие, возводим в квадрат только чётные числа

list_2_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
myGenerator = (i**2 for i in list_2_2 if i % 2 == 0)
list_2_2 = []
for i in myGenerator:
    list_2_2.append(i)
print list_2_2

    # использует 2 списка 

list_2_3_1 = [1, 2, 3, 4, 5, 6, 7]
list_2_3_2 = [8, 9, 10, 11, 12, 13, 14, 15]
myGenerator = (2*i for i in itertools.chain(list_3_1, list_3_2))
list_2_3 = []
for i in myGenerator:
    list_2_3.append(i)
print list_2_3


# 5 примеров работы с itertools.

    # itertools.cycle()

list_3 = [1, 3, 5]
i = 0
for x in itertools.cycle(list_3):
    print x
    i += 1
    if i > 10:
        break

    # itertools.count()

for i in itertools.count(25):
    print i,
    if i > 100:
        break

    # enumerate()

list_3_3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
myGenerator = [x for x in enumerate(list_3_3)]
print myGenerator

    # itertools.repeat()

list_3_4 = [1, 2, 3, 4, 5]
for x in itertools.repeat(list_3_4, 5):
    print x

    # itertools.islice()

for i in itertools.islice(range(100), 12, 32, 3):
        print i

    # itertools.permutations()

permut = [x for x in itertools.permutations("abcdefg", 3)]
print permut
