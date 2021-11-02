'''
1. this is scrappy API for HTML document
2. Configurated for table, img, str scrap
3. url input and scrapping all html structure
4. distribute data to other module
5. table_scp is display table tag 
6. string_scp is display p tag 

** Created by JHShin in Oct.2021 ** 
'''
from os import stat_result
from bs4 import BeautifulSoup
import urllib.request
import numpy as np

# search the url
def url_search(input):
    # initialize
    url = input
    data_tmp = []
    f = urllib.request.urlopen(url)
    source = f.read()

    #start the soup
    soup = BeautifulSoup(source, "html.parser")
    table = soup.find_all(['tb', 'table'])
    ### table = soup.select('table') # table tag scrap
    string = soup.find_all('p')
    ### string = soup.select('p') # p tag scrap

    data_tmp = table, string

    return data_tmp

'''
start the filtering to material blocks

'''

# filtered table tag and make drag&drop block
def table_scrappy(tables):
    ### tables is url_search(url)[0] ###
    table_html = tables

    ### return list of table tag
    return table_html

# filtered tag about string and make drag&drop block
def str_scrappy(string):
    ### tables is url_search(url)[1] ###
    str_html = string

    ### return list of p tag
    return str_html

### test
result = url_search("https://www.lawmaking.go.kr/opnPtcp/nsmLmSts/out?pageIndex=1");
print(table_scrappy(result[0]))
### print()
### print(str_scrappy(result[1]))