from bs4 import BeautifulSoup

#print(soup.prettify())

import requests

#Get html from url
url = 'https://steamcharts.com/'
#url = 'https://bab.la/'
#url = 'https://www.google.com/'
#url = 'http://olympus.realpython.org/profiles/aphrodite'
req = requests.Session()
response = req.get(url)

#Convert to soup object
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)

#r = requests.get(url)
# print("bab.la")
#soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())

#print(soup.title)