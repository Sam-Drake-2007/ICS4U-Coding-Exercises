import rectangle

obj_rectangle = rectangle.rec(0, 0)

str_choix = ""
while str_choix != "q":
    
    str_choix = input(f"""
Menu
--------
Dimentions du rectangle: {[obj_rectangle.getbase(), obj_rectangle.gethauteur()]}

1 - Créer le rectangle
2 - Modifier la base du rectangle
3 - Modifier la hauteur du rectangle
4 - Calculer le périmètre du rectangle
5 - Calculer l'aire du rectangle
6 - Calculer la somme des angles intérieurs du rectangle
7 - Vérifier si le rectangle est un carré

Q - Quitter le programme

Choix: """).lower()
    
    if str_choix == "1":
        
        int_base = input("Entrer la longueur de la base du rectangle: ")
        while type(int_base) is not int:
            try:
                int_base = int(int_base)
                if int_base <= 0:
                    int_base = input("Entrer une longueur de base plus grand que 0: ")
            except:
                int_base = input("Entrer une longueur de base valide: ")

        int_hauteur = input("Entrer la longueur de la hauteur du rectangle: ")
        while type(int_hauteur) is not int:
            try:
                int_hauteur = int(int_hauteur)
                if int_hauteur <= 0:
                    int_hauteur = input("Entrer une longueur de hauteur plus grand que 0: ")
            except:
                int_hauteur = input("Entrer une longueur de hauteur valide: ")
        
        obj_rectangle = rectangle.rec(int_base, int_hauteur)
    
    
    elif str_choix == "2":
        
        int_base = input("Entrer la nouvelle longueur de la base du rectangle: ")
        while type(int_base) is not int:
            try:
                int_base = int(int_base)
                if int_base <= 0:
                    int_base = input("Entrer une nouvelle longueur de base plus grand que 0: ")
            except:
                int_base = input("Entrer une nouvelle longueur de base valide: ")
        
        obj_rectangle.setbase(int_base)
    
    
    elif str_choix == "3":
        
        int_hauteur = input("Entrer la nouvelle longueur de la hauteur du rectangle: ")
        while type(int_hauteur) is not int:
            try:
                int_hauteur = int(int_hauteur)
                if int_hauteur <= 0:
                    int_hauteur = input("Entrer une nouvelle longueur de hauteur plus grand que 0: ")
            except:
                int_hauteur = input("Entrer une nouvelle longueur de hauteur valide: ")
        
        obj_rectangle.sethauteur(int_hauteur)
    
    
    elif str_choix == "4":
        print(f"Le périmètre est de {obj_rectangle.perimetre()} unités.")
        
    elif str_choix == "5":
        print(f"L'aire du rectangle est de {obj_rectangle.aire()} unités carrées.")

    elif str_choix == "6":
        if obj_rectangle.getbase() == 0 or obj_rectangle.gethauteur() == 0:
            print("Le carré n'a pas d'angles intérieurs!")
        else:
            print(f"La somme des angles intérieurs est de {obj_rectangle.somme_angles_interieurs()} degrés.")

    elif str_choix == "7":
        if obj_rectangle.estcarre() == True and obj_rectangle.getbase() != 0 and obj_rectangle.gethauteur() != 0:
            print("Le rectangle est un carré!")
        else:
            print("Le rectangle n'est pas un carré!")