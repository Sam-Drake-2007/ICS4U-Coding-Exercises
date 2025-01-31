# U1 L3 Ex 2 Utilisation et exploration du module math

# Exécute le code suivant

# Réponds en forme de commentaires
# aux questions suivantes dans le programme même.


# 1. Que fait l'instruction suivante?
# Cette instruction importe le module nommé "math" qui permet d'utilisé des fonction interessantes liés à ce module
import math

# Que fait l'instruction suivante?  
# Elle demande à l'utilisateur pour une donnée et la converti et type int

# Qu'arrive-t-il si l'utilisateur donne
# La donnée fourni par l'utilisateur est sauveguardée dans une variable nommée: intRayon
intRayon = int(input("Donne le rayon du cercle: "))

# Que font les deux instructions suivantes?
# La première fait une équation mathématique pour calculer la circonference du cercle
# La deuxième fait la même chose mais pour l'aire

# Nomme les fonctions du module math qui sont utilisées.
# math.pi math.pow --> toutes les fonctions qui sont précédés par math. sont des fonctions du module math
intCirconference = math.pi*2*intRayon
intAire = math.pi*math.pow(intRayon,2)

# Quelles sont les particularités de la commande print ici-bas?
# Elle utilise \n et \t pour donner du style au texte qui sera affiché
# Elle utilise aussi une fonction pour arondir les variables pour avoir 2 décimals
 
print(f"""\nPour un cercle qui a un rayon de {intRayon} unité(s),
\tla circonférence est de {intCirconference:.2f} unité(s),
\tet l'aire est de {intAire:.2f} unité(s).""")