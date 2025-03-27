# U3 L4 Ex 1 Débogage

# Les paramètres de fonctions

def mafonction1(intValeur1, intValeur2): # Il faut avoir une virgule pour séparer les variables sur cette ligne
  """ Fonction qui additionne intValeur1 et intValeur2. """
  print(intValeur1 + intValeur2)

def mafonction2(strUn_nom, strQualite = "est géniale."): # Il manquait une ":" à la fin de cette ligne
  """ Fonction qui imprime strUn_nom suivi de sa qualité (est géniale par défaut). """
  print(strUn_nom,strQualite)

def mafonction3(intChiffre1, intChiffre2): # La fonction doit avoir son propre nom
  """ Fonction qui multiplie intChiffre1 et intChiffre2. """
  print(intChiffre1*intChiffre2)

def mafonction4(intAge, strMessage = "ans n'est pas trop vieux."): # Les variables non-default doivent aller en premier des variables default
  """ Fonction qui imprime un message selon l'age donné. """
  print(intAge, strMessage)
  
print(mafonction1.__doc__)
mafonction1(101, 55)
print("")

print(mafonction2.__doc__)
mafonction2("Nicolas")
print("")

print(mafonction3.__doc__)
mafonction3(11, 13)
print("")

print(mafonction4.__doc__)
mafonction4(82)