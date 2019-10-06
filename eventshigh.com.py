{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup as BS\n",
    "\n",
    "\n",
    "try:\n",
    "    page = requests.get(\"https://www.eventshigh.com/city/kolkata\")\n",
    "#     print(\"URL is ok!\")\n",
    "\n",
    "except:\n",
    "    print(\"Somting wrong in url\")\n",
    "    \n",
    "\n",
    "\n",
    "soup = BS(page.text, 'html.parser')\n",
    "scraped_cards = soup.find_all(class_='ga-card-track')\n",
    "# print(res[1])\n",
    "event_details = []\n",
    "i = 0\n",
    "for i in range(len(res)):\n",
    "    event_details.append(scraped_cards[1].find('a').get('href'))\n",
    "\n",
    "    \n",
    "    \n",
    "    \n",
    "details = requests.get('https://www.eventshigh.com/'+event_details[1])\n",
    "soup = BS(page.text, 'html.parser')\n",
    "title = soup.find(class_='eh-heading ')\n",
    "print(title)\n",
    "    \n",
    "    \n",
    "\n",
    "# for i in range(len(event_details)):\n",
    "#     details = requests.get('https://www.eventshigh.com/'+event_details[1])\n",
    "#     soup = BS(page.text, 'html.parser')\n",
    "#     title = soup.find(class_='eh-heading')\n",
    "#     print(title)\n",
    "#     print('Successfully scraping page no: '+str(i+1))\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
