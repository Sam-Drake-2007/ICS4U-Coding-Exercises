# Que fait la ligne suivante ? Réponse: importer le module tkinter
import tkinter as tk

def cliqueCalculer():
  # Ajoute le code nécessaire pour récupérer 
  # les données d'entrées dans les boîtes d'entrée
  # Faire le calcul et afficher le résultat
  
  # Ajoute un try except pour valider
  # que les valeurs sont acceptables.
  # Rappel: n'utilise pas de boucle while avec le try except
  
  # Si les valeurs ne sont pas valide, affiche un message
  # approprié. (Utilise l'étiquette lblReponse.)
  
  largeur = entLargeur.get()
  hauteur = entHauteur.get()
  
  try:
      largeur = int(largeur)
      hauteur = int(hauteur)
      if largeur <= 0 or hauteur <= 0:
          lblReponse['text'] = "Valeurs invalides"
      else:
          lblReponse['text'] = f"L'aire du rectangle est : {largeur * hauteur}"
          
  except:
      lblReponse['text'] = "Valeurs invalides"
  
# Que fait cette partie? Réponse: Crée la fenêtre tkinter avec ces paramètres
fenetre= tk.Tk()
fenetre.title("Aire d'un rectangle")
fenetre.config(bg = "#3967a8")

# Que fait cette partie? Réponse: Crée un label et lui donne des paramètres
lblTitre = tk.Label(fenetre)
lblTitre['text'] = "Aire d'un rectangle"
lblTitre['background'] = "#3967a8"
lblTitre['foreground'] = "#ffffff"
lblTitre['font'] = "Arial 20"
lblTitre.grid(row=0, column=0, columnspan=2, padx=30, pady=5) 

# Que fait cette partie? Réponse: Crée un label et lui donne des paramètres
lblLargeur = tk.Label(fenetre)
lblLargeur['text'] = "Largeur : "
lblLargeur['background'] = "#3967a8"
lblLargeur['foreground'] = "#ebebeb"
lblLargeur['font'] = "Arial 15 italic"
lblLargeur.grid(row=1 , column=0, padx=5, pady=5)

entLargeur = tk.Entry()
entLargeur['width'] = 15
entLargeur['font'] = "Arial 15"
entLargeur.grid(row=1, column=1, padx=5, pady=5)

# Que fait cette partie? Réponse: Crée un label et lui donne des paramètres
lblHauteur = tk.Label(fenetre)
lblHauteur['text'] = "Hauteur : "
lblHauteur['background'] = "#3967a8"
lblHauteur['foreground'] = "#ebebeb"
lblHauteur['font'] = "Arial 15 italic"
lblHauteur.grid(row=2 ,column=0 ,padx=5 ,pady=5 )

entHauteur = tk.Entry()
entHauteur['width'] = 15
entHauteur['font'] = "Arial 15"
entHauteur.grid(row=2,column=1,padx=5,pady=5)

# Que fait cette partie? Réponse: Crée un bouton et lui donne des paramètres, aussi une commande à executer lorsqu'on appui sur le bouton
btnCalculer = tk.Button(fenetre)
btnCalculer['text'] = "Calculer"
btnCalculer['font'] = "Arial 15"
btnCalculer['command'] = cliqueCalculer
btnCalculer.grid(row=3,column=1,padx=5, pady=5, ipadx=41) 

# Que fait cette partie? Réponse: Crée un label et lui donne des paramètres
lblReponse = tk.Label(fenetre)
lblReponse['text'] = ""
lblReponse['background'] = "#3967a8"
lblReponse['foreground'] = "#ebebeb"
lblReponse['font'] = "Arial 15  italic"
lblReponse.grid(row=4,column=0, columnspan=2, pady=10) 

# Que fait cette partie? Réponse: Execute la fenêtre tkinter
fenetre.mainloop()
