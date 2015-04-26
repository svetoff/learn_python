# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Dictionary и их методы.

    # создание словаря.
    # a. из двух списков


def dict_2_list(lst_1, lst_2):
    final_dict = dict(zip(lst_1, lst_2))
    return final_dict


    # создание словаря.
    # b. из списка кортежей


def dict_list_tuple(lst_tuple):
    dict(lst_tuple)
    return lst_tuple


    # Написать функцию, которая принимает словарь и строку.
    # Найти в словаре ключ,
    # соответствующий строке и выставить его значение в None


def find_str_dict(dict_3, str_3):
    for key, value in dict_3.iteritems():
        if value == str_3:
            dict_3[key] = None
    return dict_3


    # Написать функцию, в которую передается два словаря. из обоих словарей
    # удалить повторяющиеся ключи, словари склеить


def del_repeate_2_dict(dict_4_1, dict_4_2):
    lst_remove = []
    for key, value in dict_4_1.iteritems():
        if key in dict_4_2:
            # пробовал удалять значения прямо в цикле выдает ошибку, из-за того
            # что словарь изменился
            lst_remove.append(key)
    for i in lst_remove:
        del dict_4_1[i]
        del dict_4_2[i]
    dict_4_1.update(dict_4_2)
    return dict_4_1

    # Написать функцию “калькулятор”. В функцию передается название операции и
    # аргументы, например: calculate(‘add’, 2, 4) => 6
    # Не используя if...else операторы.


def calculator(operation, char_1, char_2):
    dict_calc = {
        'summ': char_1 + char_2,
        'mult': char_1 * char_2,
        'div': char_1 / char_2,
        'subtr': char_1 - char_2}
    return dict_calc[operation]
print calculator('summ', 20, 4)


# Написать функцию, в которую передается словарь. Вернуть словарь, в котором
# keys и values поменяны местами.
# {‘a’: 1, ‘b’: 2} => {1: ‘a’, 2: ‘b’}


def dict_inv(dict_5):
    return dict((v, k) for k, v in dict_5.iteritems())


print dict_inv({
    0: 'January', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May',
    5: 'Jun', 6: 'Jul', 7: 'Aug', 8: 'Sep', 9: 'Oct', 10: 'Nov',
    11: 'Dec'})


print del_repeate_2_dict({
    0: 'January', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May',
    5: 'Jun', 6: 'Jul'},
    {6: 'Jul', 7: 'Aug', 8: 'Sep', 9: 'Oct', 10: 'Nov', 11: 'Dec'})


print find_str_dict({
    0: 'January', 1: 'Feb', 2: 'Mar', 3: 'Apr', 4: 'May',
    5: 'Jun', 6: 'Jul', 7: 'Aug', 8: 'Sep', 9: 'Oct', 10: 'Nov',
    11: 'Dec'}, 'Aug')

print dict_list_tuple([
    ('Moscow', 'Russia'), ('Kiev', 'Ukraine'), ('USA', 'Washington')])

print dict_2_list(['Moscow', 'Kiev', 'Washington'], [
    'Russia', 'Ukraine', 'USA'])
