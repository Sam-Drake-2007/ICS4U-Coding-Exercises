# Définition de la classe
class Maison:
  def __init__(self, valeur):
    self._prix = valeur
    self._inventaire = []

  def __str__(self):
    return f"Le prix de cette maison est {self._prix}"

  def __getitem__(self, position):
    return self._inventaire[position]

  def __len__(self):
    return len(self._inventaire)
  
  def ajout_objet(self, strObjet):
    self._inventaire.append(strObjet)
  
  @property
  def prix(self):
    return self._prix

  @prix.setter
  def prix(self, valeur):
    if valeur < 0:
      print("Le prix ne peut pas être négatif")
    else:
      self._prix = valeur

  @prix.deleter
  def prix(self):
    del self._prix

# programme principal
objMaison1 = Maison(350000)
print(objMaison1.prix)     # vérifie le décorateur @property
objMaison1.prix = 450000   # vérifie le décorateur @setter
print(objMaison1)          # vérifie la méthode __str__

# Ajouter des meubles
objMaison1.ajout_objet("4 chaises")
objMaison1.ajout_objet("Table de cuisine")
objMaison1.ajout_objet("1 Divan")
print(f"Nombre de meubles: {len(objMaison1)}") # vérifie la méthode __len__
  
for strmeuble in objMaison1: # Vérifie la méthode __getitem__
  print(strmeuble) # Vérifie la méthode __str__
  