# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# В функцию передается список.
# Найти все повторяющиеся элементы.
# регистрозависимо


def find_repeat(str):
    lst = []
    long_str = len(str)
    i = 1
    for char in str:
        if char in str[i:long_str]:
            if char in lst:
                continue
            else:
                lst.append(char)

        i += 1
    if not lst:
        return ('не найдено повторений')
    return lst
print find_repeat([
                    'bob', 'helly', [1, 2, 3], 'Bob', 'Alize', 'Ivan', 'helly',
                    'helly', '0.12', '0.12', [1, 2, 3]])
