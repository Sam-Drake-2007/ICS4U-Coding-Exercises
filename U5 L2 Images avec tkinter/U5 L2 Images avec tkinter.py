import tkinter as tk

fen = tk.Tk()
fen.title("Voitures super rapides!")
fen.config(bg="#4287f5")
fen.geometry("1000x1000")

imgApolloPetit = tk.PhotoImage(file="apollo_petit.gif")
imgApolloGrand = tk.PhotoImage(file="apollo_grand.gif")

lblImageApolloPetit = tk.Label(image=imgApolloPetit)
lblImageApolloPetit.pack()

lblImageApolloGrand = tk.Label(image=imgApolloGrand)
lblImageApolloGrand.pack()

fen.mainloop()