# Ce programme définit une classe avec
# les attributs _prenom et _surnom,
# et contient une méthode qui « parle » 
# et qui imprime «Je m'appelle prénom surnom.».

class Personne:
  def __init__(self, prénom, surnom):
    self._prenom = prénom
    self._surnom = surnom
  
  def parle(self):
      print("Je m'appelle " + self._prenom + " " + self._surnom)

objmoi = Personne("Amélie", "Poulin.")
objtoi = Personne("Albert", "Einstein.")

objmoi.parle()
objtoi.parle()

print(objmoi._prenom)
print(objmoi._surnom)