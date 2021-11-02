'''
1. this is scrappy API for HTML document
2. Configurated for table, img, str scrap
3. url input and scrapping all html structure
4. distribute data to other module
5. table_scp is display table tag 
6. string_scp is display p tag 

** Created by JHShin in Oct.2021 ** 
'''
from bs4 import BeautifulSoup
import urllib.request
import numpy as np
import pandas as pd

# searched & scrapped all tag components in the url
def url_search(input):
    # initialize
    url = input
    data_tmp = []
    f = urllib.request.urlopen(url)
    source = f.read()

    #start the soup
    soup = BeautifulSoup(source, "html.parser")
    table = soup.select('tb') # table tag scrap
    string = soup.select('p') # p tag scrap

    data_tmp = str(table), str(string)

    return 
    pass

'''
start the filtering to material blocks

'''

# filtered table tag and make drag&drop block
def table_scrappy(input_url):
    table_scrappy_db=[]

    table_html = str(tables)
    table_df_list = pd.read_html(table_html) # LIST type

    # <tb> to </tb> 까지 한개의 유닛
    # 

    for i in range(1):
        add_list = table_df_list[0]
        table_scrappy_db.append(add_list)



    pass 


# filtered tag about string and make drag&drop block
def str_scrappy(input_url):

    str_html = str(string)
    str_df_list = pd.read_html(str_html) # LIST type

    for i in range(1):
        add_list = str_df_list[0]
        str_scrappy_db.append(add_list)


    pass
