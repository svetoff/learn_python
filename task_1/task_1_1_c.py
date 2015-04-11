# !/usr/bin/env python
# -*- coding: utf-8 -*-


def simple(number):
    if number == 1:  # если number = 1

        return 'Единица не относится ни к простым, ни к составным числам'

    if number < 1 or not isinstance(number, int):  # если number отрицательная или не int

        return 'Число {0} не является натуральным'.format(number)

    i = 2

    while number != i:  # число будет простым если делится только на себя и 1

        if number % i == 0:  # если number разделось на i нацело

            return 'Число {0} не является простым'.format(number)

        i += 1

    return 'Число {0} является простым'.format(number)

print(simple(13))
