# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:24:14 2020

@author: Tuli
"""

def dirReduc(arr):
    for i in range(len(arr) -1):
        if arr[i] == "NORTH" and arr[i + 1] == "SOUTH":
            del arr[i:i+2]
            return dirReduc(arr)
        if arr[i] == "SOUTH" and arr[i + 1] == "NORTH":
            del arr[i:i+2]
            return dirReduc(arr)
        if arr[i] == "EAST" and arr[i + 1] == "WEST":
            del arr[i:i+2]
            return dirReduc(arr)
        if arr[i] == "WEST" and arr[i + 1] == "EAST":
            del arr[i:i+2]
            return dirReduc(arr)
    return arr