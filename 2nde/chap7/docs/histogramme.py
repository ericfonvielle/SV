from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt

#on peut donner le chemin d'accès vers le fichier ou la fonction askopenfilename
root = Tk()
name = askopenfilename(parent = root, filetypes =(("Fichier CSV", "*.csv"),("Fichier Texte","*.txt"),("Tous les fichiers","*.*")),title = "Choisir un fichier")
root.destroy()

sep = ";" #caractère séparateur du csv -peut être une virgule, un point-virgule ou une tabulation noté \t 
entete = 1 #nombre de lignes d'entete

f = open(name,"r")
data = f.readlines() #on lit toutes les lignes et on met ça dans une liste -un élément par ligne-
f.close() #on referme le fichier

data = data[ entete : ] #on supprime les lignes d'en-tête qui ne nous intéressent pas

#on construit les listes de valeurs utiles
t = []

for ligne in data:
    ligne = ligne.replace("," , ".") #change les virgules en point => format numérique différent sur excel et sur python
    ligne = ligne.strip().split(sep) #on sépare les différents élément en utilisant le caractère séparateur défini
    ligne = list(map(float,ligne)) #on converti chaque élément en flottant
    #on rentre les valeurs dans les lites adaptées
    t.append(ligne[0]) 


    
plt.hist(t,bins=20,rwidth=0.95)


plt.show()