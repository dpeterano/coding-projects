import tkinter as tk

root = tk.Tk()
root.resizable(False,False)

entry = tk.Entry(width=50, font=("Arial",18),bd=10, relief=tk.RIDGE,justify='right')
entry.grid(row=0,column=0,columnspan=4)

def insert(t):
    entry.insert(tk.END, t)
def convert():
    try:
        result = entry.get()
        result = float(result) * 119.33
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"{str(result)} XPF")
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def reset():
    entry.delete(0, tk.END)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('.', 4, 2)
]

for(chiffre, ligne, col) in buttons:
    button = tk.Button(root, text=chiffre, width=30, height=4, command=lambda t=chiffre:insert(t))
    button.grid(row=ligne,column=col, padx=5,pady=5)

btn_equal = tk.Button(root, text='Convert', font=("Arial",8), width=100, height=4, command=convert)
btn_equal.grid(row=6,column=0,columnspan=4,padx=5,pady=5)

btn_reset = tk.Button(root, text='Reset', font=("Arial",8), width=100, height=4, command=reset)
btn_reset.grid(row=5,column=0,columnspan=4,padx=5,pady=5)

root.mainloop()