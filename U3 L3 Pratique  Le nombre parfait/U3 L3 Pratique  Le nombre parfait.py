def nombre_parfait(num):
    diviseurs = set()
    for i in range(1, num):
        if num % i == 0:
            diviseurs.add(i)
    
    if sum(diviseurs) == num:
        return True
    else:
        return False

while True:
    nombre = input("Entrer un nombre entier positif: ")
    while type(nombre) is not int:
        try:
            nombre = int(nombre)
            if nombre < 0:
                nombre = input("Entrer un nombre entier positif valide: ")
        except:
            nombre = input("Entrer un nombre entier positif valide: ")
    
    if nombre_parfait(nombre) == True and nombre != 0:
        print(f"Le nombre {nombre} est un nombre parfait!")
    else:
        print(f"Le nombre {nombre} n'est pas un nombre parfait!")
    
    r = input("Recommencer le programme? (o/n): ")
    if r != "O" and r != "o":
        break