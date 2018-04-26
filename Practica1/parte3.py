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
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def lda(X, t):
    X1 = X[(t[0,:]==1),:];
    X2 = X[(t[1,:]==1),:];
    "Calculamos las medias"
    m1 = np.mean(X1, axis=0);
    m2 = np.mean(X2, axis=0);
    n = len(X[0,:]);
    Sw1 = np.zeros((n, n));
    Sw2 = np.zeros((n, n));
    
    for x_1 in X1:
        Sw1 = np.add(np.dot((x_1-m1)[:,np.newaxis],((x_1-m1)[:,np.newaxis]).T), Sw1);
    
    for x_2 in X2:
        Sw2 = np.add(np.dot((x_2-m2)[:,np.newaxis],((x_2-m2)[:,np.newaxis]).T), Sw2);
    
    Sw = np.add(Sw1,Sw2);
    
    Sw = np.array ([[0.2827, 22.9167],[22.9167, 47098.1844]])
    
    Sb = np.dot((m2-m1)[:,np.newaxis],((m2-m1)[:,np.newaxis]).T);
    if np.linalg.det(Sw) == 0:
        return False
    A = np.dot(np.linalg.inv(Sw), Sb);
    tmp = np.linalg.eig(A);
    eigenval, eigv = tmp;
    tmp = np.argmin(eigenval);
    separador = np.delete(eigv, (tmp), axis=1)[:,0];

    
    return separador;



X = np.array([[14.23,1065],[12.37,520],[13.20,1050],[12.33,680],[13.16,1185],[12.64,450],[14.37,1480],[13.67,630],[13.24,735],[12.37,420],[14.20,1450],[12.17,355],[14.39,1290],[12.37,678],[14.06,1295],[13.11,502],[14.83,1045],[12.37,510],[13.86,1045],[13.34,750],[14.10,1510],[12.21,718],[14.12,1280],[12.29,870],[13.75,1320],[13.86,410],[14.75,1150],[13.49,472],[14.38,1547],[12.99,985],[13.63,1310],[14.30,1280],[13.83,1130],[14.19,1680],[13.64,845]]
)
t = lda(X, np.array([[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1],[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]]
))
clf = LinearDiscriminantAnalysis()
clf.fit(X, y)
l = clf.coef_
l2 = clf.intercept_
