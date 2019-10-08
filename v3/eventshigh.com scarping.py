#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup as BS
import json
import mysql.connector


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
    organizer = data["performer"][0]['name']
    title = data['name']
    url = data['url']
    address = data['location']['name']
    price = data["offers"][0]["price"]
    image = data["image"]
    starting_date_time = data["startDate"]
    ending_date_time = data["endDate"]
    
    all_data.append({'organizer': organizer, 'title': title, 'url': url, 'address': address, 'price': price, 'image': image, 'starting_date_time': starting_date_time, 'ending_date_time': ending_date_time })
    
    print("Success!")
    
for i in range(len(all_data)):
    print(all_data[i])
    print("\n\n")
    
    
    
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
        sql = "INSERT INTO eventshigh_com (title, organizer, url, address, price, starting_date_time, ending_date_time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
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
        val = (all_data[i]['url'], 'eventshigh.com')
        try:
            myquery.execute(sql, val)
            mydb.commit()
            print("Interesting urls inserted")
        except:
            print("Unable to insert Interesting urls")

Interesting_url()


def Non_interesting_url():
    for i in range(10, len(all_events)):
        sql = "INSERT INTO non_interesting_url (url, website) VALUES (%s, %s)"
        val = (all_events[i], 'eventshigh.com')
        try:
            myquery.execute(sql, val)
            mydb.commit()
            print("Non_interesting_urls inserted")
        except:
            print("Unable to insert Non_interesting_urls")
        


Non_interesting_url()


# In[ ]:




