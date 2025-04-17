import rectangle

obj_rectangle = rectangle.rec()
obj_rectangle.setcotes(2, 2)

print(f"Les dimensions du rectangle sont de base: {obj_rectangle.getbase()}, et hauteur: {obj_rectangle.gethauteur()}")
print(f"Le périmètre est de {obj_rectangle.perimetre()} unités.")
print(f"L'aire du rectangle est de {obj_rectangle.aire()} unités carrées.")
print(f"La somme des angles intérieurs est de {obj_rectangle.somme_angles_interieurs()} degrés.")

if obj_rectangle.estcarre() == True:
    print("Le rectangle est un carré!")
else:
    print("Le rectangle n'est pas un carré!")