"""Samuel Drake. Ce programme permet à l'utilisateur de gérer des noms de marques de voitures rares et insèrer le nombre de fois qu'ils ont vu ces marques. Pour accomplir ceci, il utilise 2 tableaux numpy."""

import numpy as np # Module numpy pour manipuler les données dans une liste
import véhicule
from time import sleep # Fonction sleep pour donner du temps à lire le texte

tblMarques = np.array([], dtype=str) # Création de les listes numpy
tblNombreMarques = np.array([], dtype=int)

print("""
Bienvenu au manipulateur de marques!

Ce programme vous permet de manipuler un tableau de marques de voitures rares
et d'indiquer le nombre de voitures de ces marques que vous avez déja vu
                                                         _________________________   
                    /\      _____           _____       |   |     |     |    | |  \  
     ,-----,       /  \____/__|__\_     ___/__|__\___   |___|_____|_____|____|_|___\ 
  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |   |
 ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  
`````````````````````````````````````````````````````````````````````````````````````
      """, end="") # La fonction end="" permet que la prochaine ligne de texte s'imprime sur la même ligne

strChoix = 0
while strChoix != "q" and strChoix != "Q":
    
    sleep(1)
    
    strChoix = input(f"""
Menu
--------
Liste: {véhicule.imprimer_tableau(tblMarques, tblNombreMarques)}
1 - Ajouter une nouvelle marque de voiture et sa fréquence
2 - Modifié la fréquence d'une marque
3 - Supprimer toutes les marques et leurs fréquences
4 - Supprimer une marque et sa fréquence
5 - Trier les marques par ordre alphabétique
6 - Trier les marques par fréquence (croissant)
7 - Trier les marques par fréquence (décroissant)

Q - Quitter le programme

Choix: """).lower()
    
    if strChoix == "1":
        tblMarques, tblNombreMarques = véhicule.ajouter(tblMarques, tblNombreMarques)
    
    elif strChoix == "2":
        tblMarques, tblNombreMarques = véhicule.modifier(tblMarques, tblNombreMarques)
    
    elif strChoix == "3":
        tblMarques, tblNombreMarques = véhicule.suprimer_toutes(tblMarques, tblNombreMarques)

    elif strChoix == "4":
        tblMarques, tblNombreMarques = véhicule.suprimer_une(tblMarques, tblNombreMarques)

    elif strChoix == "5":
        tblMarques, tblNombreMarques = véhicule.trier_alphabétique(tblMarques, tblNombreMarques)

    elif strChoix == "6":
        tblMarques, tblNombreMarques = véhicule.trier_fréquence_croissant(tblMarques, tblNombreMarques)
    
    elif strChoix == "7":
        tblMarques, tblNombreMarques = véhicule.trier_fréquence_décroissant(tblMarques, tblNombreMarques)

    elif strChoix == "q":
        print(f"\nListe finale: {véhicule.imprimer_tableau(tblMarques, tblNombreMarques)}\nAu revoir!")
    
    else: # Si l'utilisateur ne donne pas un nombre de 1-7, ou Q/q
        print("\nOption invalide")