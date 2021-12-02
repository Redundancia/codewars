# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 15:05:18 2020

@author: Tuli
"""

n = 9

def digitSum(n):
    if len(str(n)) == 1:
        return n
    return digitSum(sum([int(str(n)[i]) for i in range(len(str(n)))]))
print(digitSum(n))

def digital_root(n):
    return n%9 or n and 9

print(digital_root(n))