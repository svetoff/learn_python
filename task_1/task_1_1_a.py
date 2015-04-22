# !/usr/bin/env python
# -*- coding: utf-8 -*-


def multipliers(number):
    if number == 1:  # если number = 1
        return [1]  # выводим 1
    if number < 1 or not isinstance(number, int):
        raise TypeError  # выводим ошибку
    lst = []  # объявляем пустой список
    i = 2
    while number != 1:
        if number % i == 0:  # если number разделось на i нацело
            number = number // i
            lst.append(i)  # добавляем i в список
            continue  # не увеличивая i возвражщаемся к началу цикла
        i += 1
    return lst
print(multipliers(30030))
