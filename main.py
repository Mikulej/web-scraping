from bs4 import BeautifulSoup

from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#Initialize webdriver
options = ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = Chrome(options=options)

#Render html from url
#url = 'https://avi.im/stuff/js-or-no-js.html' # test url
url = 'https://store.steampowered.com/'
driver.get(url)

print("\nFeatured Games:")

elements = driver.find_elements(By.CLASS_NAME, 'store_main_capsule')

for WebElement in elements:
   #Convert Selenium's WebElement to Soup
   elementHTML = WebElement.get_attribute('outerHTML') #gives exact HTML content of the element
   elementSoup = BeautifulSoup(elementHTML,'html.parser')

   #Get game name
   name = elementSoup.find(class_="app_name").text

   #Get game link
   link = elementSoup.find('a').get('href')

   #Get game price
   price = elementSoup.find(class_="discount_final_price")
   if(price != None):
      price = price.text
    #Get producent
#    subdriver = Chrome()
#    subdriver.get(link)
#    #check if has button
#    elements = driver.find_elements(By.ID, 'view_product_page_btn')
#    if len(elements) > 0:
#       print("Has button!")
#    else:
#       print("No button!")
# #    try:
#       button = subdriver.find_element(By.ID, 'view_product_page_btn')
#       print("Has button!")
#    except any:
#       print("No button!")
#   subdriver.implicitly_wait(0.5)

   

   print(name, " ", price, " ", link)
   

print("\nDaily sales:")

elements = driver.find_elements(By.CLASS_NAME, 'store_capsule')

for WebElement in elements:
    #Convert Selenium's WebElement to Soup
   elementHTML = WebElement.get_attribute('outerHTML') #gives exact HTML content of the element
   elementSoup = BeautifulSoup(elementHTML,'html.parser')

   #Get game name
   name = elementSoup.find('img').get('alt')

   #Get game link
   link = elementSoup.find('a').get('href')

   #Get game price
   price = elementSoup.find(class_="discount_final_price")
   if(price != None):
      price = price.text
   print(name, " ", price," ",link)
   #print(elementSoup.prettify())
