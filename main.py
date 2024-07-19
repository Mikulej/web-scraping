from bs4 import BeautifulSoup
import requests as req

#Get html from url
url = 'https://store.steampowered.com/'
#url = 'http://olympus.realpython.org/profiles/aphrodite'

response = req.get(url)

#Convert to soup object
#soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.text, 'lxml')

carousels = soup.findAll(class_='carousel_items responsive_scroll_snap_ctn')
carousel = carousels[0]
for link in carousel.findAll('a',class_="store_main_capsule responsive_scroll_snap_start broadcast_capsule"):
    print("Featured game")

carousel = carousels[1]
for link in carousel.findAll('a',class_="store_capsule daily_deal"):
    #for gameLink in link.findAll():
    print("Capsule game")
    #for gameLink in link.findAll('a'):
        #print(gameLink)
        #gameLink = link.find('a',href=True)
    #print(link.prettify())
#print(carousel)
#print(soup.prettify())
