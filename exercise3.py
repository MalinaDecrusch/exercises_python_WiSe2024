# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 08:45:52 2024

@author: s_decrusch22
"""
werte = [0,0,1,1]

def steigung_funktion(werte):
    x1= werte[0]
    y1= werte[1]
    x2= werte[2]
    y2= werte[3]
    
    
    delta_x = x2-x1
    delta_y= y2-y1
    
    if (delta_x == 0):
        print("die steigung ist nicht definiert")
    
    else: 
        steigung = delta_y / delta_x
        return(steigung)
    
print(steigung_funktion(werte))





        
