# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:55:29 2024

@author: s_decrusch22
"""
wort = "hallo, berlin"

def buchstaben_zählen(wort):
    meine_liste = list(wort)
    wort_buchstaben= [i for i in meine_liste if i.isalpha()]
    x_buchstaben_len= len(wort_buchstaben)
    return x_buchstaben_len
    
    
print (buchstaben_zählen(wort))



"""list splittet string"""
