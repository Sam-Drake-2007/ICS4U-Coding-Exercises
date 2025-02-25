# U2 L5 Ex 2 Débogage Moyenne scolaire

'''
Un programme qui calcule la moyenne d'une ou d'un élève en lettres à partir de trois notes et qui donne un message sur son rendement.

'''

# Note moyenne
# 95+   : 4+
# 80-94	: Niveau 4
# 70-79	: Niveau 3
# 60-69	: Niveau 2
# 50-59	: Niveau 1
# 0-49 : R

# --- Exemple ---
# Tests : 89, 90, 90
# Moyenne : 90
# Rendement : Niveau 4
# L'élève a réussi à son examen.

# Tests : 50, 51, 0
# Moyenne : 33
# Rendement : R
# L'élève n'a pas réussi à son examen.

intTest1 = int(input("Saisir le premier résultat de l'examen : "))

intTest2 = int(input("Saisir le deuxième résultat de l'examen : "))

intTest3 = int(input("Saisir le troisième résultat de l'examen : "))

lstTests = [intTest1, intTest2, intTest3]
somme = 0
for intNote in lstTests:
  somme = somme + intNote

fltMoyenne = somme / len(lstTests)

if fltMoyenne >= 95:
    strRendement = "Niveau 4+"
elif fltMoyenne >= 80 and fltMoyenne < 94:
    strRendement = "Niveau 4"
elif fltMoyenne > 70 and fltMoyenne < 79:
    strRendement = "Niveau 3"
elif fltMoyenne <= 69 and fltMoyenne >= 65:
    strRendement = "Niveau 2"
else:
    strRendement = "F"

print("Tests : " + str(lstTests))

print("Moyenne : " + str(fltMoyenne))

print("Rendement : ", strRendement)

if strRendement == "F":
    print("L'élève n'a pas réussi à son examen.")
else:
    print("L'élève a réussi à son examen.")