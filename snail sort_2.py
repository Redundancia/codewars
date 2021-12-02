# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:58:19 2020

@author: Tuli
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 09:22:36 2020

@author: Tuli
"""

def snail(snail_map):
    snail = []
    while len(snail_map) > 0:
        for l in snail_map[0]:
            snail.append(l)
        del snail_map[0]

        if len(snail_map) == 0:
            break
        
        for i in range(len(snail_map)):
            snail.append(snail_map[i][len(snail_map[i]) -1])
        for k in snail_map:
            k.pop(-1)
            
        for k in range(len(snail_map[-1]) -1, -1, -1):
                snail.append(snail_map[-1][k])
        del snail_map[-1]
    
        for i in range(len(snail_map)-1, -1, -1):
            snail.append(snail_map[i][0])
        for k in snail_map:
            k.pop(0)
            
    return snail
        
array = [[1,2,3,4,5],
         [6,7,8,9,10],
         [11,12,13,14,15],
         [16,17,18,19,20],
         [21,22,23,24,25]]

print(snail(array))