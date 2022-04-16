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
R = np.array([0.08764,0.0880,0.08776,0.08749,0.08705,0.08667,0.08745,0.08794,0.08868,0.08855,0.08983,0.08918,0.08905,0.08937,0.08859,0.08936,0.09014,0.09011,0.09087,0.08983,0.08848,0.09049,0.09095,0.09055,0.09143,0.09057,0.09031,0.09169,0.09086,0.09149,0.09137,0.09121,0.09109,0.09115,0.09067,0.09164,0.09091,0.09055,0.09095,0.09009,0.0913,0.08991,0.0909,0.08967,0.08971,0.08872,0.09009,0.08886
])  

# calcul de la valeur mesurée
R_val = np.mean(R) 
print(R_val)

 # incertitude-type (éval. type A) pour 48 mesures 
uR = np.std(R, ddof=1)/np.sqrt(48)  
print(uR)

print(f"R = {R_val} cm avec une incertitude u(R)={uR} cm")