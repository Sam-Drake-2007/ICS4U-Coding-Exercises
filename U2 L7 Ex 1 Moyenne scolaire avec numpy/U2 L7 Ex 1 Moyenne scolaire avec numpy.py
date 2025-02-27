import numpy as np

tableau = np.array([])
choix = ""

while choix != "Q" and choix != "q":
    choix = input("\n1: Ajoute une note scolaire dans un tableau numpy\n2: Effacer toutes les notes du tableau\n3: Calcule la moyenne\n4: Afficher le contenu du tableau\nQ: Quitter le programme\nRéponse: ")
    
    if choix == "1":
        valeur = input("Entre la valeur de la note scholaire: ")
        
        while type(valeur) is not int or valeur < 0 or valeur > 100:
            try:
                valeur = int(valeur)
                if valeur < 0 or valeur > 100:
                    valeur = input("Entre une donnée valide: ")
            except:
                if valeur == "Q" or valeur =="q":
                    exit()
                else:
                    valeur = input("Entre une donnée valide: ")
        
        tableau = np.append(tableau, valeur)
    
    elif choix == "2":
        tableau = np.array([])

    elif choix == "3":
        if not len(tableau):
            print("Le tableau est vide!")
        else:
            moyenne = round(np.average(tableau), 2)
            print(f"La moyenne des notes actuelle est: {moyenne}")
    
    elif choix == "4":
        tableau.sort()
        print(tableau)
    
    else:
        print("Entre une réponse valide (1, 2, 3, 4, Q)")