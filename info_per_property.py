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
    """
    property_info ={
        "Id" : json_info["reference"], 
        "Property type" : json_info["propertyType"], 
        "Price" : json_info["price"], 
        "Locality" : json_info["city"],
        "Postcode" : json_info["zipCode"],
        "Subtype" : json_info["propertySubType"],
        "Sale type" : json_info["transactionType"]
        }
        """
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

def get_info_project(soup: BeautifulSoup) -> dict:
    pass
"""
def get_info_project(my_tuple : tuple[BeautifulSoup, str]) -> dict:

    json_info = json.loads(my_tuple[1])
    print(json_info)

    soup = my_tuple[0]
    

    info_project = {}

    # TYPE OF PROPERTY
    title = soup.find("h1").contents[0]
    property_type = title.text.strip() if title else None
    #print(property_type)

    # ADDRESS

    title_section = driver.find_element(By.CLASS_NAME, "detail__header_address")
    address_section = title_section.find_element(By.CLASS_NAME, "d-none.d-md-block")

    spans = address_section.find_elements(By.TAG_NAME, "span")
    address = " ".join([span.text for span in spans])



    
    section = soup.find("div", class_="section-container py-2 mt-lg-2")
    highlights = section.find_all("div", class_="property-highlight")

    
    # Amount of the rooms
    for room in highlights:
        if "Bedroom" in room.text:   
            strong_tag = room.find("strong")
            if strong_tag:
                num_room = strong_tag.text  

    
    # The prize of the project
    for amount in highlights:
        if "€" in amount.text:
            strong_tag = amount.find("strong")
            price = strong_tag.text


    # The space of the project in m²

    for area in highlights:
        if "m²" in area.text:   
            strong_tag = area.find("strong")
            if strong_tag:
                area_m = strong_tag.text  


    #info_project["Property type"] = property_type
    #info_project["Address"] = address
    info_project["Number of bedrooms"] = num_room
    info_project["Livable surface"] = area_m
    info_project["Price"] = price.replace('\u202f', ' ').strip()


    return info_project
"""

def all_properties_info(properties: list[str]) -> list[dict]:
    all_properties_info = list[dict]()
    to_csv_titles() # write the titles to the csv file
    for property_url in properties:
        print(property_url)
        if re.search(r"project", property_url): 
            #info = get_info_project(get_soup(property_url))
            pass
        else:
            info = get_info(get_soup(property_url))
            print("error with info", property_url)
                
            cleaned_info = clean_property_data_output()))
            if cleaned_info is not None:
                all_properties_info.append(cleaned_info)
                print(cleaned_info.values())
                to_csv(cleaned_info)
            else:
                print(f"Error : {cleaned_info} in url {property_url}")
        #properties_info[info["Id"]] = info

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
    with open("data.csv", "w", newline='') as f:
        output = csv.writer(f)
        output.writerow(titles)

def to_csv(to_write: dict):   
    with open("data.csv", "a") as f:
        output = csv.writer(f)
        output.writerow(to_write.values())
        #for d in l:
        # output.writerow(list(to_write.values()))


def run_over_all_url_properties_from_csv():
    all_urls = []
   
    with open('url_list.txt', 'r') as file:
        all_urls = [line.strip() for line in file if line.strip()]
    print(len(all_urls))

    properties = all_properties_info(all_urls)
    print(len(properties))



run_over_all_url_properties_from_csv()
