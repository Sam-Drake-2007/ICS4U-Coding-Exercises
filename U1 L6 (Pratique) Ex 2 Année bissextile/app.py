année = int(input("Entrer une année pour vérifier si elle est bissextile: "))
final = année % 4 != 0 or année % 100 == 0 and année % 400 != 0
print(not final)