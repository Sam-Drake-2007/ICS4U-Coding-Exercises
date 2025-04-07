import numpy as np # Module numpy pour manipuler les données dans une liste
from time import sleep # Fonction sleep pour donner du temps à lire le texte

lstMarques = np.array([], dtype=str) # Création de la liste numpy
lstBanqueMarques = np.array([
    ["Audi", "Bmw", "Bugatti"],
    ["Cadillac", "Chevrolet", "Chrysler"],
    ["Dodge", "Ferrari", "Fiat"],
    ["Ford", "Honda", "Hyundai"],
    ["Jaguar", "Jeep", "Koenigsegg"],
    ["Lamborghini", "Maserati", "Mazda"],
    ["Mercedes", "Mitsubishi", "Nissan"],
    ["Porsche", "Subaru", "Toyota"],
    ["Tesla", "Volkswagen", "Volvo"]
                    ])

print("""
Bienvenu au manipulateur de marques!

Ce programme te permet de manipuler une liste contenant des noms de 
marques de voitures les plus populaires (Toyota, BMW, Nissan, etc.)

                                                         _________________________   
                    /\      _____           _____       |   |     |     |    | |  \  
     ,-----,       /  \____/__|__\_     ___/__|__\___   |___|_____|_____|____|_|___\ 
  ,--'---:---`--, /  |  _     |     `| |      |      `| |                    | |   |
 ==(o)-----(o)==J    `(o)-------(o)=   `(o)------(o)'   `--(o)(o)--------------(o)--'  
`````````````````````````````````````````````````````````````````````````````````````
      """, end="") # La fonction end="" permet que la prochaine ligne de texte s'imprime sur la même ligne

sleep(2)

strChoix = 0
while strChoix != "q" and strChoix != "Q":
    strChoix = input(f"""
Menu
--------
Liste: {lstMarques}
1 - Ajouter une marque de voiture
2 - Supprimer toutes les marques de voitures
3 - Supprimer une marque de voiture
4 - Trier les marques par ordre alphabétique
5 - Calculer la moyenne de la longeur des marques
6 - Supprimer les marques qui se répètent
7 - Compter les marques

Q - Quitter le programme

Choix: """)
    
    if strChoix == "1":
        print(f"\nVoici la banque de marques:\n\n{lstBanqueMarques}")
        strMarque = input("\nEntrer la marque à ajouter (Q - Retour au menu): ")
        strMarque = strMarque.lower().capitalize() 
        # Ses méthodes assurent que la donnée de l'utilisateur aura une paire dans la banque de marques si elle est valide

        while strMarque != "Q" and strMarque not in lstBanqueMarques: # La condition pour une réponse invalide
            strMarque = input("\nEntrer une marque valide (Q - Retour au menu): ")
            strMarque = strMarque.lower().capitalize()
        
        if strMarque != "Q": # Le programme doit juste vérifier pour le Q majuscule grâce à la méthode "capitalize()"
            lstMarques = np.append(lstMarques, strMarque)
            print(f"\nMarque '{strMarque}' enregistrée")
                
        sleep(1)
            
    
    elif strChoix == "2":
        if len(lstMarques) == 0:
            print("\nLa liste est vide!")
        
        else:
            lstMarques = np.array([], dtype=str)
            print("\nListe supprimée!")
        
        sleep(1)
        
    elif strChoix == "3":
        if len(lstMarques) == 0:
            print("\nLa liste est vide!")
            
        else:
            strIndexe = input(f"\nEntrer l'indexe de la marque à supprimer {lstMarques} (Q - Retour au menu): ")
        
            while type(strIndexe) is not int and strIndexe != "q" and strIndexe != "Q":
                try:
                    strIndexe = int(strIndexe)
                    lstMarques = np.delete(lstMarques, strIndexe) # Le programme va continuer au except si l'utilisateur donne un indexe trop grand ou petit
                    print(f"\nMarque à l'indexe {strIndexe} supprimée")
                except:
                    strIndexe = input("\nEntrer un indexe valide (Q - Retour au menu): ")
        
        sleep(1)
        
    elif strChoix == "4":
        if len(lstMarques) == 0:
            print("\nLa liste est vide!")
        
        else:
            lstMarques = np.sort(lstMarques) # Fonction qui trie les éléments par ordre alphabétique
            print(f"\nListe triée: {lstMarques}")
        
        sleep(1)
        
    elif strChoix == "5":
        intCount = 0 # Le compte total des lettres
        for marque in lstMarques:
            intCount += len(marque)

        if len(lstMarques) == 0:
            print("\nLa liste est vide!")
        
        else:
            print(f"\nLa moyenne de la longeur des marques est {round(intCount / len(lstMarques), 2)}")
        
        sleep(1)
        
    elif strChoix == "6":
        if len(lstMarques) == 0:
            print("\nLa liste est vide!")
        
        else:
            lstMarques = np.array(list(set(lstMarques.tolist())), dtype=str)
            # Conversion de la liste numpy à une liste normale pour la convertir à un set (pas de répétitions), 
            # ensuite la convertir encore à une liste pour finalement la reconvertir à une liste numpy
            
            print(f"\nMarques qui se répètent supprimées")
        
        sleep(1)
        
    elif strChoix == "7":        
        if len(lstMarques) == 0:
            print("\nLa liste est vide!")
            
        else:
            lstMarquesUniques = list(set(lstMarques.tolist())) # Marques uniques dans la liste de marques
            print("")
            
            for marque in lstMarquesUniques:
                print(f"{marque}: {int((lstMarques == marque).sum())}") # Fonction pour avoir le nombre de répétitions dans la liste
        
        sleep(1)
        
    elif strChoix == "q" or strChoix == "Q":
        print(f"\nListe finale: {lstMarques}\nAu revoir!")
    
    else: # Si l'utilisateur ne donne pas un nombre de 1-7, ou Q/q
        print("\nOption invalide")
        sleep(1)