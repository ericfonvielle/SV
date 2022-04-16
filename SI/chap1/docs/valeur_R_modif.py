# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 12:01:02 2021

@author: eric
"""
# Numpy permet de faire des calculs simples sur des arrays
import numpy as np  

# Matplotlib pour tracer des graphes
import matplotlib.pyplot as plt  

# Valeurs pointées de R(t)
R = np.array([1.0,1.1,1.2,1.3,1.3,1.1,0.9,0.8,1.3,1.4,1.0,1.2,1.2,1.1,0.9])  

# calcul de la valeur mesurée
R_val = np.mean(R) 
print(R_val)

 # incertitude-type (éval. type A) pour 48 mesures 
uR = np.std(R, ddof=1)/np.sqrt(15)  
print(uR)

print(f"R = {R_val} cm avec une incertitude u(R)={uR} cm")