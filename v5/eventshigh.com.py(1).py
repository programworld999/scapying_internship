#!/usr/bin/env python
# coding: utf-8

# In[18]:


import requests
from bs4 import BeautifulSoup as BS
import json
import mysql.connector
from art import *
import re
from tqdm import tqdm
import time


# In[19]:


try:
    page = requests.get("https://www.eventshigh.com/city/mumbai")
    print("URL is ok!")
except:
    print("Somting wrong in url")


# In[20]:


soup = BS(page.text, 'html.parser')
scraped_cards = soup.find_all(class_='ga-card-track')

interesting_urls = []
non_interesting_urls = []

for i in range(len(scraped_cards)):
    href = 'https://www.eventshigh.com'+scraped_cards[i].find('a').get('href')
    interesting_urls.append(href)

print(len(interesting_urls), interesting_urls)


# In[21]:


data = soup.find_all('a')

for i in data:
    url = i.get('href')
#     print(url)
    x = re.search("^http", str(url))
    if(x):
        url = url
    else:
        url = "https://www.eventshigh.com"+str(url)
    if(url != "https://www.eventshigh.comNone"):
        non_interesting_urls.append(url)
    
print(len(non_interesting_urls), non_interesting_urls)


# In[22]:


def mysqlConnectionInit():
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="1919",
            database="pythontwo"
        )
        print("Database connection is OK!")
        return db_connection
    except:
        print("Somting wrong in database connection")
        
mydb = mysqlConnectionInit()
mycursor = mydb.cursor()


# In[23]:


def Interesting_url():
    website = 'https://www.eventshigh.com'
    for url in interesting_urls:
        sql = "SELECT * FROM interesting_url WHERE url = %s AND website = %s"
        val = (url, website, )
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if(len(myresult) == 0):
            # print('Insertable')
            sql = "INSERT INTO interesting_url (url, website, status) VALUES (%s, %s, %s)"
            val = (url, website, 0)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                print("Interesting urls inserted")
            except:
                print('Somthing Worng ! Unable to Insert Intersting URLs')


            

Interesting_url()


# In[27]:


def Non_nteresting_url():
    website = 'https://www.eventshigh.com'
    for url in non_interesting_urls:
        sql = "SELECT * FROM non_interesting_url WHERE url = %s AND website = %s"
        val = (url, website, )
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if(len(myresult) == 0):
            # print('Insertable')
            sql = "INSERT INTO non_interesting_url (url, website) VALUES (%s, %s)"
            val = (url, website)
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                print("Non Interesting urls inserted")
            except:
                print('Somthing Worng ! Unable to Insert Non-Intersting URLs')

Non_nteresting_url()


# In[25]:



all_data = []
def scarping_single_event():
    website = 'https://www.eventshigh.com'
    sql = "SELECT * FROM interesting_url WHERE status = %s AND website = %s LIMIT 10"
    val = (0, website, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
#     print(myresult)
    events_url = []
    for event in myresult:
        event_url = event[1]
        events_url.append(event_url)
#     print(events_url)
    for i in tqdm(range(len(events_url))):
        details = requests.get(events_url[i])
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
        sql = "UPDATE interesting_url SET status = %s WHERE url = %s"
        val = (1, events_url[i], )
        mycursor.execute(sql, val)
        mydb.commit()
        
    
scarping_single_event()
# print(all_data)


# In[26]:


def insert_event_detail():
    website = 'https://www.eventshigh.com'
    for event in all_data:
#         print(event['url'], '\n')
        url = event['url']
        sql = "SELECT * FROM eventshigh_com WHERE url = %s"
        val = (url, )
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        
        if(len(myresult) == 0):
            sql = "INSERT INTO eventshigh_com (title, organizer, url, address, price, starting_date_time, ending_date_time) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (event['title'], event['organizer'], event['url'], event['address'], event['price'], event['starting_date_time'], event['ending_date_time'])
            try:
                mycursor.execute(sql, val)
                mydb.commit()
                print("Storing Event Details Is Done. Congaratulations!")
            except:
                print("Faild to insert data")
            
            
insert_event_detail()

