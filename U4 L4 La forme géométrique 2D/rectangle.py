class rec:
    
    def __init__(self):
        self._longeur_base = 1
        self._longeur_hauteur = 1
    
    def setcotes(self, base, hauteur):
        if base >= 0 or hauteur >= 0:
            self._longeur_base = base
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