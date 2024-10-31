# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:38:57 2024

@author: s_decrusch22
"""

quad_zahl = []

for zahl in range(1,11):
        if (zahl%2 == 0):
          quad_zahl.append(zahl)
        else:
            quad_zahl.append(zahl**2)
print(quad_zahl)
         
"""     
quad_zahl_neu = [zahl if zahl%2 == 0 else zahl**2 for zahl in range (1,11)]

print (quad_zahl_neu)

"""
        
        
