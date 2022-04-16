################################################################################
# CHAPITRE 2: AE.2B
################################################################################
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt

################################################################################
# Lecture du fichier et création des variables
################################################################################
#nom du fichier à traiter
fichier=input("Quel est le nom du fichier de pointage (sans l'extension .csv)?")+".csv"

Data = pd.read_csv(fichier, sep=',', header=0)

t=Data['Temps']
x=Data['X']
y=Data['Y']

################################################################################
#Calcul des coordonnées Vx et Vy des vecteurs vitesse
################################################################################
Vx=[(x[i+1]-x[i])/(t[i+1]-t[i]) for i in range(len(x)-1)]
Vy=[(y[i+1]-y[i])/(t[i+1]-t[i]) for i in range(len(y)-1)]
V=[(sqrt(Vx[i]**2+Vy[i]**2)) for i in range(len(Vx))]

#masse du système en kg
m=0.60
#intensité de la pesanteur
g=9.81

#Calcul des énergies
Ep=[(m*g*y[i]) for i in range(len(Vx))]
Ec=[]
Em=[(Ep[i]+Ec[i]) for i in range(len(Vx))]


################################################################################
# Taille du graphique
################################################################################
plt.figure(figsize=(15,12))

################################################################################
# Sous figure inférieure
################################################################################
plt.subplot(212)
X_max=max(x)
plt.ylim([0,1.1*X_max])
plt.xlim([0,t.max()])

#tracé de la position
plt.plot(t,x,'bo')

#Légendes
plt.title("Évolution de la position X du système", fontsize =16)
plt.ylabel('X (m)', fontsize =16)
plt.xlabel('$t$ (s)', fontsize =16)
plt.tick_params(labelsize=16)
#Parametres de la grille
ax = plt.gca()
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.7', color='black')
ax.grid(which='minor', linestyle='-', linewidth='0.5', color='black')

################################################################################
# Sous figure supérieure
################################################################################
plt.subplot(211)
Em_max=max(Em)
plt.ylim([0,1.5*Em_max])
plt.xlim([0,t.max()])

#tracé des énergies
plt.plot(t[0:-1],Ep,'ro',label='Énergie potentielle de pesanteur')
plt.plot(t[0:-1],Ec,'go',label='Énergie cinétique')
plt.plot(t[0:-1],Em,'ko',label='Énergie mécanique')

#Légendes
plt.title("Évolution des énergies au cours du temps", fontsize =16)
plt.ylabel(r'$\mathcal{E}$ (J)', fontsize =16)
plt.xlabel('$t$ (s)', fontsize =16)
plt.tick_params(labelsize=16)
#Parametres de la grille
ax = plt.gca()
ax.minorticks_on()
ax.grid(which='major', linestyle='-', linewidth='0.7', color='black')
ax.grid(which='minor', linestyle='-', linewidth='0.5', color='black')

#Pour faire apparaitre les légendes retirer le # devant la ligne suivante.
plt.legend(loc=2)

# Ajustement du plot
plt.subplots_adjust(hspace=0.5)

#Sauvegarde des courbes
plt.savefig("Energies.png")


plt.show()
