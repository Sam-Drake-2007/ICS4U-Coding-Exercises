import numpy as np

noms = np.array([], dtype=str)
notes = np.array([], dtype=int)

choix = "1"

while choix == "1" or choix == "2" or choix == "3" or choix == "4" or choix == "5" or choix == "6":
    choix = input("""
1: Ajouter un.e élève et sa note
2: Enlever un.e élève et sa note (à partir du nom de l'élève)
3: Afficher les notes des élèves (ordre original)
4: Afficher les notes des élèves (en ordre alphabétique)
5: Calculer la moyenne de la classe
6: Afficher les élèves qui ont sont en situation d'échec
Q: Quitter le programme
Réponse: """)
    
    if choix == "1":
        nom = input("Entre le nom de l'élève: ")
        while not nom.isalpha():
            nom = input("Entre un nom valide: ")
        
        note = input(f"Entre la note de l'élève '{nom}': ")
        while type(note) is not int:
            try:
                note = int(note)
                if note < 0 or note > 100:
                    note = input(f"Entre une note valide pour l'élève '{nom}': ")
            except:
                note = input(f"Entre une note valide pour l'élève '{nom}': ")
        
        noms = np.append(noms, nom)
        notes = np.append(notes, note)
        print(f"Nom '{nom}' enregistré avec la note de {note}.")
        print(f"Noms: {noms} \nNotes: {notes}")

    
    elif choix == "2":
        remove = input(f"Entrer l'indexe du nom de l'élève que vous voulez enlever {noms}: ")
        try:
            remove = int(remove)
            noms = np.delete(noms, remove)
            notes = np.delete(notes, remove)
            print(f"Nom à l'indexe {remove} enlevé.\nNouveau tableaux:\n{noms}\n{notes}")
        except:
            print("Indexe invalide")
            
    elif choix == "3":
        print(f"Noms: {noms} \nNotes: {notes}")
    
    elif choix == "4":
        noms_sorted = np.sort(noms)
        print(noms_sorted)
        
        notes_sorted = []
        for nom in noms_sorted:
            notes_sorted.append(int(notes[np.where(noms == nom)[0][0]]))
        
        print(notes_sorted)
            
    elif choix == "5":
        print(f"La moyenne de la classe est: {np.average(notes)}")
                    
    elif choix == "6":
        print(f"Noms: {noms} \nNotes: {notes}")
        count = 0
        for i in range(len(notes)):
            if notes[i] < 50:
                print(f"Élève {noms[i]} en situation d'échec avec une note de {notes[i]}")
            else:
                count += 1
        if count == len(notes):
            print("Aucun élève en situation d'échec!")