from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.by import By
import re
import json
import csv

from check_convert_data import clean_property_data_output
def get_soup(url:str) -> tuple[BeautifulSoup,str]:
    # initiate driver and getting the page
    driver = webdriver.Firefox()
    driver.get(url) # opening the property's page

    # click cookies
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "//*[@id='didomi-notice-agree-button']").click()
    except Exception as e:
        print(f"Error for clicking cookies   : {e} in url {url}")
    # get html
    soup = BeautifulSoup(driver.page_source, "html.parser")
    #get json for the meta data
    json_string = driver.execute_script(f"return window.localStorage.getItem('__property_details__');")
    driver.close()
    driver.quit()

    return soup, json_string

def get_info(my_tuple : tuple[BeautifulSoup, str]) -> dict:
    soup = my_tuple[0]
    try:
        json_info = json.loads(my_tuple[1])
    except Exception as e:

        print(f"Error : {e} in url {my_tuple[1]}")
        return 
    property_info ={
        "Id" : json_info["reference"] if json_info.get("reference") else None, 
        "Property type" : json_info["propertyType"] if json_info.get("propertyType") else None, 
        "Price" : json_info["price"] if json_info.get("price") else None, 
        "Locality" : json_info["city"] if json_info.get("city") else None,
        "Postcode" : json_info["zipCode"] if json_info.get("zipCode") else None,
        "Subtype" : json_info["propertySubType"] if json_info.get("propertySubType") else None,
        "Sale type" : json_info["transactionType"] if json_info.get("transactionType") else None
        }

    for info_box in soup.find(class_="general-info-wrapper").find_all(class_="data-row-wrapper"):
        for info_name, info in zip(info_box.find_all("h4"), info_box.find_all("p")):
            property_info[re.sub(r"/\n","",info_name.text.strip())] = re.sub(r"/\n","", info.text.strip())#removes \n
    return property_info

def all_properties_info(property_urls: list[str]) -> list[dict]:
    all_properties_info = list[dict]()
    to_csv_titles() # write the titles to the csv file
    for property_url in property_urls:
        print(property_url)
        if re.search(r"project", property_url): 
            pass
        else:
            info = get_info(get_soup(property_url))
            cleaned_info = clean_property_data_output(info)
            if cleaned_info is not None:
                all_properties_info.append(cleaned_info)
                to_csv(cleaned_info)
            else:
                print(f"Error : {cleaned_info} in url {property_url}")
    return all_properties_info

def to_csv_titles():
    titles = [
        "Property ID",
        "Locality name",
        "Postal code",
        "Price", 
        "Type of property", 
        "Subtype of property", 
        "Type of sale", 
        "Number of rooms", 
        "Living area", 
        "Equipped kitchen", 
        "Furnished", 
        "Open fire", 
        "Terrace", 
        "Garden", 
        "Number of facades",
        "Swimming pool", 
        "State of building"
    ]
    with open("data.csv", "a", newline='') as f:
        output = csv.writer(f)
        output.writerow(titles)

def to_csv(to_write: dict):   
    with open("data.csv", "a",encoding='utf-8', newline='') as f:
        output = csv.writer(f)
        output.writerow(to_write.values())


def run_over_all_url_properties_from_csv():
    all_urls = []
   
    with open('url_list.txt', 'r') as file:
        all_urls = [line.strip() for line in file if line.strip()]
    print(len(all_urls))

    properties = all_properties_info(all_urls)
    print(len(properties))

run_over_all_url_properties_from_csv()
