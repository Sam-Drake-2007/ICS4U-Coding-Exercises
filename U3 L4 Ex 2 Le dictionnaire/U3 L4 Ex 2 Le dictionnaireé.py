# U3 L4 Ex 2 Le dictionnaire

# Fonctions
def imprimeEleve(dctEleve, intcle):
    if intcle not in dctEleve.keys():
        print("Cet indice n'existe pas dans le dictionnaire.")
    else:
        print(dctEleve[intcle])


# Programme principal
while True:
    dctLesEleves = {
    25: ["Beauregard", "Josée", "423 533 985"],
    26: ["Dupuis", "Marie","522 781 012"],
    32: ["Sawaya", "Candice", "123 655 735"],
    12: ["Mbala", "Robert", "222 956 423"]
    }

    clé = input("L'indice de l'élève (nombre entier seulement): ")
    while type(clé) is not int:
        try:
            clé = int(clé)
            if clé < 0:
                clé = input("Entrer un indice valide: ")
                
        except:
            clé = input("Entrer un indice valide: ")
            
    imprimeEleve(dctLesEleves, clé)
    
    r = input("Imprimer un autre dossier? (o/n): ")
    if r != "o" and r != "O":
        break