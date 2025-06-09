import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("the Digital Clock")

def time():
    string  = strftime("%H:%M:%S %p\n %d/%m/%y")
    label.config(text = string)
    label.after = (1000,time)
    
label = tk.Label(root,font=('Bell MT',67, 'bold'), background='wheat', foreground='black')
label.pack(anchor='center')

time()
root.mainloop()