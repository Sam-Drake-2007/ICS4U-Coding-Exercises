val1 = input("Entrer la première valeur (Entière): ")
while type(val1) is not int:
    try:
        val1 = int(val1)
    except:
        val1 = input("Entrer une première valeur valide (Entière): ")

val2 = input("Entrer la deuxième valeur (Décimale): ")
while type(val2) is not float:
    try:
        val2 = float(val2)
    except:
        val2 = input("Entrer une deuxième valeur valide (Décimale): ")
        
operator = input("Entrer l'opérateur (+, -, *, /): ")
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
    operator = input("Entrer un opérateur valide (+, -, *, /): ")
    
if operator == "+":
    print(f"Le résultat de {val2} {operator} {val2} est: {val1 + val2}")
elif operator == "-":
    print(f"Le résultat de {val2} {operator} {val2} est: {val1 - val2}")
elif operator == "*":
    print(f"Le résultat de {val2} {operator} {val2} est: {val1 * val2}")
elif operator == "/":
    print(f"Le résultat de {val2} {operator} {val2} est: {val1 / val2}")
