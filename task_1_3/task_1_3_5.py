# !/usr/bin/env python
# -*- coding: utf-8 -*-
# В функцию передается 2 списка и элемент. Найти этот элемент в первом списке
# и вставить на ту же позицию во втором.


def lst_add_str(lst_1, lst_2, element):
    position = lst_1.index(element)
    lst_2.insert(position, element)
    return lst_2
print lst_add_str([
                    'a', 'bc', 'dasdsa', 'ewrtry', 'fkr', 'gto',
                    'jkhjk', 'ad', 'wqewqewq', 'yasdasd'], [
                    'dfhj', 'wetywety', 'word', 'pass', 'house', 'elsa', 'pep',
                    'python', 'dff', 'koll', 'dersu'], 'ad')
