while True:

    nom = input("Entrer votre nom: ")
    nombre = int(input("Entrer le nombre de pizza commandées: "))
    prix = float(input("Entrer le prix d'une pizza: "))

    final = round((nombre * prix) * 1.13, 2)

    print(f"Bonjour {nom}, vous avez commandez {nombre} pizza à {prix} par unité ce qui donne un prix final de {final}$")
    
    r = input("Recommencer le programme? (o/n): ")
    
    if r != "o":
        break