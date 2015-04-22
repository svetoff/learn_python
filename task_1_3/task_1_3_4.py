# !/usr/bin/env python
# -*- coding: utf-8 -*-
#В функцию передается уже отсортированный список строк и строка. Вставить
# строку в нужную позицию в списке, чтобы список остался отсортированным.


def lst_add_str(lst_range, specified_str):
    i = 0
    j = len(lst_range) - 1
    while i < j:
        mid = (i + j) // 2
        if specified_str > lst_range[mid]:
            i = mid + 1
        else:
            j = mid
    if lst_range[j] < specified_str:
        lst_range.insert(j + 1, specified_str)
    else:
        lst_range.insert(j, specified_str)
    return lst_range
print lst_add_str(['a', 'bc', 'dasdsa', 'ewrtry', 'fkr', 'gto', 'jkhjk', 'wqewqewq', 'yasdasd'],'ad')
