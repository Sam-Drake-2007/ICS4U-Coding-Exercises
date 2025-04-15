# U4 L2 Ex 2 Les triangles

import math

class Triangle:
  def __init__(self):
    self._fltCote_a = 2.0
    self._fltCote_b = 3.0
    self._fltCote_c = 4.0

   # Méthodes d'accessibilité.
  def setCotes(self, a, b, c):
    # Ajoute le code qui valide les côtés a, b et c et qui enlève la commande pass.
    if a < 0 or b < 0 or c < 0 or a + b < c or a + c < b or b + c < a:
        print("Valeurs impossibles pour un triangle")
    else:
        self._fltCote_a = a
        self._fltCote_b = b
        self._fltCote_c = c

  def getCoteA(self):
    # Ajoute le code qui retourne le côté a et qui enlève la commande pass.
    return self._fltCote_a
      
  def getCoteB(self):
    # Ajoute le code qui retourne le côté b et qui enlève la commande pass.
    return self._fltCote_b
      
  def getCoteC(self):
    # Ajoute le code qui retourne le côté c et qui enlève la commande pass.
    return self._fltCote_c
    
  def perimetre(self):
    # Retourne le périmètre du triangle.
    return self._fltCote_a + self._fltCote_b + self._fltCote_c

  def aire(self):
    # Calcul de l'aire du triangle avec la formule de Héron.
    p= self.perimetre()/2
    return math.sqrt(p*(p-self._fltCote_a)*(p-self._fltCote_b)*(p-self._fltCote_c))

  def estRectangle(self):
    # Calcul du théorème de Pythagore selon toutes les possibilités pour le segment représentant l'hypoténuse.
    fltHypothenuse_c = math.sqrt(self._fltCote_a*self._fltCote_a + self._fltCote_b*self._fltCote_b)
    fltHypothenuse_b = math.sqrt(self._fltCote_a*self._fltCote_a + self._fltCote_c*self._fltCote_c)
    fltHypothenuse_a = math.sqrt(self._fltCote_b * self._fltCote_b + self._fltCote_c * self._fltCote_c)

    # Vérifie si l'un des côtés est conforme au théorème de Pythagore.
    if (fltHypothenuse_a==self._fltCote_a or
      fltHypothenuse_b==self._fltCote_b or
      fltHypothenuse_c==self._fltCote_c):
      return True
    else:
      return False
    
  def estEquilateral(self):
      return self._fltCote_a == self._fltCote_b and self._fltCote_a == self._fltCote_c
      
  def estScalene(self):
      return self._fltCote_a != self._fltCote_b and self._fltCote_a != self._fltCote_c and self._fltCote_b != self._fltCote_c

  def estIsocele(self):
      cotes = (self._fltCote_a, self._fltCote_b, self._fltCote_c)
      return cotes.count(cotes[0]) == 2 or cotes.count(cotes[1]) == 2

# Programme principal.

objTriangle = Triangle()                        # création d'un triangle
objTriangle.setCotes(10000, 20, 4)
objTriangle.setCotes(-1, 2, 1)
objTriangle.setCotes(4,3,5)                     # donner les mesures des côtés

print(f"Les dimensions du triangle sont {objTriangle.getCoteA()}, {objTriangle.getCoteB()} et {objTriangle.getCoteC()}.")
print(f"Le périmètre est de {objTriangle.perimetre()} unités.")
print(f"L'aire du triangle est de {objTriangle.aire()} unités carrées.")

if objTriangle.estRectangle()==True:
   print("C'est un triangle rectangle.")
else:
   print("Ce n'est pas un triangle rectangle.")

if objTriangle.estEquilateral() == True:
    print("Ce triangle est équilatéral.")
elif objTriangle.estScalene() == True:
    print("Ce triangle est scalène.")
elif objTriangle.estIsocele() == True:
    print("Ce triangle est isocèle.")