import cercle

print(f"La fonction circonf:\n{cercle.circonf.__doc__}")
print(f"La fonction aire:\n{cercle.aire.__doc__}")
print(f"La fonction volume:\n{cercle.volume.__doc__}")

rayon = input("\nEntrer le rayon du cercle (Valeur numérique > 0) en cm: ")
while type(rayon) is not int:
    try:
        rayon = int(rayon)
        if rayon <= 0:
            rayon = input("Entrer un rayon valide (Valeur numérique > 0) en cm: ")
        
    except:
        rayon = input("Entrer un rayon valide (Valeur numérique > 0) en cm: ")

print(f"La circomférence du cercle est: {round(cercle.circonf(rayon), 2)} cm")
print(f"L'aire du cercle est: {round(cercle.aire(rayon), 2)} cm^2")
print(f"Le volume de la sphère est: {round(cercle.volume(rayon), 2)} cm^3")
