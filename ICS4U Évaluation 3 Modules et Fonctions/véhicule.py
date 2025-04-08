import numpy as np

def imprimer_tableau(noms, valeurs): # Fonction pour imprimer les données des deux tableaux d'une manière claire en utilisant un dictionnaire
    dctNoms = {}
    for i in range(len(noms)):
        dctNoms[str(noms[i])] = int(valeurs[i]) # Prend le nom come "key" et la fréquence comme "value"
    return dctNoms

def ajouter(tableau_noms, tableau_fréquence):
    """Cette fonction permet à l'utilisateur d'ajouter une marque et sa fréquence dans les tableaux"""
    
    tblBanqueMarques = np.array([
        ["Apollo", "Bugatti", "Ferrari"],
        ["Jaguar", "Koenigsegg", "Lamborghini"],
        ["Maserati", "Mercedes", "Pagani"],
        ["Porsche", "Rimac", "Zenvo"],
                        ])
    strMarque = input(f"\nVoici la banque de marques:\n\n{tblBanqueMarques}\n\nEntrer une nouvelle marque à ajouter (Q - Retour au menu): ").lower().capitalize()
    # Ses méthodes assurent que la donnée de l'utilisateur aura une paire dans la banque de marques si elle est valide

    while strMarque not in tblBanqueMarques or strMarque in tableau_noms: # La condition pour une réponse invalide
        if strMarque == "Q": # Le programme doit juste vérifier pour le Q majuscule grâce à la méthode "capitalize()"
            return tableau_noms, tableau_fréquence
        
        strMarque = input("\nEntrer une nouvelle marque valide (Q - Retour au menu): ").lower().capitalize()
    
    intFréquence = input("\nEntrer le nombre de fois que vous avec vu cette marque (Q - Retour au menu): ").capitalize()
    while type(intFréquence) is not int:
        if intFréquence == "Q":
            return tableau_noms, tableau_fréquence
        
        try:
            intFréquence = int(intFréquence)
            if intFréquence < 0: # La marque peut quand même être ajoutée si jamais vue, pour un genre de marque de rêve à voir
                intFréquence = input("\nEntrer une fréquence valide (Q - Retour au menu): ")
        except:
            intFréquence = input("\nEntrer une fréquence valide (Q - Retour au menu): ")
    
    print(f"\nMarque {strMarque} enregistrée avec une fréquence de {intFréquence}")
        
    return np.append(tableau_noms, strMarque), np.append(tableau_fréquence, intFréquence)

def modifier(tableau_noms, tableau_fréquence):
    """Cette fonction permet de modifier la fréquence d'une marque"""
    
    marque = input(f"\n{imprimer_tableau(tableau_noms, tableau_fréquence)}\nEntrer le nom de la marque à entrer une nouvelle fréquence (Q - Retour au menu): ").lower().capitalize()
    while marque not in tableau_noms:
        if marque == "Q":
            return tableau_noms, tableau_fréquence
        
        marque = input(f"\nEntrer une marque valide (Q - Retour au menu): ").lower().capitalize()
    
    nouvelle_fréquence = input(f"\nEntrer la nouvelle fréquence de la marque '{marque}': ")
    while type(nouvelle_fréquence) is not int:
        if marque == "Q":
            return tableau_noms, tableau_fréquence
        try:
            nouvelle_fréquence = int(nouvelle_fréquence)
            if nouvelle_fréquence < 0:
                nouvelle_fréquence = input(f"\nEntrer une fréquence valide (Q - Retour au menu): ")
        except:
            nouvelle_fréquence = input(f"\nEntrer une fréquence valide (Q - Retour au menu): ")
    
    tableau_fréquence[np.where(tableau_noms == marque)] = nouvelle_fréquence
    
    return tableau_noms, tableau_fréquence
    
def suprimer_toutes(tableau_noms, tableau_fréquence):
    """Cette fonction suprime toutes les données dans les tableaux numpy"""
    
    if len(tableau_noms) == 0:
        print("\nLe tableau est vide.")
        return tableau_noms, tableau_fréquence
    
    print("\nLe tableau a été suprimé.")
    return np.array([], dtype=str), np.array([], dtype=int)

def suprimer_une(tableau_noms, tableau_fréquence):
    """Cette fonction suprime une marque et sa fréquence dans le tableau numpy"""
    
    if len(tableau_noms) == 0:
        print("\nLa liste est vide!")
        return tableau_noms, tableau_fréquence
            
    marque = input(f"\n{imprimer_tableau(tableau_noms, tableau_fréquence)}\nEntrer le nom de la marque à supprimer (Q - Retour au menu): ").lower().capitalize()
    while marque not in tableau_noms:
        if marque == "Q":
            return tableau_noms, tableau_fréquence
        
        marque = input("\nEntrer une nouvelle marque valide (Q - Retour au menu): ").lower().capitalize()
    
    return np.delete(tableau_noms, np.where(tableau_noms == marque)), np.delete(tableau_fréquence, np.where(tableau_noms == marque))

def trier_alphabétique(tableau_noms, tableau_fréquence):
    """Cette fonction trie le tableau numpy en ordre alphabétique"""
    
    indices = np.argsort(tableau_noms) # La fonction argsort donne les indexes du tableau en ordre croissant
    return tableau_noms[indices], tableau_fréquence[indices] # Les ordres des tableaux sont changés pour être celle des indexes triées

def trier_fréquence_croissant(tableau_noms, tableau_fréquence):
    """Cette fonction trie le tableau numpy par sa fréquence en ordre croissant"""
    
    indices = np.argsort(tableau_fréquence) 
    return tableau_noms[indices], tableau_fréquence[indices] 

def trier_fréquence_décroissant(tableau_noms, tableau_fréquence):
    """Cette fonction trie le tableau numpy par sa fréquence en ordre décroissant"""

    indices = np.argsort(tableau_fréquence)[::-1]
    return tableau_noms[indices], tableau_fréquence[indices]