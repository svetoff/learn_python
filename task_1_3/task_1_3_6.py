# !/usr/bin/env python
# -*- coding: utf-8 -*-
# В список передается строка. Удалить из строки все слова, с нечетным
# количеством букв.


def del_odd(def_str):
    def_str = def_str.split()

    for word in def_str:
        if len(word) % 2 != 0:
            def_str.remove(word)

    def_str = ' '.join(def_str)

    return def_str
print del_odd("""It is a long established fact that a reader will be distracted
                by the readable content of a page when looking at its layout
                The point of using Lorem Ipsum is that it has a more-or-less
                normal distribution of letters as opposed to using Content here
                content here making it look like readable English Many desktop
                publishing packages and web page editors now use Lorem Ipsum as
                their default model text and a search for lorem ipsum will
                uncover many web sites still in their infancy Various versions
                have evolved over the years sometimes by accident sometimes on
                purpose""")
