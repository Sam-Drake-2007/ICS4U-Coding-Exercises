# U2 L5 Débogage 12 défis

# Défi 1
print("Défi 1: Affecter la valeur 12 à la variable intX")

intX = 12
print("Valeur de la variable intX =", intX)

# Défi 2
print("\nDéfi 2: Calculer la moyenne de 3 nombres: 8, 10 et 12")

intA, intB, intC = 8, 10, 12
fltMoyenne = (intA + intB + intC) / 3
print(f"La moyenne de {intA}, {intB} et {intC} est {fltMoyenne}")

# Défi 3
print("\nDéfi 3: Imprimer chaque caractère d'une chaîne")
strMot = "Bonjour"
for c in strMot:
  print(c)

# Défi 4
print("\nDéfi 4: Imprimer la table de multiplication pour 5 de 1 à 12 avec la boucle while")

intN = 1
while intN <= 12:
  print(f"{intN} x 5 = {intN * 5}")
  intN += 1

# Défi 5
print("\nDéfi 5: Calculer la circonférence d'un cercle")

intRayon = input("Mesure du rayon: ")
fltCirc = int(intRayon)**2 * 3.14
print(f"La circonférence d'un cercle de rayon {intRayon} = {fltCirc}")

# Défi 6
print("\nDéfi 6: Vérifier si intX est zéro ")

intX = int(input("Nombre entier: "))
if intX == 0:
  print("intX est égal à zéro")

# défi 7
print("\nDéfi 7: Vérifier que le nombre est entre -5 et 5")

intX = int(input("Nombre entier: "))
if intX > -5 and intX < 5:
  print(f"La valeur {intX} est entre -5 et 5")

# défi 8
print("\nDéfi 8: Vérifie si intX est plus petit que intY")

intX = int(input("Nombre entier: "))
intY = int(input("Deuxième nombre entier: "))

if intX < intY:
  print(f"{intX} est plus petit que {intY}")

# défi 9
print("\nDéfi 9: Ajoute 20 au nombre entier")

intX = int(input("Nombre entier: "))
print(intX + 20)

# défi 10
print("\nDéfi 10: Ajoute 20 au nombre entier")

intX = int(input("Nombre entier: "))
print(intX + 20)

# défi 11
print("\nDéfi 11: Imprime de 1 à 10 à l'aide de la boucle while")
intX = 1

while intX <= 10:
  print(intX)
  intX += 1

# défi 12
print("\nDéfi 12: Imprime la dernière lettre du nom de la personne")

strNom = input("Ton nom: ")

print("La dernière lettre de ton nom est:", strNom[-1])