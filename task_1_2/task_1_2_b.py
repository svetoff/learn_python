# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Полиндром


def palindrome(pali):
    length = len(pali)

    pol = length / 2

    pol_1 = pali[:pol]
    pol_2 = pali[-pol:]
    pol_2 = pol_2[::-1]

    if pol_1 == pol_2:
        return "{0} - Полиндром".format(pali)
    return "{0} - Не полиндром".format(pali)

print palindrome("avid diva")