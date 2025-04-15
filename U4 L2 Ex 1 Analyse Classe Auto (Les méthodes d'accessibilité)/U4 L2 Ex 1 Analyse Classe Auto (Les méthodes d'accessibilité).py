class Auto:
  # 1. Explique l’utilité de cette fonction. ### Crée les paramètres de l'objet
  def __init__(self):
    self._intLimite_reservoir = 60
    self._intNiveau_essence = 0

  # 2. Que fait cette fonction? ### Permet de changer le niveau d'essence de l'objet
  def setNiveauEssence(self, n):
    if n > self._intLimite_reservoir: # 3. Explique cette condition. ### Si le nouveau montant d'essence est au dessu de la limite du reservoir
      self._intNiveau_essence = self._intLimite_reservoir
    elif n < 0: # 4. Explique cette condition. ### Si le nouveau montant d'essence est négatif
      self._intNiveau_essence = 0
    else:
      self._intNiveau_essence = n # 5. Quand cette instruction sera-t-elle exécutée? Donne une explication. ### Si les deux autres conditions ne sont pas executées, donc si c'est une donnée valide

  # 6. Que fait cette fonction? ### Retourne le niveau d'essence actuel de la voiture
  def getNiveauEssence(self):
    return self._intNiveau_essence

# 7. Que fait cette fonction? ### Crée un objet avec la classe Auto
objAuto1 = Auto()

objAuto1.setNiveauEssence(100)
print(objAuto1.getNiveauEssence())

objAuto1.setNiveauEssence(-1)
print(objAuto1.getNiveauEssence())

objAuto1.setNiveauEssence(50)
print(objAuto1.getNiveauEssence())