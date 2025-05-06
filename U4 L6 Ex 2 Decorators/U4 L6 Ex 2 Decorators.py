
class Maison:
    def __init__(self, prix):
        self._prix = prix

    @property
    def prix(self):
        return self._prix

    @prix.setter
    def prix(self, prix):
        if prix < 0:
            print("Le prix ne peut pas être négatif.")
        else:
            self._prix = prix
    
    @prix.deleter
    def prix(self):
        del self._prix

# programme principal
objMaison1 = Maison(350000)
print(objMaison1.prix)

objMaison1.prix = 425000
print(objMaison1.prix)

del(objMaison1.prix)
objMaison1.prix = 500000
print(objMaison1.prix)