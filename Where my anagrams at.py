# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:25:05 2020

@author: Tuli
"""

def anagrams(word, words):
    
    return [i for i in words if sorted(i) == sorted(word)]
    
    answer = []
    for i in words:
        print(i)
        if sorted(i) == sorted(word):
            answer.append(i)            
    return answer
    
    

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))