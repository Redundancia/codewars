# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 04:16:11 2020

@author: Tuli
"""

def split_string(s):
    string_split = []
    sz = s[:]
    if len(s) % 2 == 1:
        sz += "_"
    print(sz)
    for i in range(0, len(sz), 2):
        string_split.append(sz[i:i+2])
    return string_split

s = "szotyolaa"

print(split_string(s))


import re

def solution(s):
    return re.findall("..", s + "_")

import re

def solution(s):
    return re.findall(".{2}", s + "_")