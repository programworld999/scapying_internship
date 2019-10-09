#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
from bs4 import BeautifulSoup as BS
import json
import mysql.connector
import re
from art import *


try:
    page = requests.get("https://naadyogacouncil.com")
    print("URL is ok!")

except:
    print("Somting wrong in url")
    
soup = BS(page.text, 'html.parser')

all_events = []
a = soup.find_all('a')
for i in range(len(a)):
    urls = a[i].get("href")    
    x = re.search("^https://naadyogacouncil.com/event/", urls)
    y = re.search("^http://naadyogacouncil.com/event/", urls)
    if(x or y):
        all_events.append(urls)
        print(urls)
        print("\n")
        
        
        

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
        price = "£"+data["offers"]["price"]
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
        print("Success!")
        all_data.append({'organizer': organizer, 'title': title, 'url': url, 'address': address, 'price': price, 'image': image, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })
#         print(organizer)
#         print(title)
#         print(url)
#         print(address)
#         print(price)
#         print(image)
#         print(starting_date_time)
#         print(ending_date_time)
#         print("===============================================================================================")
#         print("\n")

for i in range(len(non_structed_data_web)):
    details = requests.get(non_structed_data_web[i])
    details_soup = BS(details.text, 'html.parser')
    data = details_soup.find_all("script", {'type': 'application/ld+json'})
    data = data[1].text
#     print(data)
    data = json.loads(data)
    data = data[0]
    try:
        organizer = data["organizer"]['name']
        title = data['name']
        url = data['url']
        address = data['location']['name']
        price = "N/A"
        image = "N/A"
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
    all_data.append({'organizer': organizer, 'title': title, 'url': url, 'address': address, 'price': price, 'image': image, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })

    print("Success!")

print("Success!")
print("\n"+ str(len(all_data)))
for i in range(len(all_data)):
    print(all_data[i])

    
    
    
    
    

    
def mysqlConnectionInit():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1919",
            database="python"
        )
        print("Database connection is OK!")
        return db_connection
    except:
        print("Somting wrong in database connection")
        
mydb = mysqlConnectionInit()
myquery = mydb.cursor()

def insertDetailToDatabase():
    for i in range(len(all_data)):
        sql = "INSERT INTO naadyogacouncil_com (title, organizer, url, address, price, starting_date_time, ending_date_time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (all_data[i]['title'], all_data[i]['organizer'], all_data[i]['url'], all_data[i]['address'], all_data[i]['price'], all_data[i]['starting_date_time'], all_data[i]['ending_date_time'])
        try:
            myquery.execute(sql, val)
            mydb.commit()
            print("Scraping and Storing Everything Is Done. Congaratulations!")
        except:
            print("Unable to insert data")

insertDetailToDatabase()

def Interesting_url():
    for i in range(len(all_data)):
        sql = "INSERT INTO interesting_url (url, website) VALUES (%s, %s)"
        val = (all_data[i]['url'], 'insider.in')
        try:
            myquery.execute(sql, val)
            mydb.commit()
            print("Interesting urls inserted")
        except:
            print("Unable to insert Interesting urls")

Interesting_url()



    


# In[6]:



############################ Non-Interesting URLS ###################


urls = soup.find_all("a")
all_non_intersted_urls = []

for i in range(len(urls)):
    url = urls[i].get('href')
    x = re.search("^http", url)
    if(x):
        url = url
    else:
        url = "https://naadyogacouncil.com"+url
    all_non_intersted_urls.append(url)


def Non_interesting_url():
    for i in range(10, len(all_non_intersted_urls)):
        sql = "INSERT INTO non_interesting_url (url, website) VALUES (%s, %s)"
        val = (all_non_intersted_urls[i], 'naadyogacouncil.com')
        try:
            myquery.execute(sql, val)
            mydb.commit()
            print("Non_interesting_urls inserted")
        except:
            print("Unable to insert Non_interesting_urls")
        


Non_interesting_url()

############################ Non-Interesting URLS ###################




tprint("Successful!")

