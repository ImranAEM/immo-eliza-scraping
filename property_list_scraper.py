import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service



def get_urls(provinces: list):
    page = 1 #page number on immovlan, we start at 1
    max_page = 50
    provinces = ["hainaut", "antwerp", "east-flanders", "west-flanders", "brabant-wallon", "vlaams-brabant", "liege", "limburg", "luxembourg", "namur", "brussels"]

    """
    Loops through each province in the list, navigates pages of property listings on immovlan.be,
    extracts property URLs from each page, and writes them to a file ("url_list.txt").
    """
    for province in provinces:
        print(province)
        page = 1 #page number on immovlan, we start at 1

        driver = webdriver.Firefox()
        driver.set_page_load_timeout(1000)
        driver.get(F"https://immovlan.be/en/real-estate?propertytypes=house,apartment&propertysubtypes=residence,villa,bungalow,chalet,cottage,master-house,mansion,mixed-building,apartment,ground-floor,penthouse,duplex,triplex,studio,loft&provinces={province}&page={page}") # opening the first page containing the list of all houses and appartment per province
        print(f"province {province} page {page}")
        for article in driver.find_elements(By.CLASS_NAME,"list-view-item"):
            #properties.append(article.get_attribute('data-url'))
            with open("url_list.txt", "a") as f:
                    f.write(f"{article.get_attribute('data-url')}\n")

        #check for cookies with new provinces
        try:
            time.sleep(2)
            driver.find_element(By.XPATH, "//*[@id='didomi-notice-agree-button']").click()
        except:
            pass

        page += 1
        while page <= max_page:
            driver.get(F"https://immovlan.be/en/real-estate?propertytypes=house,apartment&propertysubtypes=residence,villa,bungalow,chalet,cottage,master-house,mansion,mixed-building,apartment,ground-floor,penthouse,duplex,triplex,studio,loft&provinces={province}&page={page}") # opening the first page containing the list of all houses and appartment per province
            print(f"province {province} page {page}")
            for article in driver.find_elements(By.CLASS_NAME,"list-view-item"):
                with open("url_list.txt", "a") as f:
                    f.write(f"{article.get_attribute('data-url')}\n")

            time.sleep(3)
            page += 1
        driver.quit()



get_urls(provinces[:4])
get_urls(provinces[4:8])
get_urls(provinces[8:])
