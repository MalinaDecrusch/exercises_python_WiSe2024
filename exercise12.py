# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:19:45 2024

@author: s_decrusch22

np.linalg.inv(M)= 
"""

import numpy as np

M = np.array([3,2,1,4]).reshape(2,2)

#print(M)

M_inv = np.linalg.inv(M)

I = np.matmul(M_inv, M)

a = np.array([7,5,-3,3,-5,2,5,3,-7]).reshape(3,3)

r = np.array([16,-8,0]).reshape(3,1)

A_inv = np.linalg.inv(a)

b = np.matmul(A_inv, r)

print(b)

