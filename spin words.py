# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:28:33 2020

@author: Tuli
"""

def spin_words(sentence):
    splitSentence = sentence.split(' ')
    reversed = ''
    for words in splitSentence:
        if len(words) > 4:
            reversed += words[::-1]
        else:
            reversed += words
        reversed += ' '
    return reversed[:-1]

print(spin_words("Welcome"))