class Vélo:
    
    endroit = "Ottawa"
    
    def __init__(self, intVitesse, strCouleur, strType):
        self.intVitesse = intVitesse
        self.strCouleur = strCouleur
        self.strType = strType
        
    def peinturer(self, couleur):
        self.strCouleur = couleur
    
    def arrêter(self):
        self.intVitesse = 0
    
    def changer_vitesse(self, nouvelle_vitesse):
        self.intVitesse = nouvelle_vitesse
        
objVélo_1 = Vélo(30, "Rouge", "Route")

print(objVélo_1.endroit)
print(objVélo_1.intVitesse)
print(objVélo_1.strCouleur)
print(objVélo_1.strType)

objVélo_1.peinturer("Vert")
print(objVélo_1.strCouleur)

objVélo_1.arrêter()
print(objVélo_1.intVitesse)

objVélo_1.changer_vitesse(25)
print(objVélo_1.intVitesse)