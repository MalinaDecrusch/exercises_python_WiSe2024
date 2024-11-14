# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:50:24 2024

@author: s_decrusch22

axis0= links nach rechts

axis1=oben nach unten


"""

import numpy as np

data = np.arange(1, 11)

D = np.tile(data, 10).reshape(10,10)

print(D.sum(axis=0))

print(D.mean(axis =1)) 
