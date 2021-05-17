# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:20:21 2021

@author: reena
"""

import requests
from bs4 import BeautifulSoup as BS
Base_URL='https://www.carpages.ca/'
my_useragent= {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
carlinks=[]
for i in range(1,50,50):#not getting more than 110 records so kept it to 200 only
    my_request=requests.get(f'https://www.carpages.ca/used-cars/search/?num_results=50&search_radius=100&province_code=ab&city=calgary&sale_type=used&ll=51.0483,-113.9633&p={i}')
    my_soup=BS(my_request.content,'lxml')
    carlist=my_soup.find_all('div',class_='media')
    for car in carlist:
        for link in car.find_all('a',href=True):
            carlinks.append(Base_URL+link['href'])
print(len(carlinks))
#print(carlinks)
from selenium import webdriver
driver = webdriver.Firefox()
Cardata=[]
for i in carlinks:
    driver.get(carlinks[1])
    name=driver.find_element_by_xpath(xpath='//*[contains(concat( " ", @class, " " ), concat( " ", "hero-title", " " ))]')
    Cartype=name.text
    price=driver.find_element_by_xpath(xpath='//*[contains(concat( " ", @class, " " ), concat( " ", "hero-price", " " ))]')
    Carprice=price.text
    km=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-0")]')
    Km_travelled=km.text
    trim=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-2")]')
    Trim=trim.text
    BT=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-3")]')
    BodyType=BT.text
    Eng=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-4")]')
    Engine=Eng.text
    Cyl=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-5")]')
    Cylinder=Cyl.text
    Trans=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-6")]')
    Transmission=Trans.text
    DT=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-7")]')
    DriveTrain=DT.text
    SN=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-8")]')
    Stock_number=SN.text
    door=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-10")]')
    Doors=door.text
    FT=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-11")]')
    Fuel_Type=FT.text
    citympg=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-12")]')
    City_mpg=citympg.text
    Hwympg=driver.find_element_by_xpath(xpath='//*[(@id = "spec-value-13")]')
    Highway_mpg=Hwympg.text
    carprofile={
        'CarModel':Cartype,
        'Price':Carprice,
        'Km_travelled':Km_travelled,
        'Trim':Trim,
        'Body_Type':BodyType,
        'Engine':Engine,
        'Cylinder':Cylinder,
        'Transmission':Transmission,
        'DriveTrain':DriveTrain,
        'Stock_Number':Stock_number,
        'Color':Color,
        'Doors':Doors,
        'Fuel_Type':Fuel_Type,
        'City_mpg':City_mpg,
        'Highway_mpg':Highway_mpg
        }
    Cardata.append(carprofile)
    print(i)
import pandas as pd
df=pd.DataFrame(Cardata)
df.to_csv('Car_data.csv')