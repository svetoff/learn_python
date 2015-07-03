# !/usr/bin/env python
# -*- coding: utf-8 -*-


class GeneratorHTML(object):
    def __init__(self):
        self.name_to_file = "tags.txt"
        self.list_tags_spase = []
        self.list_spase = []
        self.list_tags = []
        self.dict_tags = {
            'html': ("<html>", "</html>"),
            'head': ("<head>", "</head>"),
            'title': ("<title>", "</title>"),
            'body': ("<body>", "</body>"),
            }

    def open_file(self):
        # lst_temp = self.dict_tags['html']
        # print lst_temp[1]
        try:
            in_file = open(self.name_to_file, 'r')

        except IOError as e:
            print "Файл не найден"
        reverse_list_space = []
        reverse_list_tags = []
        for line in in_file.xreadlines():
            tags = line.rstrip().replace(' ', '')
            self.list_tags.append(tags)
            reverse_list_tags.append(tags)
            spaces = ' ' * line.count(' ')
            self.list_spase.append(spaces)
            reverse_list_space.append(spaces)

        with open('output.txt', 'w') as output_file:
            reverse_list_tags.reverse()
            reverse_list_space.reverse()
            while reverse_list_tags:
                tag = reverse_list_tags.pop()
                lst_temp = self.dict_tags[str(tag)]
                output_file.writelines("{0}{1}\n".format(reverse_list_space.pop(), lst_temp[0]))
            while self.list_tags:
                tag = self.list_tags.pop()
                lst_temp = self.dict_tags[str(tag)]
                output_file.writelines("{0}{1}\n".format(self.list_spase.pop(), lst_temp[1]))

p = GeneratorHTML()
p.open_file()
