# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:36:16 2024

@author: s_decrusch22
"""

def buchstaben_ändern(string, buchstaben):
    string_lower = string.lower()
    
    for v in "aeiou":
        new_sentence = []
        
        for char in string_lower:
            if char == buchstaben:
                new_sentence.append(v)
                
            else:
                new_sentence.append(char)
                
        print("".join(new_sentence))
        
buchstaben_ändern(string ="banana",buchstaben = "a")
    