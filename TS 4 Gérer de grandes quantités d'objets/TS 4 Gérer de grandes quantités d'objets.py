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
        print(f"\nJeux '{lstjeux[-1].strnom}' créer!")


################## Option 2 ##################

    elif str_choix == "2" and len(lstjeux) != 0:
        
        str_choix_modifier = input(f"\n{afficher(lstjeux)}\nEntrer le nom du jeux que vous voulez modifier les propriétés: ")
        while str_choix_modifier not in afficher(lstjeux):
            str_choix_modifier = input(f"\nOption invalide; entrer le nom du jeux que vous voulez modifier les propriétés: ")

        idx = afficher(lstjeux).index(str_choix_modifier)

        choix_propriété = input(f"""
{lstjeux[idx]}

Entrer la propriété à modifier:
    1. Le nom du jeux
    2. Le(s) developpeurs
    3. Le genre
    4. L'année de publication
    5. Les langues disponibles

Choix: """)
        
        if choix_propriété == "1":
            nouveau_nom = input(f"\nNom actuel: '{lstjeux[idx].strnom}'\nEntrer le noveau nom: ")
            lstjeux[idx].strnom = nouveau_nom
        
        elif choix_propriété == "2":
            ajouter_supprimer = input("\n1. Ajouter un developpeur\n2. Supprimer un developpeur\nChoix: ")
            
            if ajouter_supprimer == "1":
                developpeur = input("\nEntrer le nom du developpeur à ajouter: ")
                lstjeux[idx].ajout_objet_dev(developpeur)
                print(f"Developpeur {developpeur} ajouté.")
            
            elif ajouter_supprimer == "2":
                developpeur = input(f"\n{lstjeux[idx].lstdeveloppeur} Entrer le nom du developpeur à supprimer: ")
                lstjeux[idx].supp_objet_dev(developpeur)
                print(f"Developpeur {developpeur} supprimé.")
        
        elif choix_propriété == "3":
            ajouter_supprimer = input("\n1. Ajouter un genre\n2. Supprimer un genre\nChoix: ")
            
            if ajouter_supprimer == "1":
                genre = input("\nEntrer le nom du genre à ajouter: ")
                lstjeux[idx].ajout_objet_genre(genre)
                print(f"Genre {genre} ajouté.")
            
            elif ajouter_supprimer == "2":
                genre = input(f"\n{lstjeux[idx].lstgenre} Entrer le nom du genre à supprimer: ")
                lstjeux[idx].supp_objet_genre(genre)
                print(f"Genre {genre} supprimé.")
        
        elif choix_propriété == "4":
            loop = ""
            while loop != "false":
                try:
                    intnouveau_an = int(input("Quel est l'année de publication modifié : "))
                    if intnouveau_an < 0:
                        print("L'année de publication ne peut pas être un nombre négatif, ressayer.")
                    else:
                        lstjeux[idx].intannee = intnouveau_an
                        print(f"Année de publication modifiée à {intnouveau_an}")
                        loop = "false"
                except:
                    print("L'année de publication doit être un nombre entier, ressayer.")
        
        elif choix_propriété == "5":
            
            position = afficher(lstjeux).index(str_choix_modifier)
            print(f"Voici les languages disponibles pour le jeu vidéo {afficher(lstjeux)[position]} : {lstjeux[position].lstlangage}")
            while True:
                strchoix = input("Voulez vous supprimer ou ajouter un des langages disponibles? (supprimer/ajouter) ").lower()
                if strchoix == "supprimer":
                    print(len(lstjeux[position]))
                    x, y, z = len(lstjeux[position])
                    if z > 0:
                        while True:
                            strchoixsup = input("Quel langage veut tu supprimer? : ").lower()
                            positionsup = lstjeux[position].lstlangage.index(strchoixsup)
                            x, langage = lstjeux[position].lstlangage[positionsup]
                            if strchoixsup == langage:
                                lstjeux[position].lstlangage[positionsup].sup_objet_dev(strchoixsup)
                                break
                            else:
                                print(f"Le jeu vidéo {strchoixsup} n'est pas un jeu qui a été créer, ressayer.")
                            break
                    else:
                        print("Il n'y a aucun langue disponible à supprimer.")
                          
                elif strchoix == "ajouter":
                    while True:
                        strchoixajou = input("Quel langage veux-tu ajouter? : ").lower()
                                
                        if strchoixajou not in lstjeux[position].lstlangage:
                            lstjeux[position].lstlangage.append(strchoixajou)
                            break
                        else:
                            print(f"La langue {strchoixajou} a déjà été créer, ressayer.")
                    break
                else:
                    print("Entrer soit supprimer ou ajouter, ressayer.")
                
        
        else:
            print("Choix invalide")


################## Option 3 ##################

    elif str_choix == "3" and len(lstjeux) != 0:
        
        str_choix_afficher = input(f"\nListe de jeux: {afficher(lstjeux)}\nEntrer un nom de jeu vidéo pour voir ses propriétés: ")
        while str_choix_afficher not in afficher(lstjeux):
            str_choix_afficher = input(f"Option invalide. Entrer un nom de jeu vidéo pour voir ses propriétés: ")
        
        idx = afficher(lstjeux).index(str_choix_afficher)
        print(f"\nNom: '{lstjeux[idx].strnom}'\nDeveloppeur(s): {lstjeux[idx].lstdeveloppeur}\nGenre: {lstjeux[idx].lstgenre}\nAnnée de publication: {lstjeux[idx].intannee}\nLangues disponibles: {lstjeux[idx].lstlangage}")


################## Option 4 ##################

    elif str_choix == "4" and len(lstjeux) != 0:
        
        loop = ""
        while loop != "false":
            nom = input(f"\nListe de jeux: {afficher(lstjeux)}\nEntrer le nom du jeu que tu veux supprimer : ")
            try:
                lstjeux.pop(afficher(lstjeux).index(nom))
                loop = "false"
                print(f"\nLe jeu vidéo '{nom}' a été supprimé.")
            except:
                print(f"Le jeu vidéo '{nom}' n'existe pas, ressayer.")


################## Autres ##################

    elif str_choix != "q" and len(lstjeux) == 0:
        print("Créer un objet avant d'utiliser cette fonction!")
        
    elif str_choix == "q":
        print("\nAu revoirs!")
    
    else:
        print("\nOption invalide.")