import time

while True:

    nom = input("Entrer votre nom: ")
    time.sleep(1)

    année = input("Entrer l'année courante: ")
    time.sleep(1)

    while type(année) != int or année < 0:
        try:
            année = int(année)
        except:
            année = input("Entrer une année valide: ")

    graduation = input("Entrer votre année de graduation: ")
    time.sleep(1)

    while type(graduation) != int:
        try:
            graduation = int(graduation)
        except:
            graduation = input("Entrer une année valide: ")

    if année == graduation:
        print(f"Félicitation {nom}! Tu termines ton secondaire cette année!")
    elif année - graduation == 1:
        print(f"Ne lâche pas, {nom}! Il te reste qu'une année de secondaire pour obtenir ton diplôme.")
    else:
        print(f"Continue à persévérer, {nom}! Tu n'as que {graduation - année} années à aller pour obtenir ton diplôme secondaire.")
    
    recommencer = input("Recommencer le programme? [o/n]: ")
    
    if recommencer == "o":
        continue
    else:
        break