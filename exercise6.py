# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 09:26:33 2024

@author: s_decrusch22
"""

a = 1
r = 0.5
s = 0
k = 0
limit = (a/(1-r))
epsilon = 0.001

while True:
    s += a * r**k
    k += 1
    print(s, end = " ")

    #Erste lösung   
    #if s == (a/(1-r)):
      #  break
  
    if(limit - s) < epsilon:
         break
    
    

""" solange differenz kleiner ist als epsilon wird geprintet, wenn nicht wird
while schlelife gestoppt"""

