# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 08:30:11 2020

@author: Tuli
"""

def make_readable(seconds):
    hour = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    return ":".join([(f'{hour:02}'), (f'{minutes:02}'), (f'{seconds:02}')])

print(make_readable(3500))