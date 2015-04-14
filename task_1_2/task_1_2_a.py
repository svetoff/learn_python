# !/usr/bin/env python
# -*- coding: utf-8 -*-


def letters(big_string):
    lst = []
    if big_string.islower():
        return "Все буквы маленькие"
    else:
        for char in big_string:
            if char.isupper():
                lst.append(char)
        lst = ''.join(lst)
        return "В строке найдены следующие заглавные буквы: {0}".format(lst)

print letters("Trees Are So Kind")