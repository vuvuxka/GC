# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 11:18:11 2018

@author: vuvux
"""

import matplotlib.pyplot as plt
from dibujapuntos import *

fig = plt.figure()
ax = plt.subplot(111)
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_aspect('equal')  

start = CreatePoints(fig, ax)

plt.show()
#end = CreatePoints(fig,ax, "b")