import tkinter as tk

# Création du Canva

root = tk.Tk()
root.title("Calculatrice")
root.resizable(False,False)

# Entrée de texte

entry = tk.Entry(width="30",font=("Arial", 18), bd=10,relief=tk.RIDGE,justify="right")
entry.grid(row=0,column=0,columnspan=4)

# Fonction de concaténation dans la zone d'entrée

def add_car(c):
    entry.insert(tk.END, c)

# fonction de calcul qui remplace également la zone d'entrée par le résultat de l'eval

def calculate():
    try:
        expression = entry.get()
        resultat = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultat))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erreur")

def reset():
    entry.delete(0,tk.END)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Création des bouttons

for(texte, ligne, colonne) in buttons:
    if texte == '=':
        button = tk.Button(root, text=texte, width=5, height=2, font=("Arial", 18), command=calculate)
    else:
        button = tk.Button(root, text=texte, width=5, height=2, font=("Arial", 18), command=lambda t=texte: add_car(t))
    button.grid(row=ligne, column=colonne, padx=5, pady=5)

# Button 'C'

btn_reset = tk.Button(root,text='C', width=28,height=2,font=("Arial", 18), command=reset)
btn_reset.grid(row=5,column=0,columnspan=4,padx=5,pady=5)

root.mainloop()