# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:38:57 2020

@author: Tuli
"""

def rgb(r, g, b):
    L1 = [r, g, b]
    for i in range(len(L1)):
        if L1[i] > 255:
            L1[i] = hex(255)[2:].upper()
        elif L1[i] < 0:
            L1[i] = "00"
        elif L1[i] < 10:
            L1[i] = f'{L1[i]:02}'
        else:
            L1[i] = hex(L1[i])[2:].upper()
    return "".join(L1)

print(rgb(300,-10,17))

def rgb2(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))


print(rgb2(300,-10,17))


round = lambda x: min(255, max(x, 0))
print(("{:02X}" * 3).format(round(256), round(9), round(56)))
