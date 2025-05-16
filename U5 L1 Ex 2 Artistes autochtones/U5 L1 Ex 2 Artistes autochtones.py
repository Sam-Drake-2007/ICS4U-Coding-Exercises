import tkinter as tk

objFen = tk.Tk()
objFen.title("Liste de mes artistes")
objFen.geometry("300x200")
objFen.configure(bg="#709174")

lblTitre = tk.Label(objFen, text="Artistes", font="Arial 20 bold", bg="#709174")
lblTitre.pack()

lblSousTitre = tk.Label(objFen, text="Liste de mes artistes préférés", font="Helvetica 12 italic", fg="#454545", bg="#709174")
lblSousTitre.pack()

for i in range(1, 6):
    lblArt = tk.Label(objFen, text=f"Artiste {i}", font="Helvetica 14", bg="#709174")
    lblArt.pack()

objFen.mainloop()