import re

def property_data_output(property_info: dict) -> dict:
    #output = {"id" : property_info["id"], "locality" : property_info['property type'], "postcode" :  property_info[], "price" :  int(''.join(filter(str.isdigit, property_info['price']))), "type" :  property_info[], "subtype" :  property_info[], "sale_type" :  property_info[], "nb_rooms" :  int(property_info['Number of bedrooms']), "area" :  property_info[], "equipped_kitchen" :  property_info['Kitchen equipment'], "furnished" :  property_info[], "open_fire" :  property_info[], "terrace" :  property_info[], "garden" :  property_info[], "facades":  property_info[], "pool" :  property_info[], "state" : property_info['State of the property']}
    output = {
    "Property ID" : property_info["id"],
    "Locality name" : re.sub(r"\d+","",property_info['locality']),
    "Postal code" :  re.sub(r"\D+","",property_info['locality']),
    "Price" :  int(''.join(filter(str.isdigit, property_info['price']))), 
    "Type of property" :  property_info['property type'], 
    "Subtype of property" :  property_info[], 
    "Type of sale" :  property_info[], 
    "Number of rooms" :  int(property_info['Number of bedrooms']), 
    "Living area" :  int(''.join(filter(str.isdigit, property_info['Livable surface']))), 
    "Equipped kitchen" :  property_info['Kitchen equipment'], 
    "Furnished" :  property_info['Furnished'], 
    "Open fire" :  property_info['Fireplace'], 
    "Terrace" :  property_info['Terrace'] + property_info['Surface terrace'], 
    "Garden" :  property_info['Garden'] + property_info['Surface garden'], 
    "Number of facades":  int(property_info['Number of facades']), 
    "Swimming pool" :  property_info['Swimming pool'], 
    "State of building" : property_info['State of the property']
    }

def all_properties_data_output(all_properties_info: dict) -> list[dict]:
    output = []
    for property_id in all_properties_info:
        output.append(property_data_output(all_properties_info[property_id]))
    return output

def to_csv(output: list[dict]):
    with open("data.csv", "a") as f:
        pass




