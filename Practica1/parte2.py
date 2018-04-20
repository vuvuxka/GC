# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:40:47 2018

@author: Eva Gala

2. Dada una nube de puntos X y un vector de clases t, implementar un funcion 
que calcule el vector de pesos w˜ ∈ R
D+1 asociado a (X, t) por el algoritmo de mınimos cuadrados. La
definicion de la funcion sera:
def least_squares(X, t)
"""
import numpy as np

def least_squares(X, t):
    n = X.shape[1]
    Xg = np.insert(X, 0, np.ones(n) , axis=0)
    XXt = np.dot(Xg, np.transpose(Xg));
    XXt2 = np.transpose(np.linalg.inv(XXt));
    XXt2X = np.dot(XXt2, Xg);
    return np.dot(XXt2X, np.transpose(t))

t = least_squares(np.matrix('1 2 3 4; 5 15 7 8; 9 10 11 12'), np.matrix('1, 2, 3, 45'))