# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 19:00:55 2018

@author: vuvux


3. Dada una nube de puntos X y un vector de clases t, implementar una funcion 
que calcule el vector de pesos w˜ ∈ R^D+1 asociado a (X, t) por el algoritmo de
LDA (tambien conocido como discriminante lineal de Fisher). 
La definicion de la funcion sera:
def lda(X, t)
"""
import numpy as np
from numpy.linalg import inv

def lda(X, t):
    X1 = X[(t==0),:]; "Consideramos las clases como 0 y mayor que 0"
    X2 = X[(t>0),:];
    "Calculamos las medias"
    m1 = np.mean(X1, axis=0);
    m2 = np.mean(X2, axis=0);
    n = len(X[1,:]);
    Sw1 = np.zeros((n, n));
    Sw2 = np.zeros((n, n));
    for x_1 in X1:
        Sw1 = np.add(np.dot((x_1-m1)[:,np.newaxis],((x_1-m1)[:,np.newaxis]).T), Sw1);
    for x_2 in X2:
        Sw2 = np.add(np.dot((x_2-m2)[:,np.newaxis],((x_2-m2)[:,np.newaxis]).T), Sw2);
    Sw = np.add(Sw1,Sw2);
    Sb = np.dot((m2-m1)[:,np.newaxis],((m2-m1)[:,np.newaxis]).T);
    A = np.dot(np.linalg.inv(np.matrix(Sw)), Sb);
    tmp = np.linalg.eig(A);
    eigenval, eigv = tmp;
    tmp = np.argmin(eigenval);
    separador = np.delete(eigv, (tmp), axis=0);
    return separador;
t = lda(np.array([[7,4],[5,8],[3,5], [6,1], [5,2]]), np.array([1,0,0,1,1]))