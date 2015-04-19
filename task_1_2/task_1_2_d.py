# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def mix_words(just_string):
    just_string = just_string.split( )
    random.shuffle(just_string)
    return just_string

print mix_words("Bears are the best animals ever")
