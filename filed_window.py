import tkinter as tk
from bs4 import BeautifulSoup
import pandas as pd
import requests

scrap = tk.Tk()

scrap.title("법안자동수집정리머신")
scrap.geometry("600x450")

display = tk.Entry(scrap, width=50)
display.pack()

def scrappy():
    page_url = input
    soup = BeautifulSoup(html_doc, 'html.parser')

    data=[]

    
    for no in notebook.tqdm(range(1, 76)):
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
        final_result.to_excel("result.xlsx")

display.bind('<Return>') 

scrap.mainloop()

