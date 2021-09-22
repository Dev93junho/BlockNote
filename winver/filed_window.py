import tkinter as tk
from bs4 import BeautifulSoup
import urllib.request
import numpy as np
# from tqdm import trange, notebook
import pandas as pd
# import requests

scrap = tk.Tk()

scrap.title("법안자동수집정리머신")
scrap.geometry("450x600")
scrap.resizable(True, True)


def scrappy():
    page_url = input
    # soup = BeautifulSoup(html_doc, 'html.parser')


    page_url = 'https://www.lawmaking.go.kr/opnPtcp/nsmLmSts/out?pageIndex='
    data=[]

    for no in range(1, 76):
        url = page_url + str(no)
        f = urllib.request.urlopen(url)
        source = f.read()
        
        # start the soup 
        soup = BeautifulSoup(source, "html.parser")
        tables=soup.select('table') # fixed html tag

        table_html = str(tables)
        table_df_list = pd.read_html(table_html) # LIST type

        for i in range(1):
            add_list = table_df_list[0]
            data.append(add_list)

        # Data framing
        X= np.array(data).reshape(-1, 6)
        df = pd.DataFrame(X)

        # change the order
        df.columns = ['의안명','발의의원', '상임위', '국회현황', '의결결과','의안번호']
        final = df[['의안번호', '국회현황','발의의원','의안명','의결결과','상임위']]
        final.to_excel("result.xlsx")


# the button invoke to download excel file
button = tk.Button(scrap, command=scrappy, overrelief="solid",text="Start", width=15, repeatdelay=1000, repeatinterval=100)
button.pack()

button.bind('<Return>') 

scrap.mainloop()

