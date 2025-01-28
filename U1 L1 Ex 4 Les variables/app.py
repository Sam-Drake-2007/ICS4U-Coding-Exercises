# ICS4U Les variables et les types de données
# Ce programme assigne les types de données typiques à des variables en Python. 
# 1. Peux-tu prédire la sortie du programme sans l’exécuter? 
# 2. Ajoute un commentaire pour chaque variable qui indique son type (par ex int, string, etc...)
# 3. Exécute le programme pour vérifier si la sortie est bien celle que tu as prédite.  
# 4. Corrige les erreurs s’il y en a.

num1 = 5 # Int
num2 = "test" # String
montext = "Ton nom" # String
estvrai = True # Boolean

print(estvrai)
print(num1)
print("La variable 'num2' = ", num2) # Pour voir le type d'une variable il faut faire type(x). Donc il faudrait faire: 
print("La variable 'num2' = ", type(num2))

test = (5 < 8)
print(test)

# a, b = 5, 7 On ne peut pas déclarer deux variables dans une ligne
a = 5
b = 7
print(a)
print(b)

#Pourquoi la ligne ci-dessous génère-t-elle une erreur?
# print (Montext) Lettre majuscule qui devrais être minuscule et il y a un espace avant les paramètres
print(montext)