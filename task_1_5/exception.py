# !/usr/bin/env python
# -*- coding: utf-8 -*-


class NegativNumbersException(Exception):
    '''Пользовательский класс исключения.'''

    def __init__(self):
        Exception.__init__(self)

file_numbers = open('test.txt')
int_numbers = []

try:
    for numbers in file_numbers:
        if int(numbers) < 0:
            raise NegativNumbersException
        int_numbers.append(int(numbers))
except ValueError:
    print('Error: Это не число. Выходим.')
except NegativNumbersException:
    print('Error: Число отрицательное. Выходим')
else:
    print('Всё хорошо.')
finally:
    file_numbers.close()
    print('Я закрыл файл.')
