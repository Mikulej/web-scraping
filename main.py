from bs4 import BeautifulSoup

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
url = 'https://avi.im/stuff/js-or-no-js.html' # test url
#url = 'https://store.steampowered.com/'
page = driver.get(url)
p_element = driver.find_element(by=By.ID,value='intro-text')
print(p_element.text)
#soup = BeautifulSoup(page.text, 'lxml')
#Get html from url
# url = 'https://store.steampowered.com/'
# #url = 'http://olympus.realpython.org/profiles/aphrodite'

# #Convert to soup object
# #soup = BeautifulSoup(response.text, 'html.parser')
# soup = BeautifulSoup(text, 'lxml')
# featuredGames = soup.find_all('a',class_='store_main_capsule')
# print(soup.prettify())
# for link in featuredGames:
#     print("Featured game")
# carousels = soup.findAll(class_='carousel_items responsive_scroll_snap_ctn')
# carousel = carousels[0]
# # for link in carousel.findAll('a',class_="store_main_capsule responsive_scroll_snap_start broadcast_capsule"):
# # #for link in carousel.findAll.a:
# #     print("Featured game")

# carousel = carousels[1]
# for link in carousel.findAll('a',class_="store_capsule daily_deal"):
#     #for gameLink in link.findAll():
#     print("Capsule game")
#     #for gameLink in link.findAll('a'):
#         #print(gameLink)
#         #gameLink = link.find('a',href=True)
#     #print(link.prettify())
# #print(carousel)
# #print(soup.prettify())