test_dict = {'id': 'VWD15538', 'property type': 'Villa for sale - Seneffe VWD15538', 'price': 'Make offer from 410\u202f000 €', 'State of the property': 'Normal', 'Build Year': '1966', 'Availability': 'Negotiable', 'Number of bedrooms': '4', 'Surface bedroom 1': '20 m²', 'Surface bedroom 2': '21 m²', 'Surface bedroom 3': '18 m²', 'Surface bedroom 4': '9 m²', 'Livable surface': '175 m²', 'Total surface': '346 m²', 'Surface of living-room': '47 m²', 'Cellar': 'Yes', 'Surface of the cellar(s)': '62 m²', 'Attic': 'Yes', 'Attic surface': '30 m²', 'Veranda': 'No', 'Wash room': 'Yes', 'Bike storage': 'No', 'Garage': 'Yes', 'Number of parking spaces (indoor)': '2', 'Surface of the garage': '44 m²', 'Motorized garage door': 'No', 'Electric charging station': 'No', 'Kitchen equipment': 'Partially equipped', 'Kitchen type': 'Independent', 'Surface kitchen': '10 m²', 'Water softener': 'No', 'Number of bathrooms': '2', 'Surface of the bathroom(s)': '5 m²', 'Low-energy house': 'No', 'Solar panels': 'No', 'Type of heating': 'Fuel oil', 'Floor heating': 'No', 'Heat pump': 'No', 'Type of glazing': 'Double glass', 'Bi-hourly counter': 'No', 'Air conditioning': 'No', 'Domotica': 'No', 'Entry phone': 'Yes', 'Alarm': 'Yes', 'Security door': 'No', 'Elevator': 'No', 'Hammam/Sauna/Jacuzzi': 'No', 'Fireplace': 'No', 'Orientation of the front facade': 'North-west', 'Number of facades': '4', 'Number of parking places (outdoor)': '4', 'Garden': 'Yes', 'Garden orientation': 'South-east', 'Terrace': 'Yes', 'Total land surface': '2667 m²', 'Sewer Connection': 'Yes', 'Gas': 'No', 'Running water': 'Yes', 'Rain water tank': 'Yes', 'Swimming pool': 'No', 'Specific primary energy consumption': '223 kWh/m²/year', 'Yearly total primary energy consumption': '77067 kWh/year', 'EPC/PEB reference': '20251022003880', 'Validity date EPC/PEB': '22/10/2035', 'Certification - Electrical installation': 'No, certificate does not comply', 'Certification - Electrical installation : validity': '22/12/2036', 'Certification - Gasoil tank': 'Not applicable', 'Building permission granted': 'Yes', 'Planning permission granted': 'Yes', 'Preemption right': 'No', 'Description of urbanism infraction': 'en ordre', 'Certification "As-Build"': 'No', 'Flooding Area type': 'no flooding area', 'Demarcated flooding area': '(information not available)', 'Water sensitive open space areas': 'No', 'The property and/or its surroundings are protected.': 'No'}
#test_dict = {'id': 'VWD15538', 'property type': 'Villa for sale - Seneffe VWD15538', 'price': 'Make offer from 410\u202f000 €', 'State of the property': 'Normal', 'Build Year': '1966', 'Availability': 'Negotiable', 'Number of bedrooms': '4', 'Surface bedroom 1': '20 m²', 'Surface bedroom 2': '21 m²', 'Surface bedroom 3': '18 m²', 'Surface bedroom 4': '9 m²', 'Livable surface': '175 m²', 'Total surface': '346 m²', 'Surface of living-room': '47 m²', 'Cellar': 'Yes', 'Surface of the cellar(s)': '62 m²', 'Attic': 'Yes', 'Attic surface': '30 m²', 'Veranda': 'No', 'Wash room': 'Yes', 'Bike storage': 'No', 'Garage': 'Yes', 'Number of parking spaces (indoor)': '2', 'Surface of the garage': '44 m²', 'Motorized garage door': 'No', 'Electric charging station': 'No', 'Kitchen equipment': 'Partially equipped', 'Kitchen type': 'Independent', 'Surface kitchen': '10 m²', 'Water softener': 'No', 'Number of bathrooms': '2', 'Surface of the bathroom(s)': '5 m²', 'Low-energy house': 'No', 'Solar panels': 'No', 'Type of heating': 'Fuel oil', 'Floor heating': 'No', 'Heat pump': 'No', 'Type of glazing': 'Double glass', 'Bi-hourly counter': 'No', 'Air conditioning': 'No', 'Domotica': 'No', 'Entry phone': 'Yes', 'Alarm': 'Yes', 'Security door': 'No', 'Elevator': 'No', 'Hammam/Sauna/Jacuzzi': 'No', 'Fireplace': 'No', 'Orientation of the front facade': 'North-west', 'Number of facades': '4', 'Number of parking places (outdoor)': '4', 'Garden': 'Yes', 'Garden orientation': 'South-east', 'Terrace': 'Yes', 'Total land surface': '2667 m²', 'Sewer Connection': 'Yes', 'Gas': 'No', 'Running water': 'Yes', 'Rain water tank': 'Yes', 'Swimming pool': 'No', 'Specific primary energy consumption': '223 kWh/m²/year', 'Yearly total primary energy consumption': '77067 kWh/year', 'EPC/PEB reference': '20251022003880', 'Validity date EPC/PEB': '22/10/2035', 'Certification - Electrical installation': 'No, certificate does not comply', 'Certification - Electrical installation : validity': '22/12/2036', 'Certification - Gasoil tank': 'Not applicable', 'Building permission granted': 'Yes', 'Planning permission granted': 'Yes', 'Preemption right': 'No', 'Description of urbanism infraction': 'en ordre', 'Certification "As-Build"': 'No', 'Flooding Area type': 'no flooding area', 'Demarcated flooding area': '(information not available)', 'Water sensitive open space areas': 'No', 'The property and/or its surroundings are protected.': 'No'}
print(property_data_output(test_dict))