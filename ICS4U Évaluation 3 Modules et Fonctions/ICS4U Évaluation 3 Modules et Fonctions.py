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
1 - Ajouter une marque de voiture et sa fréquence
2 - Supprimer toutes les marques et leurs fréquences
3 - Supprimer une marque et sa fréquence
4 - Trier les marques par ordre alphabétique
5 - Trier les marques par fréquence

Q - Quitter le programme

Choix: """)
    
    if strChoix == "1":
        tplValeurs = véhicule.ajouter(tblMarques, tblNombreMarques)
        if tplValeurs != False:
            tblMarques = tplValeurs[0]
            tblNombreMarques = tplValeurs[1]
    
    elif strChoix == "2":
        if len(lstMarques) == 0:
            print("\nLa liste est vide!")
        
        else:
            lstMarques = np.array([], dtype=str)
            print("\nListe supprimée!")

    elif strChoix == "3":
        pass

    elif strChoix == "4":
        pass

    elif strChoix == "5":
        pass

    elif strChoix == "q" or strChoix == "Q":
        print(f"\nListe finale: {véhicule.imprimer_tableau(tblMarques, tblNombreMarques)}\nAu revoir!")
    
    else: # Si l'utilisateur ne donne pas un nombre de 1-7, ou Q/q
        print("\nOption invalide")