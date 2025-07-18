import tkinter as tk

root = tk.Tk()
root.title("Currency Converter")
root.resizable(False,False)

def converts(rate):
    try:
        expression = entry.get()
        resultat = float(expression) * float(rate)
        entry.delete(0,tk.END)
        entry.insert(tk.END, f"{resultat:.2f}")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def insert_rate(a):
    changeentry.delete(0, tk.END)
    changeentry.insert(tk.END, a)

entry_label = tk.Label(root, text="Entry")
entry_label.grid(row=0, column=0, columnspan=4)
entry = tk.Entry(width="40", font=("Arial", 18), relief=tk.RIDGE, justify="center", bd=8)
entry.grid(row=1, column=0, columnspan=4)

change_rate = [
    ("XPF",2,0,0.00974),("EUR",2,1, 1.162),("GBP",3,0,1.342),("NZD",3,1,0.595)
]

for (currency, ligne, colonne, taux) in change_rate:
    button = tk.Button(root, text=currency, width=20, height=5, command=lambda t=taux:insert_rate(t))
    button.grid(row=ligne,column=colonne,columnspan=1,padx=5,pady=5)

changeentry_label = tk.Label(root, text="Change Rate")
changeentry_label.grid(row=0, column=4, columnspan=5)
changeentry = tk.Entry(width="10", font=("Arial", 18), relief=tk.RIDGE, justify="center", bd=8)
changeentry.grid(row=1, column=5, columnspan=4)

convert = tk.Button(root, text="Convert",command=lambda : converts(float(changeentry.get())), font=("Arial",14))
convert.grid(row=2,column=4,columnspan=4,padx=5,pady=5)


root.mainloop()