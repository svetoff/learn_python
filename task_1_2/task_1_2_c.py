# !/usr/bin/env python
# -*- coding: utf-8 -*-


def find_letter(where, letter):
    if letter in where:
        where = where.split()
        lst = []
        for word in where:
            if word[0].lower() == letter.lower():
                lst.append(word)
                continue
        return lst
    else:
        return ("Буквы - \"{0}\" нет в строке - \"{1}\"").format(letter, where)


print find_letter("Bears are the best animals ever", 'b')
