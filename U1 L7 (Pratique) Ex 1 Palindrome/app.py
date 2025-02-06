while True:
    
    mot_2 = ""
    
    mot_1 = input("Entrer un mot pour vérifier si c'est un palindrome (x pour arrêter le programme): ")

    if mot_1 == "x":
        break

    for m in mot_1[::-1]:
        mot_2 = mot_2 + m
        
    if mot_1.lower() == mot_2.lower():
        print("Ce mot est un palindrome!")
        mot_2 = ""

    else:
        print("Ce mot n'est pas un palindrome!")
        mot_2 = ""