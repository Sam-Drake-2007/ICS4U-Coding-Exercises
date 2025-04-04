from math import factorial

def triangle(rangées):
    
    lstrangées = [] # Liste contenant tout les rangées
    
    for i in range(rows + 1): # + 1 car les rangées commencent à 0
        rangée = ""
        
        for j in range(i + 1): # + 1 car les positions dans les rangées commencent à 0
            rangée += str(int(factorial(i) / (factorial(j) * factorial(i - j)))) + " " # Formule de combinaison pour chaque position de la rangée
            
        lstrangées.append(rangée)
    
    for rangée in lstrangées:
        rangée = rangée.center(len(lstrangées[-1])) # Centre la rangée en utilisant la rangée la plus longue (dernière de la liste)
        print(rangée)

rows = input("Entrer le nombre de rangées dans le triangle de pascal (Nombre entier positif >= 0): ")
while type(rows) is not int:
    try:
        rows = int(rows)
        if rows < 0:
            rows = input("Entrer un nombre de rangées valide (Nombre entier positif >= 0): ")
    except:
        rows = input("Entrer un nombre de rangées valide (Nombre entier positif >= 0): ")
        
triangle(rows)