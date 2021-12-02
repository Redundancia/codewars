# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:16:50 2020

@author: Tuli
"""
import re

def land_perimeter(arr):
    perimeter = 0
    for row in arr:
        perimeter += row.count('X') * 4
        perimeter -= sum(2 for _ in re.finditer('(?=XX)', row))
    for column in (zip(*arr)):
        perimeter -= sum(2 for _ in re.finditer('(?=XX)', "".join(column)))
    return "Total land perimeter: " + str(perimeter)
    


(land_perimeter(["OXOOOX", 
                      "OXOXOO", 
                      "XXOOOX", 
                      "OXXXOO", 
                      "OOXOOX", 
                      "OXOOOO", 
                      "OOXOOX", 
                      "OOXOOO", 
                      "OXOOOO", 
                      "OXOOXX"]))