# !/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os


# comprehensions 
# 3 примера list comprehensions, возвращающих итератор 

# 2. функции 

#   a. написать функцию, возвращающую несколько значений 


def multi(x1, x2):
    return x1**3-x2, x2**2+x1
res_1, res_2 = multi(12, 6)
print res_1, res_2

#   b. генератор любой


def any_generator():
    list_users = open('users.csv')
    for i in list_users:
        yield 'Привет! ' + i.rstrip()
my_any_generator = any_generator()
for i in my_any_generator:
    print i

    #   c. пример на lambda 


lst = [2, 18, 9, 22, 17, 24, 8, 12, 27]
res_3 = filter(lambda x: x % 2 == 0, lst)
print res_3

# c. пример на nested function(вложенные функции) и на closure.


def katet(z1):
    def calc_hypotenuse(z2):
        return math.sqrt(z1**2+z2**2)
    return calc_hypotenuse
mid_res = katet(10)
hypotenuse = mid_res(23)
print(hypotenuse)

# d. снова, по примеру на *args, **kwargs, optional и named


def test_args(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

args = ("два", 3)
test_args(1, *args)


def test_kwargs(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3

kwargs = {"arg3": 3, "arg2": "два"}
test_kwargs(1, **kwargs)


def test_named(b=6, c=12):
    print b, c
test_named()
test_named(9, 17)
test_named(b=125, c=36)


#   e. декораторы 


def name_func(func):
    """
    Декоратор выводящий имя
    декорируемой функции
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__
        return res
    return wrapper


@name_func
def test_named(b=6, c=12):
    print b, c
test_named()
test_named(9, 17)
test_named(b=125, c=36)


def time_func(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print time.clock() - t
        return res
    return wrapper


@time_func
def test_named(b=6, c=12):
    print b, c
test_named()
test_named(9, 17)
test_named(b=125, c=36)


def user_func(func):
    """
    Декоратор, запрещающий
    выполнение декорируемой функции
    если она запущена не от заданного пользователя.
    """

    def wrapper(*args, **kwargs):
        user = os.getlogin()
        if user == "vlad":
            res = func(*args, **kwargs)
            return res
        else:
            print "Запуск скрипта возможен только пользователем vlad"

    return wrapper


@user_func
def test_named(b=6, c=12):
    print b, c
test_named()
test_named(9, 17)
test_named(b=125, c=36)



"""Декоратор, ничего не делающий если функция True,
и выводящий строку если  """


class StringException(Exception):
    def __init__(self):
        Exception.__init__(self)


def string_or_true(function):
    def wrapper(*args, **kwargs):
        type_of_func = function(*args, **kwargs).__class__
        res = function(*args, **kwargs)
        try:
            if test_func is True:
                pass
            elif type_of_func is str:
                raise StringException
        except StringException:
            print res
    return wrapper


@string_or_true
def test_func(arg):
    return arg

test_func(True)
