import tkinter as tk
from core import scrappy

scrap = tk.Tk()

scrap.title("법안자동수집정리머신")
scrap.geometry("450x600")
scrap.resizable(True, True)

scrappy

# the button invoke to download excel file
button = tk.Button(scrap, command=scrappy, overrelief="solid",text="Start", width=15, repeatdelay=1000, repeatinterval=100)
button.pack()

button.bind('<Return>') 

scrap.mainloop()

