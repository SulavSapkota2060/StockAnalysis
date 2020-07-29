import requests
from bs4 import BeautifulSoup as bs
from datetime import date
import datetime
import pandas as pd

def scraper(symbol):

    company = symbol
    start_date = str(date.today()-datetime.timedelta(days=10))
    end_date = str(date.today())
    sdD = datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    edD = datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    cpList = []
    date_list = []
    xl_list = []
    url = 'http://nepalstock.com/main/todays_price/index/1/total-share/asc/YTozOntzOjk6InN0YXJ0RGF0ZSI7czoxMDoiMjAyMC0wNy0wOCI7czoxMjoic3RvY2stc3ltYm9sIjtzOjQ6IkFLUEwiO3M6NjoiX2xpbWl0IjtzOjI6IjIwIjt9?startDate='+str(sdD)+'&stock-symbol='+company+'&_limit=20'
    
    for i in range((edD-sdD).days + 1):
        url = 'http://nepalstock.com/main/todays_price/index/1/total-share/asc/YTozOntzOjk6InN0YXJ0RGF0ZSI7czoxMDoiMjAyMC0wNy0wOCI7czoxMjoic3RvY2stc3ltYm9sIjtzOjQ6IkFLUEwiO3M6NjoiX2xpbWl0IjtzOjI6IjIwIjt9?startDate='+str(sdD)+'&stock-symbol='+company+'&_limit=20'
        r = requests.get(url)
        
        soup = bs(r.content,'lxml')
        try:
            cp = soup.select("table tr")[2]
        except IndexError as e:
            scraper(company)
            print('ERROR Retrying......')
        try:
           
            clp = cp.select("td")[5]
            
            price = clp.get_text()
            cpList.append(float(price))
            date_list.append(str(sdD))
            my_list = []
            my_list.append(str(sdD))
            my_list.append(float(price))
            xl_list.append(my_list)
            sdD += datetime.timedelta(days=1)

        except:
            sdD += datetime.timedelta(days=1)
    return cpList,date_list

 
    