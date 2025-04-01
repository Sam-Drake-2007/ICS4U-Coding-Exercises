def addition(num1, num2, bool1):
    """Cette fonction addition deux nombres ensembles."""
    if bool1 is True:
        print(f"(Fonction) Le résultat de l'addition entre {num1} et {num2} est {num1 + num2}!")
    else:
        return num1 + num2

def soustraction(num1, num2, bool1):
    """Cette fonction soustrait un nombre d'un autre."""
    if bool1 is True:
        print(f"(Fonction) Le résultat de la soustraction entre {num1} et {num2} est {num1 - num2}!")
    else:
        return num1 - num2
    
def multiplication(num1, num2, bool1):
    """Cette fonction multiplie deux nombres ensembles."""
    if bool1 is True:
        print(f"(Fonction) Le résultat de la multiplication entre {num1} et {num2} est {num1 * num2}!")
    else:
        return num1 * num2
    
def division(num1, num2, bool1):
    """Cette fonction divise un nombre par un autre."""
    if num2 == 0:
        print("(Fonction) On ne peut pas diviser un nombre par 0!")
    elif bool1 is True and num2 != 0:
        print(f"(Fonction) Le résultat de la division entre {num1} et {num2} est {num1 / num2}!")
    else:
        return num1 / num2