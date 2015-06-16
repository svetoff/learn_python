# !/usr/bin/env python
# -*- coding: utf-8 -*-
import math


#   d. снова, по примеру на *args, **kwargs, otional и named 
#   e. декораторы 
#       i. написать декоратор, показывающий время работы функции 
#       ii. декоратор, выводящий имя функции перед результатом ее 
# работы 
#       iii. Декоратор, запрещающий выполнение функции, если скрипт 
# запущен не от указанного пользователя. 
#       iv. Декоратор. Если функция вернула True, не делает ничего, если 
# вернула строку, выбрасывает исключение, с этой строкой в 
# качестве параметра.

# comprehensions 
# 3 примера list comprehensions, возвращающих итератор 

# 2. функции 

	#   a. написать функцию, возвращающую несколько значений 


def multi(x1, x2):
	return x1**3-x2, x2**2+x1
res_1, res_2 = multi(12,6)
print res_1, res_2

	#   b. генератор любой


users = [user.rstrip() for user in open('users.csv') if user[0] == 'i']
print users

	#   c. пример на lambda 


lst = [2, 18, 9, 22, 17, 24, 8, 12, 27]
res_3 = filter(lambda x:x%2==0, lst)
print res_3

	# c. пример на nested function(вложенные функции) и на closure.


def katet(z1):
	def calc_hypotenuse(z2):
		return math.sqrt(z1**2+z2**2)
	return calc_hypotenuse
mid_res = katet(10)
hypotenuse = mid_res(23)
print(hypotenuse)

	
