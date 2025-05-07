# Définition de la classe.
class Maison:
  def __init__(self, valeur):
    self._prix = valeur
    self._inventaire = []

  def __str__(self):
    return f"Le prix de cette maison est de {self._prix}."

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
      print("Le prix ne peut pas être négatif.")
    else:
      self._prix = valeur

  @prix.deleter
  def prix(self):
    del self._prix