# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:08:14 2024

@author: s_decrusch22
"""

x = 4

y = 3


def teilbar(x,y): 
    
    if y==0:
        print("Es ist nicht möglich durch 0 zu teilen")
        
    elif y==x: 
        print ("X und y sind gleich")
          
    else:
        if x%y == 0:
          print("x ist durch y teilbar")
          
        else:
            print("x ist nicht durch y teilbar")

        
teilbar(x,y)