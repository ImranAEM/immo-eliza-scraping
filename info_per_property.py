from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
import re


def get_soup(url:str) -> BeautifulSoup:
    # initiate driver and getting the page
    driver = webdriver.Firefox()
    driver.get(url) # opening the property's page

    # click cookies
    time.sleep(5)
    driver.find_element(By.XPATH, "//*[@id='didomi-notice-agree-button']").click()

    # get html
    soup = BeautifulSoup(driver.page_source, "html.parser")

    driver.quit()

    return soup

def get_info(soup: BeautifulSoup) -> dict:
    property_info ={"id" : soup.find(class_="vlancode").text, "property type" : soup.find("h1").text}
    print(property_info['property type'])
    for info_box in soup.find(class_="general-info-wrapper").find_all(class_="data-row-wrapper"):
        for info_name, info in zip(info_box.find_all("h4"), info_box.find_all("p")):
            property_info[info_name.text] = info.text

    return property_info

def all_properties_info(properties: list[str]) -> dict:
    properties_info = {}
    for property_url in properties:
        print(property_url)
        info = get_info(get_soup(property_url))
        properties_info[info["id"]] = info

    return properties_info


list_of_properties = ['https://immovlan.be/en/detail/villa/for-sale/7180/seneffe/vwd15538', 'https://immovlan.be/en/detail/apartment/for-rent/1410/waterloo/vbd47706', 'https://immovlan.be/en/detail/residence/for-sale/7090/hennuyeres/rbu63284', 'https://immovlan.be/en/detail/residence/for-rent/6830/bouillon/vbd47666', 'https://immovlan.be/en/detail/duplex/for-rent/9300/aalst/rbu63264', 'https://immovlan.be/en/detail/apartment/for-rent/9150/bazel/rbu63097', 'https://immovlan.be/en/detail/mixed-building/for-sale/9688/schorisse/rbu63087', 'https://immovlan.be/en/detail/residence/for-sale/9630/zwalm/rbu62977', 'https://immovlan.be/en/detail/apartment/for-rent/2600/berchem/rbu62725', 'https://immovlan.be/en/detail/apartment/for-rent/2000/antwerp/rbu62723', 'https://immovlan.be/en/detail/residence/for-rent/8211/aartrijke/rbu62717', 'https://immovlan.be/en/detail/loft/for-rent/1080/sint-jans-molenbeek/vbd47427', 'https://immovlan.be/en/detail/residence/for-sale/5190/jemeppe-sur-sambre/vbd47422', 'https://immovlan.be/en/detail/apartment/for-sale/8210/zedelgem/rbu62613', 'https://immovlan.be/en/detail/apartment/for-sale/2840/rumst/rbu62593', 'https://immovlan.be/en/detail/residence/for-sale/8552/moen/rbu62561', 'https://immovlan.be/en/detail/residence/for-sale/8560/gullegem/rbu62532']
#list_of_properties_projects = ['https://immovlan.be/en/projectdetail/24431-p-vk0101-tfjkrblr', 'https://immovlan.be/en/projectdetail/25733-4036945', 'https://immovlan.be/en/detail/villa/for-sale/7180/seneffe/vwd15538', 'https://immovlan.be/en/detail/apartment/for-rent/1410/waterloo/vbd47706', 'https://immovlan.be/en/detail/residence/for-sale/7090/hennuyeres/rbu63284', 'https://immovlan.be/en/detail/residence/for-rent/6830/bouillon/vbd47666', 'https://immovlan.be/en/detail/duplex/for-rent/9300/aalst/rbu63264', 'https://immovlan.be/en/detail/apartment/for-rent/9150/bazel/rbu63097', 'https://immovlan.be/en/detail/mixed-building/for-sale/9688/schorisse/rbu63087', 'https://immovlan.be/en/detail/residence/for-sale/9630/zwalm/rbu62977', 'https://immovlan.be/en/detail/apartment/for-rent/2600/berchem/rbu62725', 'https://immovlan.be/en/detail/apartment/for-rent/2000/antwerp/rbu62723', 'https://immovlan.be/en/detail/residence/for-rent/8211/aartrijke/rbu62717', 'https://immovlan.be/en/detail/loft/for-rent/1080/sint-jans-molenbeek/vbd47427', 'https://immovlan.be/en/detail/residence/for-sale/5190/jemeppe-sur-sambre/vbd47422', 'https://immovlan.be/en/detail/apartment/for-sale/8210/zedelgem/rbu62613', 'https://immovlan.be/en/detail/apartment/for-sale/2840/rumst/rbu62593', 'https://immovlan.be/en/detail/residence/for-sale/8552/moen/rbu62561', 'https://immovlan.be/en/detail/residence/for-sale/8560/gullegem/rbu62532']

#print(all_properties_info(list_of_properties))

print(get_info(get_soup('https://immovlan.be/en/detail/villa/for-sale/7180/seneffe/vwd15538')))
#print(get_info(get_soup('https://immovlan.be/en/projectdetail/1485771-01267921_om_272263')))