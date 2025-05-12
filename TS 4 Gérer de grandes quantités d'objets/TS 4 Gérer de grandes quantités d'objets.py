"""Samuel Drake et Nicolas Bennett. Ce programme permet à l'utilisatuer de manipuler des objets sous la forme de jeux-vidéos. Chaque objet contient plusieurs propriétés qui peuvent être modifiés. Ce programme accomplit ceci en utilisant la programmation orientée objet."""

from time import sleep
from jeu import jeu
        
def afficher(lst):
    return [jeu.strnom for jeu in lst]

lstjeux = []

print("""
Bienvenu à JV documentation!

Ce programme vous permet de documenter de l'information pertinente sur les jeux vidéos incluant:
    1. Le nom du jeu
    2. Les developpeurs
    3. Le genre
    4. L'année de publication
    5. Les languages disponibles""")


################## Menu ##################

str_choix = ""
while str_choix != "q":
    
    sleep(1)
    
    str_choix = input(f"""
Menu
--------
Jeux vidéos: {afficher(lstjeux)}

1 - Créer un jeu vidéo
2 - Modifié les propriétés d'un jeu vidéo
3 - Afficher les propriétés d'un jeu vidéo
4 - Supprimer un jeu vidéo

Q - Quitter le programme

Choix: """).lower()

################## Option 1 ##################

    if str_choix == "1":
        
        strnom = input("Entrer le nom du jeux: ")
        lstjeux.append(jeu(strnom))
        print(f"Jeux '{lstjeux[-1].strnom}' ajoutée!")


################## Option 2 ##################

    elif str_choix == "2":
        
        str_choix_modifier = input(f"\n{afficher(lstjeux)}\nEntrer le nom du jeux que vous voulez modifier les propriétés: ")
        while str_choix_modifier not in afficher(lstjeux):
            str_choix_modifier = input(f"\nOption invalide; entrer le nom du jeux que vous voulez modifier les propriétés: ")
            
        choix_propriété = input(f"""
Jeux: {str_choix_modifier}
Entrer la propriété à modifier:
    1. Le nom du jeux
    2. Le(s) developpeurs
    3. Le genre
    4. L'année de publication
    5. Les langues disponibles""")


################## Option 3 ##################

    elif str_choix == "3":
        
        str_choix_afficher = input(f"\n{afficher(lstjeux)}\nEntrer le nom du jeux que vous voulez voir les propriétés: ")
        while str_choix_afficher not in afficher(lstjeux):
            str_choix_afficher = input(f"\nOption invalide; entrer le nom du jeux que vous voulez voir les propriétés: ")
        
        idx = afficher(lstjeux).index(str_choix_afficher)
        print(f"""
Nom: {lstjeux[idx].strnom}
Developpeur(s): {lstjeux[idx].lstdeveloppeur}
Genre: {lstjeux[idx].strgenre}
Année de publication: {lstjeux[idx].intannee}
Langues disponibles: {lstjeux[idx].lstlangage}""")


################## Option 4 ##################

    elif str_choix == "4":
        
        loop = ""
        while loop != "false":
            nom = input(f"\n{afficher(lstjeux)}\nEntrer le nom du jeu que tu veux supprimer : ")
            try:
                lstjeux.pop(afficher(lstjeux).index(nom))
                loop = "false"
                print(f"\nLe jeu vidéo {nom} a été supprimé.")
            except:
                print(f"\nLe jeu vidéo {nom} n'existe pas, ressayer.")


################## Autres ##################

    elif str_choix == "q":
        print("\nAu revoirs!")
    
    else:
        print("\nOption invalide.")