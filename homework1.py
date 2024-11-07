# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 08:41:31 2024

@author: s_decrusch22


import matplotlib.pyplot as plt

def spar_funktion(AK, SR, i, lz):
            
     kapital = AK
     gesamt_kapital = []
     
     for k in range(1, lz+1):
         kapital = SR + kapital* (1+i)
         gesamt_kapital.append(round(kapital,2))
         
     return gesamt_kapital
    
#print(spar_funktion(AK = 10000, 
  #            SR = 1000, 
     #         i = 0.01, 
     #         lz = 10))

sparplan = spar_funktion(AK = 10000, 
              SR = 1000, 
              i = 0.01, 
              lz = 10)

plt.bar(range(1,11),sparplan)

"""

