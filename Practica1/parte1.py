# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 17:55:06 2018

@author: Eva Gala

1. Implementar una funcion que clasifica un punto x ∈ R
D segun si esta por encima o por debajo
del hiperplano definido por w˜ ∈ R
D+1. La definicion de la funcion sera:
def classify(x, w)
"""
import numpy as np

def classify(x,w):
    xg = np.insert(x, 0, np.matrix('1') , axis=0)
    return np.dot(np.transpose(w), xg) > 0

t = classify(np.matrix('5;6'), np.matrix('1; 3; 4'))