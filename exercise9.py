# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:18:12 2024

@author: s_decrusch22

a.size = wie viele elemetne
a.dtype = welcher typ zb Int
respahe = array neue dimensionen erstellen
arange = elemente von wo bis wo
"""

import numpy as np

a= np.arange(1, 13).reshape(3, 2, 2)

print(a)