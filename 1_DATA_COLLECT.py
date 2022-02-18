#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:12:14 2022
@author: fabien
"""


from bs4 import BeautifulSoup as bs
import pandas as pd, numpy as np
import requests

html_address = "https://fr.wikipedia.org/wiki/Liste_des_cath%C3%A9drales_inscrites_au_patrimoine_mondial"

############ Preambule : see element in html code (Ctrl+maj+J)
html_find = "wikitable"
table_slct = "tr" 

############ Get all cathedral info
r = requests.get(html_address)
# convert to bs project
soup = bs(r.content, 'html.parser')
# extract content
contents = soup.prettify()
cathdrals_table = soup.find_all(class_ = html_find)

dict_list = []
for cathdrals in cathdrals_table :
    list_ = cathdrals.select(table_slct)
    dict_index = []
    for i in range(len(list_)):
        if i == 0 :
            head = list_[0].find_all('th')
            for h in head :
                dict_index += [h.getText("", strip=True)]
        else :
            row_dict = {}
            row = list_[i].find_all('td')
            for j in range(len(row)):
                d = row[j].getText("", strip=True)
                row_dict[dict_index[j]] = d
                if j == 0 :
                    try:
                        row_dict['href'] = row[0].find('a')['href']
                    except Exception as e :
                        print(e,',', d)
            dict_list += [row_dict]
############ Find plan for each page

