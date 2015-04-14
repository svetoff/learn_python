# !/usr/bin/env python
# -*- coding: utf-8 -*-


# atm uses only 100, 50, 20, 10, 5 and 1 notes.
def atm(summ):
    bill = [100, 50, 20, 10, 5, 1]
    i = 0  # счётчик
    j = 0  # счётчик кол-ва купюр
    lst = []

    if summ <= 0 or not isinstance(summ, int):
        return "Сумма денег должна быть целым числом больше нуля"

    if summ in bill:
        return "Получите купюру в {0} рублей".format(summ)

    while summ != 1:
        if summ >= bill[i]:
            summ = summ - bill[i]
            if summ != bill[i]:
                j += 1
                continue
            else:
                j +=2

        lst.append("{0} RUB - {1} pieces".format(bill[i], j))  # на кириллицу ругается :(
        i += 1
        j = 0

    return lst
print atm(287)

