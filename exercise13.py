# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:38:03 2024

@author: s_decrusch22
"""

from math import log10
import numpy as np

x = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000, 10000000000]

x_log10 = [log10(k)for k in x]

x_log10_array = np.log10(x)