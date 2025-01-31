while True:
    nombre = input("Entrer un nombre qui contient seulement des chiffres (0 à 9): ")
    
    while nombre.isdigit() != True:
        nombre = input("Entrer un nombre valide qui contient seulement des chiffres (0 à 9): ")
    
    print(f"Ton nombre contient {len(nombre)} chiffres!")
    
    r = input("Recommencer le programme? (o/n): ")
    if r != "o":
        break