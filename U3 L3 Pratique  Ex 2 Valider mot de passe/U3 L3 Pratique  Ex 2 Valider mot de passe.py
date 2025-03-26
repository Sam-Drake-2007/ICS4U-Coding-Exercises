def évaluation_de_mp(mdp):
    alpha, digit, special = [], [], []
    
    for lettre in mdp:
        if lettre.isalpha():
            alpha.append(lettre)
        elif lettre.isdigit():
            digit.append(lettre)
        else:
            special.append(lettre)
    
    if len(mdp) >= 14 and len(digit) > 0 and len(special) > 0:
        return "fort"
    elif len(mdp) >= 8 and (len(digit) > 0 or len(special)) > 0:
        return "modéré"
    else: # Je considère que les mot de passes très longs sont faibles s'ils n'ont pas de numéros ou symboles
        return "faible"

while True:
    
    mot_de_passe = input("Entrer un mot de passe pour valider si il est fort: ")
    mot_de_passe = mot_de_passe.replace(" ", "")
    
    while len(mot_de_passe) == 0:
        mot_de_passe = input("Entrer un mot de passe valide: ")
        mot_de_passe = mot_de_passe.replace(" ", "")
        
    print(f"Le mot de passe '{mot_de_passe}' est {évaluation_de_mp(mot_de_passe)}")
    
    r = input("Recommencer le programme? (o/n): ")
    if r != "O" and r != "o":
        break