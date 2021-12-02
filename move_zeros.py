# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 06:47:51 2020

@author: Tuli
"""

def move_zeros(array):
    for e in range(len(array)- 1, 0 -1, -1):
        if array[e] is False:
            continue
        if array[e] == 0:
            array.append(array.pop(e))
    return array

print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))