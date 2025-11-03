import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

driver = webdriver.Firefox()

page = 1 #page number on immovlan, we start at 1
max_page = 50
driver.get(F"https://immovlan.be/en/real-estate?transactiontypes=for-rent,for-sale,in-public-sale,to-share&propertytypes=house,apartment&page={page}&noindex=1") # opening the first page containing the list of all houses and appartment

time.sleep(5)
# click cookies
driver.find_element(By.XPATH, "//*[@id='didomi-notice-agree-button']").click()

properties = []
while page <= max_page:
    driver.get(F"https://immovlan.be/en/real-estate?transactiontypes=for-rent,for-sale,in-public-sale,to-share&propertytypes=house,apartment&page={page}&noindex=1") # opening the first page containing the list of all houses and appartment
    print(f"page {page}")
    for article in driver.find_elements(By.CLASS_NAME,"list-view-item"):
        properties.append(article.get_attribute('data-url'))

    time.sleep(5)
    page += 1

driver.close()

with open("url_list.txt", "w") as f:
    for url in properties:
        f.write(f"{url}\n")
    f.write(str(properties))

print(properties)


#/html/body/div[1]/div[4]/div[3]/div/div[2]/div[2]/section/article[1]

#/html/body/div[1]/div[4]/div[3]/div/div[2]/div[2]/section/article[2]

