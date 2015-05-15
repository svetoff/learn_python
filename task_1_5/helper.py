# !/usr/bin/env python
# -*- coding: utf-8 -*-

# Модуль argparse
# Написать модуль helper, принимающий следующие опции:
# t | ­­time
# выводит текущее время
# d | ­­date
# выводит текущую дату.
# u | ­­uname
# выводит имя текущего пользователя
# v | ­­version
# выводит текущую версию python­ интерпретатора.
# t | ­­tree
# выводит список файлов в текущей директории

import argparse
import datetime
import os
from sys import version


parser = argparse.ArgumentParser()

parser.add_argument(
    '-t', '--time', action='store_true',
    help='Выводит текущее время')
parser.add_argument(
    '-d', '--date', action='store_true',
    help='Выводит текущую дату')
parser.add_argument(
    '-u', '--uname', action='store_true',
    help='Выводит имя текущего пользователя')
parser.add_argument(
    '-v', '--version', action='store_true',
    help='Выводит текущую версию python­ интерпретатора.')
parser.add_argument(
    '-T', '--tree', action='store_true',
    help='выводит список файлов в текущей директории')

output = parser.parse_args()

if output.time:
    print datetime.datetime.now().strftime("%H:%M:%S")

elif output.date:
    print datetime.date.today().strftime("%d.%m.%Y")

elif output.uname:
    print os.getlogin()

elif output.version:
    print version

elif output.tree:
    for items in os.listdir("."):
        print items
else:
    parser.print_help()
