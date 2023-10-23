import tkinter as tk

OL1 = [
"USD", "EUR","INR",

]

OL2 = [
"INR",
"srilankars","USD", "EUR"
]

def Ok():

    fr = variable.get()
    to = variable1.get()

    amount = float(e1.get())

    if (fr == "USD" and to == "INR"):

        total = amount * 80
    elif (fr == "EUR" and to == "INR"):
    
        total = amount * 90
    elif (fr == "INR" and to == "USD"):
    
        total = amount / 80
    elif (fr == "INR" and to == "EUR"):
    
        total = amount / 90

    else:
        total = amount *325

    nsalText.set(total)

root = tk.Tk()
root.geometry('600x200')
root.title("Currency Converter")

variable = tk.StringVar(root)
variable.set(OL1[0])

opt = tk.OptionMenu(root, variable, *OL1)
opt.config(width=10, font=('Segoe UI', 12))
opt.pack(side="top")

variable1 = tk.StringVar(root)
variable1.set(OL2[0])

opt = tk.OptionMenu(root, variable1, *OL2)
opt.config(width=10, font=('Segoe UI', 12))
opt.pack(side="top")

global e1
global nsalText
nsalText = tk.StringVar()
labelTest = tk.Label(text="", font=('Segoe UI', 12), fg='red')
labelTest.pack(side="top")


tk.Label(root, text="From").place(x=10, y=10)
tk.Label(root, text="To").place(x=10, y=40)
tk.Label(root, text="Amount").place(x=10, y=80)

tk.Label(root, text="Total:").place(x=10, y=150)
tk.Label(root, text="", font=('Segoe UI', 12), fg='red' , textvariable=nsalText).place(x=100, y=150)
tk.Button(root, text="Calculate", command=Ok ,height = 1, width = 5).place(x=100, y=110)

e1 = tk.Entry(root)
e1.place(x=80, y=80)

root.mainloop()
