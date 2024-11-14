# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:38:02 2024

@author: s_decrusch22
"""

import numpy as np

M = np.eye(5, dtype ="int")
M[0:2,3:5] = 3
M[3:5,0:2] = 2
