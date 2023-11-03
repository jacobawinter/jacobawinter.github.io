#get_schedule.py
# Nov 2, 2023
# Grab content from Toronto rec website to display locally

import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

now = datetime.datetime.now()
now = now.strftime("%a %b %d")

def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    tab = soup.find_all(id = 'dropin_Swimming_0') # get drop in swimming table
    rows = pd.read_html(str(tab))[0]
    rows = rows[rows['Program'] == 'Lane Swim (7yrs and over)']
    return(rows)

jimmie = get_data("https://www.toronto.ca/data/parks/prd/facilities/complex/58/index.html")
pam = get_data("https://www.toronto.ca/data/parks/prd/facilities/complex/2012/index.html")

place = ['Jimmie Simpson', 'Pam McConnell']

#concat dataframes
df = pd.concat([jimmie, pam], ignore_index=True)

#df = jimmie.append(pam)
df["Location"] = ['Jimmie Simpson', 'Pam McConnell']
df = df.drop(columns=['Program'])

#Put location column first
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

#save as html table
html = df.to_html(index = False)
# html = html.replace('<table border="1" class="dataframe">', '<table class="table table-striped">')
html = html.replace('<thead>', '<thead class="thead-dark">')
html = html.replace('<tr style="text-align: right;">','<tr>')
html = html.replace('<tr>','<tr class="table-primary">')


#write to html file
f = open('pool_schedule.html','w')
f.write(html)
f.close()

#Today
today = df[['Location', now]]


#save as html table
html = today.to_html(index = False)
html = html.replace('<table border="1" class="dataframe">', '<table class="table table-striped">')
html = html.replace('<thead>', '<thead class="thead-dark">')
html = html.replace('<tr style="text-align: right;">','<tr>')
html = html.replace('<tr>','<tr class="table-primary">')


#write to html file
f = open('today.html','w')
f.write(html)
f.close()

