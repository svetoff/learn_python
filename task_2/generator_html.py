# !/usr/bin/env python
# -*- coding: utf-8 -*-


class GeneratorHTML(object):
    def __init__(self):
        self.name_to_file = "tags.txt"

    def open_file(self):
        try:
            in_file = open(self.name_to_file, 'r')

        except IOError as e:
            print "Файл не найден"

p = GeneratorHTML()
p.open_file()

