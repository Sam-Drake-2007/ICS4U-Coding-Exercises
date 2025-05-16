import tkinter as tk

def reaction():
    strMot = entMessage.get()
    lblReaction.config(text=f"Tu as dit '{strMot}'\nTrop drôle!!!")

def caracteres():
    strMot = entMessage.get()
    lenMot = len(entMessage.get())
    lblCaracteres.config(text=f"La longeur de ton message '{strMot}' est: {lenMot} caractères!")
    
    
Fen = tk.Tk()
Fen.title("Réacion")
Fen.geometry("500x500")
Fen.config(bg="#ef684b")

lblMessage = tk.Label(Fen, text="Tape un mot drôle dans la zone de texte ci-dessous", bg="#ef684b")
lblMessage.pack()

entMessage = tk.Entry(Fen, justify="center")
entMessage.pack()

btnSoumettre = tk.Button(Fen, text="Soumettre", bg="#e9836d", command=reaction)
btnSoumettre.pack()

btnCaracteres = tk.Button(Fen, text="Nombre de caractères", bg="#e9836d", command=caracteres)
btnCaracteres.pack()

lblReaction = tk.Label(bg="#ef684b")
lblReaction.pack()

lblCaracteres = tk.Label(bg="#ef684b")
lblCaracteres.pack()


Fen.mainloop()