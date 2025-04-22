class rec:
    
    def __init__(self, base, hauteur):
        self._longeur_base = base
        self._longeur_hauteur = hauteur
    
    def setbase(self, base):
        self._longeur_base = base

    def sethauteur(self, hauteur):
        self._longeur_hauteur = hauteur
            
    def getbase(self):
        return self._longeur_base
    
    def gethauteur(self):
        return self._longeur_hauteur
            
    def aire(self):
        return self._longeur_base * self._longeur_hauteur
    
    def perimetre(self):
        return 2 * self._longeur_base + 2 * self._longeur_hauteur
    
    def somme_angles_interieurs(self):
        return 360
    
    def estcarre(self):
        if self._longeur_base == self._longeur_hauteur:
            return True
        else:
            return False