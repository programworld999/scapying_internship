#!/usr/bin/env python
# coding: utf-8

# In[57]:


import requests
from bs4 import BeautifulSoup as BS
import json

try:
    page = requests.get("https://insider.in/kolkata")
    print("URL is ok!")

except:
    print("Somting wrong in url")
    
soup = BS(page.text, 'html.parser')
scraped_cards = soup.find_all(class_='featured-card ')
# print(res[1])

all_events = []

i = 0

for i in range(len(scraped_cards)):
    all_events.append("https://insider.in"+scraped_cards[i].contents[0].get('href'))

# print(all_events)


if(len(all_events)<10):
    event_range = len(all_events)
else:
    event_range =10

    
    
##### ========================= ================== tests ===================================
"""
data = requests.get(all_events[0])
print(all_events[1])
soup = BS(data.text, "html.parser")
data = soup.find_all(type="application/ld+json")
data = data[0].text
print(data)
data = json.loads(data)
print("\n\n")

organization_name = data["performer"]['name']
title = data['name']
url = data['url']
address = data['location']['name']
price = data["offers"]["offers"][0]["price"]
starting_date_time = data["startDate"]
ending_date_time = data["endDate"]
    
    
print(ending_date_time)
"""

##### ========================= ================== tests ===================================

    
    

# for i in range(event_range):
#     data = requests.get(all_events[i])
#     soup = BS(data.text, "html.parser")
#     data = soup.find_all(type="application/ld+json")
#     data = data[0].text
#     print(data)
#     print("\n\n\n")
    

all_data = []

for i in range(event_range):
    details = requests.get(all_events[i])
    details_soup = BS(details.text, 'html.parser')
    data = details_soup.find_all("script", {'type': 'application/ld+json'})
    data = data[0].text
    data = json.loads(data)
    organization_name = data["performer"]['name']
    title = data['name']
    url = data['url']
    address = data['location']['name']
    price = data["offers"]["offers"][0]["price"]
    starting_date_time = data["startDate"]
    ending_date_time = data["endDate"]
    
    all_data.append({'organization_name': organization_name, 'title': title, 'url': url, 'address': address, 'price': price, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })
    
    print("Success!")



print("\n\n\n")
for i in range(len(all_data)):
    print(all_data[i])
    print("\n\n")
    

