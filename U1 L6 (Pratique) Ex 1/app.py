# Module qui permet de donnés des valeurs alléatoires

import random

# Boucle pour permettre de recommencer le programme

while True:
    
    # Input pour receuillir des donnés de l'utilisateur

    poules = input("Entrer le nombre de poules: ")

    # Boucle pour vérifier que les données sont valides

    while type(poules) != int:
        try:
            poules = int(poules)
        except:
            poules = input("Entrer un nombre de poules valide: ")
        
        if type(poules) == int and poules < 0:
            poules = input("Entrer un nombre de poules valide: ")

    vache = input("Entrer le nombre de vaches: ")

    while type(vache) != int:
        try:
            vache = int(vache)
        except:
            vache = input("Entrer un nombre de poules valide: ")
        
        if type(vache) == int and vache < 0:
            vache = input("Entrer un nombre de poules valide: ")
            
    chevaux = input("Entrer le nombre de chevaux: ")

    while type(chevaux) != int:
        try:
            chevaux = int(chevaux)
        except:
            chevaux = input("Entrer un nombre de poules valide: ")
        
        if type(chevaux) == int and chevaux < 0:
            chevaux = input("Entrer un nombre de poules valide: ")
            
    total = (poules * 2) + (vache * 4) + (chevaux * 4)

    print(f"Le nombre total de jambes est: {total}")
    
    # Calculs pour déterminer le nombre d'animaux de chaque catégorie
    
    chevache = total // 4
    pou = (total - (4 * chevache)) / 2
    chev = random.randint(0, chevache)
    vach = chevache - chev
    
    print(f"Avec ce nombre de pattes ({total}), la combinaison aurai pu être: {int(pou)} poules, {chev} chevaux et {vach} vaches.")
    
    r = input("Recommencer le programme? (o/n): ")
    
    if r != "o":
        break