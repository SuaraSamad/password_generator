
import tkinter as tk
import math
from tkinter import*

window= Tk()
window.title("login")
window.geometry("500x500")
window.resizable(False,False)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=3)

username=tk.Label(window, text="username")
username.grid(column=0,row=0,sticky=tk.W,padx=5,pady=5)
username_entry = tk.Entry(window)
username_entry.grid(column=1,row=1,sticky=tk.W,padx=5,pady=5)

window.mainloop()
