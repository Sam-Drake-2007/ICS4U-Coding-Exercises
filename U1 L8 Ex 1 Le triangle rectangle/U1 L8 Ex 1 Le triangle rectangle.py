# U1 L8 Ex 1 Le triangle rectangle

import math

# Bloc de input pour recueillir les coordonnées

x1 = int(input("Entrer la première coordonnée x: "))
y1 = int(input("Entrer la première coordonnée y: "))

x2 = int(input("Entrer la deuxième coordonnée x: "))
y2 = int(input("Entrer la deuxième coordonnée y: "))

x3 = int(input("Entrer la troisième coordonnée x: "))
y3 = int(input("Entrer la troisième coordonnée y: "))


# Calculs pour la pente entre chaque point

m1 = (y2 - y1) / (x2 - x1)
m2 = (y3 - y1) / (x3 - x1)
m3 = (y3 - y2) / (x3 - x2)


# Calculs pour les réciproques négatives

if m1 != 0:
    r1 = -1 * (1 / m1)
else:
    r1 = 0

if m2 != 0:
    r2 = -1 * (1 / m2)
else:
    r2 = 0

if m3 != 0:
    r3 = -1 * (1 / m3)
else:
    r3 = 0


# Calculs pour voir la distance entre chaque point

d1 = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
d2 = math.sqrt(((x3 - x1) ** 2) + ((y3 - y1) ** 2))
d3 = math.sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2))


# Conditions ifs pour vérifier si une des réciproques négatives est égal à une des pentes

if r1 == m2:
    print("Le triangle est rectangle car la pente entre le premier et deuxième point est la réciproque négative de la pente entre le premier et troisième.")
elif r1 == m3:
    print("Le triangle est rectangle car la pente entre le premier et deuxième point est la réciproque négative de la pente entre le deuxième et troisième.")

elif r2 == m1:
    print("Le triangle est rectangle car la pente entre le premier et troisième point est la réciproque négative de la pente entre le premier et deuxième.")
elif r2 == m3:
    print("Le triangle est rectangle car la pente entre le premier et troisième point est la réciproque négative de la pente entre le deuxième et troisième.")

elif r3 == m1:
    print("Le triangle est rectangle car la pente entre le deuxième et deuxième point est la réciproque négative de la pente entre le premier et deuxième.")
elif r3 == m2:
    print("Le triangle est rectangle car la pente entre le deuxième et deuxième point est la réciproque négative de la pente entre le premier et troisième.")

else:
    print("Le triangle n'est pas un triangle rectangle")
    

# Conditions if pour vérifier si le triangle est équilatéral

if d1 == d2 == d3:
    print("Le triangle est équilatéral")
else:
    print("Le triangle n'est pas équilatéral")
