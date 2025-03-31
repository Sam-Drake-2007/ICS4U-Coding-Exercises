def hacker(mot):
    remplacements = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}
    
    for remplacement in remplacements:
        mot = mot.replace(remplacement, remplacements[remplacement])

    return mot

def rhacker(mot):
    remplacements = {"4": "a", "3": "e", "1": "i", "0": "o", "5": "s"}

    for remplacement in remplacements:
        mot = mot.replace(remplacement, remplacements[remplacement])

    return mot

message = input("Entrer une phrase alphabétique pour la convertir en hacker: ")
print(hacker(message))

message = input("Entrer une phrase hacker pour la convertir en phrase alphabétique: ")
print(rhacker(message))