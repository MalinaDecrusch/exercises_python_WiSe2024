# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:35:55 2024

@author: s_decrusch22
"""
import math
from math import sqrt


ak = 100

ek = 700

t = 30


def cagr_berechnung(ak,ek, t):
    ak_abs= abs(ak) 
    cagr = ((ek/ak_abs)**(1/t)-1)
    return cagr
    


print (cagr_berechnung(ak, ek, t))

rendite = (cagr_berechnung(ak, ek, t))

print(120*(1+rendite)**30)

    
        
   
    