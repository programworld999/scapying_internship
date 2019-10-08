import requests
from bs4 import BeautifulSoup as BS
import json

try:
    page = requests.get("https://www.eventshigh.com/city/kolkata")
#     print("URL is ok!")

except:
    print("Somting wrong in url")
    


soup = BS(page.text, 'html.parser')
scraped_cards = soup.find_all(class_='ga-card-track')
# print(res[1])
all_events = []
i = 0
for i in range(len(scraped_cards)):
    all_events.append('https://www.eventshigh.com'+scraped_cards[i].find('a').get('href'))

# print(events_detail)


####### ========================================== test =========================================

data = requests.get(all_events[0])
soup = BS(data.text, 'html.parser')
data = soup.find_all("script", {'type': 'application/ld+json'})

data = '{ "ALLDATA": '+ data[2].text+ '}'

data = json.loads(data)
data = data["ALLDATA"][0]
print(data)


organization_name = data["performer"][0]['name']
title = data['name']
url = data['url']
address = data['location']['name']
price = data["offers"][0]["price"]
image = data["image"]
starting_date_time = data["startDate"]
ending_date_time = data["endDate"]


####### ========================================== test =========================================




if(len(all_events)<10):
    event_range = len(all_events)
else:
    event_range =10

    
    
    
    
    
all_data = []

for i in range(event_range):
    details = requests.get(all_events[i])
    details_soup = BS(details.text, 'html.parser')
    data = details_soup.find_all("script", {'type': 'application/ld+json'})
    data = '{ "ALLDATA": '+ data[2].text+ '}'
    data = json.loads(data)
    data = data["ALLDATA"][0]
#     print(data)
    organization_name = data["performer"][0]['name']
    title = data['name']
    url = data['url']
    address = data['location']['name']
    price = data["offers"][0]["price"]
    image = data["image"]
    starting_date_time = data["startDate"]
    ending_date_time = data["endDate"]
    
    all_data.append({'organization_name': organization_name, 'title': title, 'url': url, 'address': address, 'price': price, 'image': image, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })
    
    print("Success!")
    


# In[30]:


# print(all_data)
for i in range(len(all_data)):
    print(all_data[i])
    print("\n\n")

