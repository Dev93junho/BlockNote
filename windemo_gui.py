import tkinter as tk
from core import scrappy

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.inner_widgets()

    def inner_widgets(self):
        self.scrap = tk.Button(self)
        self.scrap["text"] = "Scarp!"
        self.scrap["command"] = self.scrap_func
        # self.scrap["overreilf"] = "solid"
        self.scrap.pack(side="top")

    def scrap_func(self):
        scrappy


root = tk.Tk()

# root.title("법안자동수집정리머신")
# root.geometry("450x600")
# root.resizable(True, True)


app = Application(master=root)
app.mainloop

# # the button invoke to download excel file
# button = tk.Button(scrap, command=scrappy, overrelief="solid",text="Start", width=15, repeatdelay=1000, repeatinterval=100)
# button.pack()

# button.bind('<Return>') 
