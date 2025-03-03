import numpy as np

arr, valeur, unique, répétition = np.array([]), "", [], [] # Déclaration des variables

while valeur != "Q" and valeur != "q": # Boucle pour demander de l'information de l'utilisateur
    valeur = input("\nAjoute un chiffre dans un tableau numpy (Q/q pour quitter): ")
    
    while type(valeur) is not int and valeur != "Q" and valeur != "q": # Boucle pour vérifier que les donnés sont valides
        try:
            valeur = int(valeur)
        except:
            valeur = input("Entre une donnée valide: ")
            
    if valeur != "Q" and valeur != "q":
        arr = np.append(arr, valeur)
        print(f"Valeur {valeur} ajoutée. Tableau: {arr}")

for num in arr: # Boucle pour déterminer quels nombres sont uniques
    num = int(num)
    num = str(num)
    
    if len(num) == len(set(num)):
        unique.append(num)
    else:
        répétition.append(num)

arr.sort()
unique.sort()
répétition.sort()

print(f"\nIl y a {len(arr)} nombres dans la liste: {arr}\nIl y a {len(unique)} nombres dans la liste avec des chiffres uniques: {unique}\nIl y a {len(répétition)} nombres dans la liste avec des chiffres répétitifs: {répétition}")