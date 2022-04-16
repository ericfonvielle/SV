%matplotlib qt
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.gridspec import GridSpec
import pandas as pd
import numpy as np

################################################################################
#FONCTION Update qui va permettre de modifier l'affichage de la régression
################################################################################
def update(val):
    '''
    Fonction qui permet d'actualiser la droite de modélisation et son équation,
     en fonction de la valeur du curseur
    '''
    T_regression = a.val*rcube_regression
    p.set_ydata(T_regression)
    equa.set_text('$T^2$ = %.2e $a^3$'%(a.val))
    
    ################################################################################
#LECTURE DU FICHIER de type csv
################################################################################
fichier='exo_13.csv'
Data = pd.read_csv(fichier, sep=';', header=0)

T = Data['T(s)']
r = Data['a(km)']
################################################################################
# Variables et régression linéaire moyenne
#Calcul des variable associée à la fonction
Tcarre = T**2
rcube = (r*1000)**3
# Calcul de la régression linéaire
regression = np.polyfit(rcube, Tcarre,1)
pente_moyenne=regression[0]
init_a=6.00e-14
#Variables pour la régression (on souhaite une droite passant par l'origine
rcube_regression=np.linspace(0,rcube[2]*2,5)
Tcarre_regression = init_a*rcube_regression

################################################################################
#Tracé de la courbe exprimentale et de la régression linéaire
################################################################################

G = GridSpec(15, 10)
fig, ax = plt.subplots(figsize=(15,10))
# Création d'une zone pour le graphique, amputée d'une ligne (:-2) pour y insérer le curseur
axes_1 = plt.subplot(G[:-2, :])
# Légende des axes, titre et gestion de la taille de la police
plt.xlabel('$r^3$ $(m^3)$', fontsize=16)
plt.ylabel('$T^2$ $(s^2)$', fontsize=16)
plt.title('$T^2 = f(r^3)$', fontsize=18)
plt.tick_params(labelsize=14)

plt.axis([0,max(rcube)*1.15,0,max(Tcarre)*1.15])
# Tracé des points de mesure
plt.scatter(rcube, Tcarre, s=50, color='r', marker='x',label='points expérimentaux')
equa = axes_1.text(max(rcube)*0.7,max(Tcarre)*0.15,'$T^2$ = %.2e $r^3$'%(init_a),
                   fontsize = 16, color="green", backgroundcolor = "#FFFF55")
# Affichage de l'équation de la droite de modélisation
p, = plt.plot(rcube_regression, Tcarre_regression, '-g',label='modélisation')
 # Affichage des légendes des graphiques
plt.legend(loc=2, fontsize=14)

plt.grid()
################################################################################
#Création d'un curseur.
################################################################################
rectangle_a = plt.axes([0.25, 0.1, 0.5, 0.02])
a = Slider(rectangle_a, 'coeff directeur',0,pente_moyenne*2, valinit=init_a)
# appel de la fonction update lorsque le curseur est actionné
a.on_changed(update)

plt.show()


