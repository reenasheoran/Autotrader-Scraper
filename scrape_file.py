# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:34:40 2021

@author: reena
"""
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd
my_useragent= {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56'}
job_listings=[]

for i in range(0,110,10):
    my_url='https://ca.indeed.com/jobs?q=data&l=Canada&start='+str(i)
    my_request=requests.get(my_url,my_useragent)
    #print(my_request.status_code) # to check response object
    my_soup= BS(my_request.content,'html.parser')
    #print(my_soup) To check the parsing of website
    data=my_soup.find_all('div',class_="jobsearch-SerpJobCard")
    #print(len(data))
    for job in data:
        #job_title= job.find('a').text
        job_title= job.find('a').text.strip()#strip removes white spaces
        #print(job_title)
        try:
            job_company=job.find('span',class_='company').text.strip()
       #job_company=job.find('span',{'class':'company'}).text.strip()#another way
        except:
           job_company=''
        #print(job_company)
        #when info is missing in some sections use try and except
        try:
            job_salary=job.find('span',class_='salaryText').text.strip()
        except:
            job_salary=''
        job_summary=job.find('div',class_='summary').text.strip().replace('\n','')
        job_info = {
            'TITLE' : job_title,
            'COMPANY': job_company,
            'SALARY': job_salary,
            'SUMMARY': job_summary}
        job_listings.append(job_info)
    print(i)
print(len(job_listings))
#print(job_listings)# check the data and refine it like I saw \n therefore I added replace in summary above
df=pd.DataFrame(job_listings)
df.head()
df.to_csv('joblistings.csv')