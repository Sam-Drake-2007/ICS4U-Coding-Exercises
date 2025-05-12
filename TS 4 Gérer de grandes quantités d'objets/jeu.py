class jeu:
    
    def __init__(self, nom):
        self._strnom = nom
        self._lstdeveloppeur = []
        self._strgenre = ""
        self._intannee = 0
        self._lstlangage = []
    
    
    def __str__(self):
        return f"Le nom du jeu vidéo est : {self._strnom}"
    
    def __getitem__(self, position):
        return self._lstdeveloppeur[position], self._lstlangage[position]
    
    def __len__(self):
        return len(self._lstdeveloppeur), len(self._lstlangage)
    
    def ajout_objet_dev(self, strObjet):
        self._lstdeveloppeur.append(strObjet)
    
    def ajout_objet_langage(self, strObjet):
        self._lstlangage.append(strObjet)
    
    @property 
    def strnom(self):
        return self._strnom
        
    @strnom.setter
    def strnom(self, strvaleur):
        self.strnom = strvaleur
        
    @property 
    def lstdeveloppeur(self):
        return self._lstdeveloppeur
        
    @lstdeveloppeur.setter
    def lstdeveloppeur(self, lstvaleur):
        self.lstdeveloppeur = lstvaleur
        
    @property 
    def strgenre(self):
        return self._strgenre
        
    @lstdeveloppeur.setter
    def strgenre(self, strvaleur):
        self._strgenre = strvaleur
        
    @property
    def intannee(self):
        return self._intannee
        
    @intannee.setter
    def intannee(self, intvaleur):
        self.intannee = intvaleur
        
    @property
    def lstlangage(self):
        return self._lstlangage
        
    @lstlangage.setter
    def lstlangage(self, lstvaleur):
        self._lstlangage = lstvaleur