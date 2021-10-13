'''
1. this is scrappy API for HTML document
2. Configurated for table, img, str scrap


** Created by JHShin in Oct.2021 ** 

'''
from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import pandas as pd

def table_scrappy(input_url):
    page_url = input_url
    table_scrappy_db=[]

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
            table_scrappy_db.append(add_list)
        break


# need to change the source for drag area scrapping
def str_scrappy():
    page_url = input()
    str_scrappy_db = []

    # start the soup
    soup = BeautifulSoup(source, "html.parser")
    tables=soup.select('table') # fixed html tag

    str_html = str(tables)
    str_df_list = pd.read_html(str_html) # LIST type

    for i in range(1):
        add_list = str_df_list[0]
        str_scrappy_db.append(add_list)


    pass



def img_scrappy():
    pass