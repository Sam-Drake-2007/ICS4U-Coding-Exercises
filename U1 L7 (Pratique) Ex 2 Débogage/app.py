# Boîte à outils B1 Débogage

# Un programme qui accepte 2 données et imprime la plus grande

while True:

    intDonne1 = input("Entrer le premier chiffre: ")

    while type(intDonne1) != int:
        try:
            intDonne1 = int(intDonne1)
        except:
            intDonne1 = input("Entrer un premier chiffre valide: ")

    intDonne2 = input("Entrer le deuxième chiffre: ")

    while type(intDonne2) != int:
        try:
            intDonne2 = int(intDonne2)
        except:
            intDonne2 = input("Entrer un deuxième chiffre valide: ")

    if intDonne1 < intDonne2:
        print(f"Le chiffre {intDonne2} est plus grand")
    else:
        print(f"Le chiffre {intDonne1} est plus grand")
        
    r = input("Recommencer le programme? (o/n): ")
    
    if r != "o":
        break