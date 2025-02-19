file, caisse, count = [], {"5$": 0, "10$": 0, "20$": 0}, 1 # Déclaration des variables

while True:
   
    argent = input(f"\nClient #{count}:\nEntrer le billet recu (Q/q pour quitter)\n")
   
    if argent != "5" and argent != "10" and argent != "20": break
   
    file.append(int(argent))
    count += 1

for i in range(len(file)):
   
    extra = file[i] - 5
   
    print(f"\nClient #{i + 1} paye avec un billet de {file[i]}$.\n{extra}$ à rendre")
   
    if extra == 0:
            caisse["5$"] += 1
            print(f"Argent remis | Change: {caisse}")

    elif extra == 5:
        caisse["10$"] += 1
        if caisse["5$"] >= 1:
            caisse["5$"] -= 1
            print(f"Argent remis | Change: {caisse}")
        else:
            print(f"Pas assez de change: {caisse}")
            quit()
       
    elif extra == 15:
        caisse["20$"] += 1
        if caisse["10$"] >= 1 and caisse["5$"] >= 1:
            caisse["5$"] -= 1
            caisse["10$"] -= 1
            print(f"Argent remis | Change: {caisse}")
        else:
            print(f"Pas assez de change: {caisse}")
            quit()