# -*- coding: utf-8 -*-
"""
Created on Wed May 12 09:57:39 2021

@author: reena
"""

import requests
from bs4 import BeautifulSoup as BS
Base_URL='https://www.carpages.ca/'
my_useragent= {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
carlinks=[]
for i in range(1,3):
    my_request=requests.get(f'https://www.carpages.ca/used-cars/search/?num_results=50&search_radius=100&province_code=ab&city=calgary&sale_type=used&ll=51.0483,-113.9633&p={i}')
    my_soup=BS(my_request.content,'lxml')
    carlist=my_soup.find_all('div',class_='media')
    for car in carlist:
        for link in car.find_all('a',href=True):
            carlinks.append(Base_URL+link['href'])
print(len(carlinks))
carlinks = list(dict.fromkeys(carlinks))

print(len(carlinks))
#print(carlinks)
from selenium import webdriver
driver = webdriver.Firefox()
Cardict=[]
for i in carlinks:
    if i == 'https://www.carpages.ca//buy-from-home/':
        print(i)
    else:
        driver.get(i)
        carinfo=driver.find_element_by_class_name('vhcl-info__details')
        items = carinfo.find_elements_by_tag_name("li")
        cardata=['null','null','null','null','null','null','null','null','null','null']
        j=0
        for item in items:
            data = item.text   
            n=data.split("\n",1)[1] 
            cardata[j]=n   
            j=j+1
       
        price=driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "vhcl-info__price", " " ))]').text
       # price=priceinfo.find_elements_by_tag('h3')
        carprofile={}
        carprofile={
                'Price': price,
                'Exterior color':cardata[0],
                'Interior color':cardata[1],
                'Body Style': cardata[2],
                'Fuel Type': cardata[3],
                'Drive type': cardata[4],
                'Transmission': cardata[5],
                'Engine': cardata[6],
                'Doors': cardata[7],
                'Stock': cardata[8],
                'Mileage': cardata[9]}  
        Cardict.append(carprofile)
        print(i)
import pandas as pd
df=pd.DataFrame(Cardict)
df.to_csv('Carpages_data.csv')