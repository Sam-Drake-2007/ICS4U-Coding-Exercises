# U3 L6 Ex 1 Exploration : La portée d'une variable

# Exploration: La portée d'une variable

# Modification de valeurs dans des fonctions.
# Exécute ce programme et examine la sortie. 

# Ensuite réponds aux questions suivantes:
"""
1. Est-ce que les valeurs transférées aux fonctions doivent être du même type? (Par exemple, est-ce qu’un fonction peut accepter juste des variables « int », ou juste des variable « string », etc…)
    Réponse: non

2. Y a-t-il des différences dans la façon dont les valeurs sont modifiées dans les fonctions?
    Réponse: non
    
3. Que veut-on dire par « intérieur » et « extérieur » de la fonction?
    Réponse: intérieur fait partie de la fonction, extérieur fait partie du code principal
    
4. Que remarques-tu à propos de la valeur du dictionnaire dctUnDiction1 après l’appel à la fonction3? Après l’appel à la fonction 4?
    Réponse: Le dictionnaire se fait modifié et reste modifié même apres d'être sorti de la fonction

"""

def fonction1(intN):
  print(f"Valeur de 'intN' dans la fonction1 : {intN}")
  intN += 5
  print(f"Nouvelle valeur de 'intN' dans la fonction1 : {intN}")
  return

def fonction2(strTexte):
  print(f"Valeur de 'strTexte' dans la fonction2 : {strTexte}")
  strTexte = "autres choses"
  print(f"Nouvelle valeur de 'strTexte' dans la fonction2 : {strTexte}")
  return

def fonction3(dctEleves):
  # Modification d'un dictionnaire.
  print(f"Valeur de 'dctEleves' dans la fonction3 : {dctEleves}")
  dctEleves={'alok':30,'Nevadan':28}
  print(f"Nouvelle valeur de 'dctEleves' dans la fonction3 : {dctEleves}")
  return

def fonction4(dctEleves):
  # Modification d'un dictionnaire version 2.
  print(f"Valeur de 'dctEleves' dans la fonction4 : {dctEleves}")
  dctEleves.update({'alok':30,'Nevadan':28})
  print(f"Nouvelle valeur de 'dctEleves' dans la fonction4 : {dctEleves}")
  return

# Modification d'un chiffre entier dans une fonction.
intValeur1 = 10
print(f"Valeur de 'intValeur1' avant la fonction1 : {intValeur1}")
fonction1(intValeur1)
print(f"Valeur de 'intValeur1' après la fonction1 : {intValeur1}")

print("\n")
# Modification d'une chaîne de caractères dans une fonction.
strValeur2 = "Bonjour"
print(f"Valeur de 'strValeur2' avant la fonction2 : {strValeur2}")
fonction2(strValeur2)
print(f"Valeur de 'strValeur2' après la fonction2 : {strValeur2}")

print("\n")
# Modification d'un dictionnaire dans une fonction.
dctUnDiction1 = {'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
print(f"Valeur de 'dctUnDiction1' avant la fonction3 : {dctUnDiction1}")
fonction3(dctUnDiction1)
print(f"Valeur de 'dctUnDiction1' après la fonction3 : {dctUnDiction1}")

print("\n")
# Modification d'un dictionnaire dans une fonction.
dctUnDiction2 = {'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
print(f"Valeur de 'dctUnDiction2' avant la fonction4 : {dctUnDiction2}")
fonction4(dctUnDiction2)
print(f"Valeur de 'dctUnDiction2' après la fonction4 : {dctUnDiction2}")