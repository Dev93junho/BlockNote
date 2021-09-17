import tkinter as tk
from bs4 import BeautifulSoup
import pandas as pd
import requests

scrap = tk.Tk()

scrap.title("법안자동수집정리머신")
scrap.geometry("600x450")

display = tk.Entry(scrap, width=50)
display.pack()

display.bind('<Return>') 

scrap.mainloop()

