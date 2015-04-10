# !/usr/bin/env python 
# -*- coding: utf-8 -*- 

def mn(n):
    if n == 1:  # если n = 1
        return [1]  # выводим 1
    if n < 1 or not isinstance(n, int):  # если n отрицательная или не int
        raise TypeError  # выводим ошибку
    lst = []  # объявляем пустой список
    i = 2
    while n != 1:
        if n % i == 0:  # если n разделось на i нацело
            n = n // i
            lst.append(i)  # добавляем i в список
            continue  # не увеличивая i возвражщаемся к началу цикла
        i += 1
    return lst
print(mn(3579))
