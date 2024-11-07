# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:17:48 2024

@author: s_decrusch22
"""

"""
Geometrische Liste berechnen
"""
import matplotlib.pyplot as plt


r = 1.1

a = 1
n = 10
s_n=[]
summe = 0


for k in range(0,n):
    summe += a*r**k
    s_n.append(summe)
print (s_n)

plt.plot(s_n)




