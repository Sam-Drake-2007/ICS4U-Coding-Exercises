import math
def circonf(rayon):
    """Cette fonction calcule la circonférence d'un cercle."""
    return 2 * rayon * math.pi

def aire(rayon):
    """Cette fonction calcule l'aire d'un cercle."""
    return rayon ** 2 * math.pi

def volume(rayon):
    """Cette fonction calcule le volume d'un cercle."""
    return rayon ** 3 * (4 / 3) * math.pi