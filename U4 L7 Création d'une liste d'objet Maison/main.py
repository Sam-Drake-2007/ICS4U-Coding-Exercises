# U4 L7 Création d'une liste d'objet Maison

from maison import Maison

lstM = []
i = 0

continuer = ""
while continuer != "q":

    prix = input("Prix de la maison: ")
    while type(prix) is not int:
        try:
            prix = int(prix)
            if prix < 0:
                prix = input("Prix invalide, essayer à nouveau: ")
        except:
            prix = input("Prix invalide, essayer à nouveau: ")
    lstM.append(Maison(prix))
    
    item = ""
    while item != "q":
        item = input("Item à ajouter à l'inventaire ou q pour quitter: ").lower()
        if item != "q":
            lstM[i].ajout_objet(item)
            
    print(f"\nVoici les détails de la maison\n{lstM[i]}\nIl y a {len(lstM[i])} item(s) dans l'inventaire. Les voici:")
    for item in lstM[i]:
        print(item)
    
    continuer = input("\nEnter pour ajouter d'autres données, q pour quitter: ").lower()
    i += 1