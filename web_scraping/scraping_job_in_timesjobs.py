import requests
from bs4 import BeautifulSoup


print('Enter some skill that you are not familiar with')
unfamiliar_skill=input('>')
print(f'Filtering out {unfamiliar_skill}')
url=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text
soup=BeautifulSoup(url,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
for job in jobs:
    published_date=job.find('span',class_='sim-posted').span.text
    if 'few' in published_date:
        job_title=job.find('strong',class_='blkclor').text
        company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skill=job.find('span',class_='srp-skills').text.replace(' ','')
        more_info=job.header.h2.a['href']
        if unfamiliar_skill not in skill:
            print(f"Langeuage:{job_title.strip()}")
            print(f"Company Name:{company_name.strip()}")
            print(f"required Skills:{skill.strip()}") 
            print(f"More Info:{more_info.strip()}")  
            
            print()