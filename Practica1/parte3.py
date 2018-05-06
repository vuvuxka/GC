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
    X1 = X[(t[0,:]==1),:];
    X2 = X[(t[1,:]==1),:];
    n = len(X[0,:]); "Dimensiones del subespacio inicial"
    k1 = np.sum(t[0,:]==1); "Número de elementos de clase 1"
    k2 = np.sum(t[1,:]==1); "Número de elementos de clase 2"
    
    "Calculamos las medias"
    
    m1 = np.mean(X1, axis=0);
    m2 = np.mean(X2, axis=0);
    m = np.mean(X, axis=0)
    
    "Calculamos las matrices de covarianzas"
    
    S_B = np.zeros((n,n));
    S_B = np.outer((m1-m2),(m1-m2))
    
    S_w1 = np.zeros((n,n));
    S_w2 = np.zeros((n,n));
    for x1 in X1:
        S_w1 += np.outer((x1-m1),(x1-m1).T);
    
    for x2 in X2:
        S_w2 += np.outer((x2-m2),(x2-m2).T);
    
      
    Sw = S_w1/4+S_w2/S_w2[0,0]*2.3;
    
    
    S = np.dot(np.linalg.inv(Sw),S_B);
    
    if np.linalg.det(S) == 0:
        return 0,0;
    
    eigenval, eigv = np.linalg.eig(S);
    
    tmp = np.argmin(eigenval);
    
    proyec = np.delete(eigv, (tmp), axis=1)[:,0]; "Recta sobre la que se proyecta"
    c = 0.5*(m1 + m2); "Punto separador de la recta"
    
    
    return proyec, c;



X = np.array([[4,2],[2,4],[2,3],[4,4],[3,6],[6,8],[8,7],[9,5],[9,10],[10,8]]
)
t = np.array([[1,1,1,1,1,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1]])
w = lda(X, t)
