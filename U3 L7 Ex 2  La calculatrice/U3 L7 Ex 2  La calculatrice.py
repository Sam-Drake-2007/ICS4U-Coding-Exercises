import calculatrice

print(f"La fonction addition:\n{calculatrice.addition.__doc__}")
print(f"La fonction soustraction:\n{calculatrice.soustraction.__doc__}")
print(f"La fonction multiplication:\n{calculatrice.multiplication.__doc__}")
print(f"La fonction division:\n{calculatrice.division.__doc__}")

for i in range(1, 4):
    num1 = input(f"\nTest #{i}\nEntrer la valeur du premier nombre: ")
    while type(num1) is not float:
        try:
            num1 = float(num1)
        except:
            num1 = input(f"Entrer une valeur valide pour le premier nombre: ")
            
    num2 = input(f"\nPremier numéro accepté\nEntrer la valeur du deuxième nombre: ")
    while type(num2) is not float:
        try:
            num2 = float(num2)
        except:
            num2 = input(f"Entrer une valeur valide pour le deuxième nombre: ")
    
    bool1 = input("Imprimer les résultats dans la fonction? (o/n): ")
    if bool1 == "o" or bool1 == "O":
        bool1 = True
        calculatrice.addition(num1, num2, bool1)
        calculatrice.soustraction(num1, num2, bool1)
        calculatrice.multiplication(num1, num2, bool1)
        calculatrice.division(num1, num2, bool1)
    else:
        bool1 = False
        print(f"(Main) Le résultat de l'addition entre {num1} et {num2} est {calculatrice.addition(num1, num2, bool1)}!")
        print(f"(Main) Le résultat de la soustraction entre {num1} et {num2} est {calculatrice.soustraction(num1, num2, bool1)}!")
        print(f"(Main) Le résultat de la multiplication entre {num1} et {num2} est {calculatrice.multiplication(num1, num2, bool1)}!")
        if num2 == 0:
            print("(Main) On ne peut pas diviser un nombre par 0!")
        else:
            print(f"(Main) Le résultat de la division entre {num1} et {num2} est {calculatrice.division(num1, num2, bool1)}!")