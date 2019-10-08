#!/usr/bin/env python
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup as BS
import json
import mysql.connector




class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# print(color.BOLD + 'Hello World !' + color.END)







try:
    page = requests.get("https://naadyogacouncil.com")
    print("URL is ok!")

except:
    print("Somting wrong in url")
    
soup = BS(page.text, 'html.parser')


# In[31]:




all_events = [
"https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-2/",
"http://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-veer-kaur/",
"https://naadyogacouncil.com/event/naad-yoga-teacher-training-germany-2/",
"https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-3/",
"https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-4/"
]

# print(all_events)


if(len(all_events)<10):
    event_range = len(all_events)
else:
    event_range =10

    

all_data = []
non_structed_data_web = []
for i in range(event_range):
    details = requests.get(all_events[i])
    details_soup = BS(details.text, 'html.parser')
    data = details_soup.find_all("script", {'type': 'application/ld+json'})
    data = data[1].text
    data = json.loads(data)[0]    
#     print(data)
#     print("\n\n")
    try:
        organizer = data["organizer"]['name']
        title = data['name']
        url = data['url']
        address = data['location']['name']
        price = data["offers"]["price"]
        image = data["image"]
        starting_date_time = data["startDate"]
        ending_date_time = data["endDate"]
    except:
        organizer = "N/A"
        title = "N/A"
        url = "N/A"
        address = "N/A"
        price  = "N/A"
        image = "N/A"
        starting_date_time = "N/A"
        ending_date_time = "N/A"
        
    if(organizer == "N/A"):
        non_structed_data_web.append(all_events[i])
#         print("This event have no structed data")
#         print(all_events[i])
    else:
        all_data.append({'organization_name': organization_name, 'title': title, 'url': url, 'address': address, 'price': price, 'image': image, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })
        print(organization_name)
        print(title)
        print(url)
        print(address)
        print(price)
        print(image)
        print(starting_date_time)
        print(ending_date_time)
        print("===============================================================================================")
        print("\n")
  

for i in range(len(non_structed_data_web)):
    details = requests.get(non_structed_data_web[i])
    details_soup = BS(details.text, 'html.parser')
    data = details_soup.find_all("script", {'type': 'application/ld+json'})
    data = data[1].text
#     print(data)
    data = json.loads(data)
    data = data[0]
    organizer = data["organizer"]['name']
    title = data['name']
    url = data['url']
    address = data['location']['name']
    price = "N/A"
    image = "N/A"
    starting_date_time = data["startDate"]
    ending_date_time = data["endDate"]
    all_data.append({'organization_name': organization_name, 'title': title, 'url': url, 'address': address, 'price': price, 'image': image, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })
    print(organization_name)
    print(title)
    print(url)
    print(address)
    print(price)
    print(image)
    print(starting_date_time)
    print(ending_date_time)
    print("===============================================================================================")
    print("\n")





print(color.BOLD+color.GREEN+"Success!"+color.END)


# In[27]:


for i in range(len(non_structed_data_web)):
    details = requests.get(non_structed_data_web[i])
    details_soup = BS(details.text, 'html.parser')
    data = details_soup.find_all("script", {'type': 'application/ld+json'})
    print("length is : "+str(len(data)))
    data = data[1].text
#     print(data)
    data = json.loads(data)
    data = data[0]
    organizer = data["organizer"]['name']
    title = data['name']
    url = data['url']
    address = data['location']['name']
    price = "N/A"
    image = "N/A"
    starting_date_time = data["startDate"]
    ending_date_time = data["endDate"]

    all_data.append({'organization_name': organization_name, 'title': title, 'url': url, 'address': address, 'price': price, 'image': image, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })
    


# In[23]:


event = "https://naadyogacouncil.com/event/heartspace-sound-meditation-naad-yoga-2/"
page = requests.get(event)
soup = BS(page.text, 'html.parser')
data = soup.find_all("script", {'type': 'application/ld+json'})

data = data[1].text
# print(data)
print("\n")

data = json.loads(data)
data = data[0]

all_data = []
organization_name = data["organizer"]['name']
title = data['name']
url = data['url']
address = data['location']['name']
price = data["offers"]["price"]
image = data["image"]
starting_date_time = data["startDate"]
ending_date_time = data["endDate"]
    
all_data.append({'organization_name': organization_name, 'title': title, 'url': url, 'address': address, 'price': price, 'image': image, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })

print(all_data)

