# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# В функцию передается список. Вывести статистику по типам данных элементов
# Например: list => 2, int => 4


def stat(specified_lst):

    lst_type = []
    lst_count = []
    i = 1

# Получаем список с типами элементов заданного списка
    for char in specified_lst:
       lst_type.append(char.__class__.__name__)

# Берём элемент списка lst_type и считаем количество вхождений
    for char in lst_type:
# Отбрасываем уже посчитанные типы
        if char in lst_type[0:i-1]:
            i += 1
            continue
        i += 1
        lst_count.append("{0} => {1}".format(str(char), str(lst_type.count(char))))
    return lst_count

print stat([
    'bob',
    'helly',
    [1, 2, 3],
    'Bob',
    'Alize',
    'Ivan',
    'helly',
    'helly',
    0.12,
    0.156,
    [1, 2, 3],
    52,
    19,
    -25])
