# !/usr/bin/env python 
# -*- coding: utf-8 -*- 
import math  # подключаем библиотеку для работы sqrt


def equation(a, b, c):

    D = b*b - 4*a*c  # считаем дискриминант

    if D < 0:  # если меньше 0 нет корней

        return "Корней нет"

    if D == 0:  # если равен 0 один корень

        x1 = -b / (2 * a)

        return 'Один корень x1 = %.2f' % x1

    if D > 0:  # если больше 0 два корня

        x1 = (-b + math.sqrt(b*b - 4*a*c))/(2 * a)
        x2 = (-b - math.sqrt(b*b - 4*a*c))/(2 * a)

        return 'Два корня x1 = %.2f, x2 = %.2f' % (x1, x2)

print(equation(1, 22, 4))  # вводим коэффициенты a, b, c
