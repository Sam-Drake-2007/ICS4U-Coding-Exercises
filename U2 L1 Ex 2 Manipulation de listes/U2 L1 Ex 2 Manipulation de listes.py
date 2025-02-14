# U2 L1 Ex 2 Manipulation de listes

# Modifie le code ci-dessous pour que chaque liste soit modifiée selon
# la sortie indiquée sur la dernière page de la présentation.

# Début du programme

# Défi 1
print("\nDéfi 1")
lstEntree = ["pomme", "banane", "cerise"]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu: ["pomme", "groseille", "cerise"]

lstEntree[1] = "groseille"

print(f"Liste sortie: {lstEntree}")

# Défi 2 façon 1
print("\nDéfi 2 façon 1")
lstEntree = ["pomme", "banane", "cerise"]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree.extend(["orange"])

print(f"Liste sortie: {lstEntree}")

# Défi 2 façon 2
print("\nDéfi 2 façon 2")
lstEntree = ["pomme", "banane", "cerise"]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree.append("orange")

print(f"Liste sortie: {lstEntree}")

# Défi 3
print("\nDéfi 3")
lstEntree = ["pomme", "banane", "cerise"]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree.insert(1, "poire")

print(f"Liste sortie: {lstEntree}")

# Défi 4
print("\nDéfi 4")
lstEntree = ["pomme", "banane", "cerise", "orange", "kiwi", "melon", "mangue"]  
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree = lstEntree[3:6]

print(f"Liste sortie: {lstEntree}")

# Défi 5
print("\nDéfi 5 façon 1")
lstEntree = ["pomme", "poire", "banane", "cerise"]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree.remove(lstEntree[2])

print(f"Liste sortie: {lstEntree}")

# Défi 5 façon 2
print("\nDéfi 5 façon 2")
lstEntree = ["pomme", "poire", "banane", "cerise"]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree.pop(2)

print(f"Liste sortie: {lstEntree}")

# Défi 6
print("\nDéfi 6")
lstEntree = ["pomme", "poire", "cerise"]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree.extend(["orange", "kiwi", "melon", "mangue"])

print(f"Liste sortie: {lstEntree}")

# Défi 7
print("\nDéfi 7")
lstEntree = [100, 300, 400, 200, 600]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree = sum(lstEntree)

print(f"Liste sortie: {lstEntree}")

# Défi 8
print("\nDéfi 8")
lstEntree = [100, 300, 400, 200, 600]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree.sort()
lstEntree.reverse()

print(f"Liste sortie: {lstEntree}")

# Défi 9 façon 1
print("\nDéfi 9 façon 1")
lstEntree = [100, 300, 400, 200, 600]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree.reverse()

print(f"Liste sortie: {lstEntree}")

# Défi 9 façon 2
print("\nDéfi 9 façon 2")
lstEntree = [100, 300, 400, 200, 600]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

lstEntree = lstEntree[::-1]

print(f"Liste sortie: {lstEntree}")

# Défi 10 (Difficulté élevé)
print("\nDéfi 10 façon 1")
lstEntree = ["a", "b", "c", "d", "e"]  # Établir la liste.
print(f"Liste entrée: {lstEntree}")

# Ajoute le code qui utilise les fonctions appropriées pour manipuler
# la liste afin d'obtenir le résultat attendu

for i in range(1, 2* len(lstEntree) - 1, 2):
    lstEntree.insert(i, "-")

print(f"Liste sortie: {lstEntree}")