import numpy as np

tableau = np.array([], dtype=str)
choix = "1"

while choix == "1" or choix == "2" or choix == "3" or choix == "4":
    choix = input("\n1: Ajouter un mot dans un tableau numpy\n2: Compter le nombre de mots dans le tableau\n3: Calculer la moyenne du nombre de caractères des mots dans le tableau\n4: Enlever un mot du tableau\nQ: Quitter le programme\nRéponse: ")
    
    if choix == "1":
        valeur = input("Entre le mot: ")
        while not valeur.isalpha():
            valeur = input("Entre un mot valide: ")
        
        tableau = np.append(tableau, valeur)
        print(f"Mot {valeur} ajouté. Nouveau tableau: {tableau}")
    
    elif choix == "2":
        print(f"Le tableau: {tableau} contient {len(tableau)} mots.")

    elif choix == "3":
        if len(tableau) == 0:
            print("Le tableau est vide!")
        else:
            count = 0
            for t in tableau:
                count += len(t)
            print(f"La moyenne du nombre de caractères des mots dans le tableau {tableau} est {count / len(tableau)}")
    
    elif choix == "4":
        remove = input(f"Entrer l'indexe du mot que vous voulez enlever {tableau}: ")
        try:
            remove = int(remove)
            tableau = np.delete(tableau, remove)
            print(f"Mot à l'indexe {remove} enlevé. Nouveau tableau: {tableau}")
        except:
            print("Indexe invalide")            