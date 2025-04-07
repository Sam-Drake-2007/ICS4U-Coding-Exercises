import numpy as np

def imprimer_tableau(noms, valeurs): # Fonction pour imprimer les données des deux tableaux d'une manière claire en utilisant un dictionnaire
    dctNoms = {}
    for i in range(len(noms)):
        dctNoms[str(noms[i])] = int(valeurs[i])
    return dctNoms

def ajouter(tableau_noms, tableau_fréquence):
    tblBanqueMarques = np.array([
        ["Apollo", "Bugatti", "Ferrari"],
        ["Jaguar", "Koenigsegg", "Lamborghini"],
        ["Maserati", "Mercedes", "Pagani"],
        ["Porsche", "Rimac", "Zenvo"],
                        ])
    print(f"\nVoici la banque de marques:\n\n{tblBanqueMarques}")
    strMarque = input("\nEntrer la marque à ajouter (Q - Retour au menu): ")
    strMarque = strMarque.lower().capitalize() 
    # Ses méthodes assurent que la donnée de l'utilisateur aura une paire dans la banque de marques si elle est valide

    while strMarque != "Q" and strMarque not in tblBanqueMarques: # La condition pour une réponse invalide
        strMarque = input("\nEntrer une marque valide (Q - Retour au menu): ")
        strMarque = strMarque.lower().capitalize()
    
    if strMarque != "Q": # Le programme doit juste vérifier pour le Q majuscule grâce à la méthode "capitalize()"
        intFréquence = input("\nEntrer le nombre de fois que vous avec vu cette marque (Q - Retour au menu): ")
        
        while intFréquence != "Q" and intFréquence != "q" and type(intFréquence) is not int:
            try:
                intFréquence = int(intFréquence)
                if intFréquence < 0: # La marque peut quand même être ajoutée si jamais vue, pour un genre de marque de rêve à voir
                    intFréquence = input("\nEntrer une fréquence valide (Q - Retour au menu): ")
                    
            except:
                intFréquence = input("\nEntrer une fréquence valide (Q - Retour au menu): ")
    
        if intFréquence != "Q" and intFréquence != "q":
            print(f"\nMarque {strMarque} enregistrée avec une fréquence de {intFréquence}")
            tableau_noms = np.append(tableau_noms, strMarque)
            tableau_fréquence = np.append(tableau_fréquence, intFréquence)
        
        return tableau_noms, tableau_fréquence