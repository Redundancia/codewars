# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:58:28 2020

@author: Tuli
"""
cc = "szotyola"

def maskify(cc):
    masked = ''
    if len(cc) <= 4:
        masked = cc
    if len(cc) > 4:
        for i in range(len(cc)- 4):
            masked += '#'
        for i in range(-4, 0):
            masked += cc[i]
    return masked


print(maskify(cc))

masked3 = ['#' if len(cc) - c > 4 else cc[c] for c in range(len(cc))]
print(''.join(masked3))

def maskify_Opt(cc):
    
    return ''.join(['#' if len(cc) - c > 4 else cc[c] for c in range(len(cc))])

print(maskify_Opt(cc))   

#helper for comprehension
list1 = [i for i in range(15) if i%2 == 0]

list2 = [i if i%2 == 0 else i for i in range(15)]