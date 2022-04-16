" Programme permettant de déterminer la contribution d'un paramètre à l'incertitude composée d'un rendement par simulation "


# importation des bibliothèques utiles #

" pour générer les valeurs aléatoires "
import numpy as np


# définition des fonctions pour l'étude statistique #

" fonction retournant une liste de 1000 valeurs aléatoires de valeur moyenne et d'incertitude connus "
def tirage(moyenne, Incertitude):
    L = np.random.normal(moyenne, Incertitude, 1000)
    return(L)

" fonction retournant la moyenne d'une liste de valeurs " 
def moy(L) :
    vmoy = sum(L)/len(L)
    return(vmoy)

" fonction retournant l'écart type d'une liste de valeurs "
def incertitude(L):
    somme_carres_ecarts = 0
    for i in range(0, len(L)):
        somme_carres_ecarts = somme_carres_ecarts + (L[i]-moy(L))**2
    Ur = (somme_carres_ecarts/(len(L)-1))**0.5
    return(Ur)

# demande les valeurs utiles concernant le paramètre choisi #

moyenne = float(input("valeur du paramètre choisi = "))
Incertitude = float(input("incertitude sur la valeur du paramètre choisi = "))


#######################
# programme principal #
#######################

" tirage de la liste de valeurs pour le paramètre choisi"
symbole_du_parametre = tirage(moyenne, Incertitude)

" calculs des valeurs du rendement pour chaque valeur du paramètre choisi "
liste_r = []
for i in range(0,len(symbole_du_parametre)) :
    r = formule
    " les valeurs de r sont ajoutés à la liste "
    liste_r.append(r)

# étude statistique de la liste des valeurs de r #

moyenne = moy(liste_r)
Ur = incertitude(liste_r)


# affichage des résultats #

print("Résultats de la simulation :")
print("valeur moyenne du rendement = ",moyenne)
print("incertitude sur la valeur du rendement = ",Ur)


