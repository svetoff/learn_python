# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
# В функцию передается список строк. Отсортировать список по последней букве
# слова.


def range_lst_of_last_char(specified_lst):
    lst = []

    for char in specified_lst:
        lst.append(char[-1])

    d = dict(zip(lst, specified_lst))
    lst.sort()
    specified_lst = []

    for char in lst:
        specified_lst.append(d[char])
    return specified_lst
print range_lst_of_last_char([
    'dfgfcgh',
    'fhfhggggdf',
    'hcddddy47ggg2yqwtqswrsqweqs',
    'sqwn235gdtsgdyw7eyi2qwwwwww',
    '<heduoleiyer72>;wk21lue319i2o7e</heduoleiyer72kreyi2',
    'jlsuwdiqjsy8wj2eiyi',
    'ed3yjqw37yei21e473yier',
    'a',
    'b'])
