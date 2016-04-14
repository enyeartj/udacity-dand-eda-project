# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 09:20:24 2016

@author: warg
"""

import csv
import requests
from pprint import pprint
from bs4 import BeautifulSoup

website = 'https://en.wikipedia.org/wiki/List_of_cities_in_Nevada'
csvOut = 'C:/p4/nvCityCountyPop.csv'

def requestPage(url):
    r = requests.get(url)
    return r.text

if __name__ == '__main__':
    p = requestPage(website)
    s = BeautifulSoup(p, 'html.parser')
    table0 = s.find_all('table')[0]
    table1 = s.find_all('table')[1]
    
    rows0 = table0.find_all('tr')
    rows1 = table1.find_all('tr')
    
    data_w_empty = []
    for row in rows0:
        cols = row.find_all('td')
        cols = [e.text.strip() for e in cols]
        data_w_empty.append([e for e in cols if e])
    for row in rows1:
        cols = row.find_all('td')
        cols = [e.text.strip() for e in cols]
        data_w_empty.append([e for e in cols if e])
    
    # "remove" empty rows and Settlement Type column
    data = []
    for row in data_w_empty:
        if row != []:
            data.append([row[0], row[-2], int(row[-1].replace(',',''))])
    
    # add headers
    data.insert(0,['city', 'county', 'city_pop'])
    
    # clean up city names
    for r in range(len(data)):
        if u' \u2020' in data[r][0]:
            i = data[r][0].find(u' \u2020')
            data[r][0] = data[r][0][:i]
    
    # check our work
    pprint(data)
    
    with open(csvOut, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(data)