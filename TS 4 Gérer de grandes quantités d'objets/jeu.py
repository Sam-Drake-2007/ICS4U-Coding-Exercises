class jeu:
    
    def __init__(self, nom):
        self._strnom = nom
        self._lstdeveloppeur = []
        self._lstgenre = []
        self._intannee = 0
        self._lstlangage = []
    
    
    def __str__(self):
        return f"Le nom du jeu vidéo est: '{self._strnom}'"
    
    def __getitem__(self, position):
        return self._lstdeveloppeur[position], self._lstlangage[position]
    
    def __len__(self):
        return len(self._lstdeveloppeur), len(self._lstgenre), len(self._lstlangage)
    
    def ajout_objet_dev(self, strObjet):
        self._lstdeveloppeur.append(strObjet)
        
    def supp_objet_dev(self, strObjet):
        self._lstdeveloppeur.remove(strObjet)

    def ajout_objet_genre(self, strObjet):
        self._lstgenre.append(strObjet)
        
    def supp_objet_genre(self, strObjet):
        self._lstgenre.remove(strObjet)
    
    def ajout_objet_langage(self, strObjet):
        self._lstlangage.append(strObjet)

    def supp_objet_langage(self, strObjet):
        self._lstdeveloppeur.remove(strObjet)
    
    @property 
    def strnom(self):
        return self._strnom
        
    @strnom.setter
    def strnom(self, strvaleur):
        self._strnom = strvaleur
        
    @property 
    def lstdeveloppeur(self):
        return self._lstdeveloppeur
        
    @lstdeveloppeur.setter
    def lstdeveloppeur(self, lstvaleur):
        self._lstdeveloppeur = lstvaleur
        
    @property 
    def lstgenre(self):
        return self._lstgenre
        
    @lstdeveloppeur.setter
    def lstgenre(self, strvaleur):
        self._lstgenre = strvaleur
        
    @property
    def intannee(self):
        return self._intannee
        
    @intannee.setter
    def intannee(self, intvaleur):
        self._intannee = intvaleur
        
    @property
    def lstlangage(self):
        return self._lstlangage
        
    @lstlangage.setter
    def lstlangage(self, lstvaleur):
        self._lstlangage = lstvaleur