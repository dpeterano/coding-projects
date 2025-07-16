import tkinter as tk

root = tk.Tk()
root.resizable(False,False)

def cal():
    try:
        expression = entry.get()
        resultat = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultat))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def insertion(t):
    if entry.get() == "Error":
        entry.delete(0, tk.END)
    if entry.get().endswith('.') == True:
        return
    entry.insert(tk.END, t)
def clear():
    entry.delete(0, tk.END)

entry = tk.Entry(width="32", font=("Arial Bold", 18),bd=10, relief=tk.RIDGE,justify='right')
entry.grid(row=0,column=0,columnspan=4)

buttons = [
    ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
    ('0',4,1),('.',4,2),('+',4,3)
]

for (texte, ligne, colonne) in buttons:
    button = tk.Button(root, text=texte, width=15, height=2, command=lambda t=texte:insertion(t))
    button.grid(row=ligne, column=colonne, padx=5, pady=5)

btn_clear = tk.Button(root, width=15, text='C', height=2,command=clear)
btn_clear.grid(row=4,column=0, padx=5, pady=5)

btn_equal = tk.Button(root, width=40, text='=', height=3,command=cal)
btn_equal.grid(row=5,column=0, columnspan=4, padx=5, pady=5)

root.mainloop()