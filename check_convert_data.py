import re
import csv

def property_data_output(property_info: dict) -> dict:
    #output = {"id" : property_info["id"], "locality" : property_info['property type'], "postcode" :  property_info[], "price" :  int(''.join(filter(str.isdigit, property_info['price']))), "type" :  property_info[], "subtype" :  property_info[], "sale_type" :  property_info[], "nb_rooms" :  int(property_info['Number of bedrooms']), "area" :  property_info[], "equipped_kitchen" :  property_info['Kitchen equipment'], "furnished" :  property_info[], "open_fire" :  property_info[], "terrace" :  property_info[], "garden" :  property_info[], "facades":  property_info[], "pool" :  property_info[], "state" : property_info['State of the property']}
    
    def _to_bool(text: str | None):
        if text is None:
            return None
        t = (text or "").strip().lower()
        return True if t == "yes" else False if t == "no" else text

    def _to_int(text: str):
        m = re.search(r"(\d+)", text or "")
        return int(m.group(1)) if m else None

    def _money_to_int(text: str):
        digits = re.sub(r"\D", "", text or "")
        return int(digits) if digits else None
        
    print(property_info.get(_to_bool('Furnished'),None))
    print(property_info.get('Furnished'),None)
    output = {
    "Property ID" : property_info['Id'],
    "Locality name" : property_info['Locality'],
    "Postal code" :  property_info['Postcode'],
    "Price" :  float(property_info['Price']), 
    "Type of property" :  property_info['Property type'], 
    "Subtype of property" :  property_info['Subtype'], 
    "Type of sale" :  property_info['Sale type'], 
    "Number of rooms" :  int(property_info['Number of bedrooms']), 
    "Living area" : re.sub(r"m²" , "",property_info['Livable surface']), #int(''.join(filter(str.isdigit, property_info['Livable surface']))), 
    "Equipped kitchen" : 1 if re.search(r"equipped", property_info['Kitchen equipment']) else 0, 
    "Furnished" :  property_info.get(_to_bool('Furnished'),None),
    "Open fire" :  _to_bool(property_info['Fireplace']), 
    # "Terrace" :  0 if property_info['Terrace'] == "No" else _money_to_int(property_info['Surface terrace']), 
    # "Garden" :  0 if property_info['Garden'] == "No" else _money_to_int(['Surface garden']), 
    "Number of facades":  int(property_info['Number of facades']), 
    "Swimming pool" :  _to_bool(property_info.get('Swimming pool', None)), #Heloise will check if this is correct
    "State of building" : property_info['State of the property']
    }

    return output



# def all_properties_data_output(all_properties_info: dict) -> list[dict]:
#     for property_id in all_properties_info:
#         output.append(property_data_output(all_properties_info[property_id]))
#     return output

# #
#     with open("data.csv", "a") as f:
#         pass

def to_csv(to_write: dict):
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
    with open("data.csv", "a") as f:
        output = csv.writer(f)
        output.writerow(titles)
        #for d in l:
        output.writerow(list(to_write.values()))


test_dict = {'Id': 'VWD15538', 'Property type': 'House', 'Price': '410000.00', 'Locality': 'Seneffe', 'Postcode': '7180', 'Subtype': 'Villa', 'Sale type': 'Sale', 'State of the property': 'Normal', 'Build Year': '1966', 'Availability': 'Negotiable', 'Number of bedrooms': '4', 'Surface bedroom 1': '20 m²', 'Surface bedroom 2': '21 m²', 'Surface bedroom 3': '18 m²', 'Surface bedroom 4': '9 m²', 'Livable surface': '175 m²', 'Total surface': '346 m²', 'Surface of living-room': '47 m²', 'Cellar': 'Yes', 'Surface of the cellar(s)': '62 m²', 'Attic': 'Yes', 'Attic surface': '30 m²', 'Veranda': 'No', 'Wash room': 'Yes', 'Bike storage': 'No', 'Garage': 'Yes', 'Number of parking spaces (indoor)': '2', 'Surface of the garage': '44 m²', 'Motorized garage door': 'No', 'Electric charging station': 'No', 'Kitchen equipment': 'Partially equipped', 'Kitchen type': 'Independent', 'Surface kitchen': '10 m²', 'Water softener': 'No', 'Number of bathrooms': '2', 'Surface of the bathroom(s)': '5 m²', 'Low-energy house': 'No', 'Solar panels': 'No', 'Type of heating': 'Fuel oil', 'Floor heating': 'No', 'Heat pump': 'No', 'Type of glazing': 'Double glass', 'Bi-hourly counter': 'No', 'Air conditioning': 'No', 'Domotica': 'No', 'Entry phone': 'Yes', 'Alarm': 'Yes', 'Security door': 'No', 'Elevator': 'No', 'Hammam/Sauna/Jacuzzi': 'No', 'Fireplace': 'No', 'Orientation of the front facade': 'North-west', 'Number of facades': '4', 'Number of parking places (outdoor)': '4', 'Garden': 'Yes', 'Garden orientation': 'South-east', 'Terrace': 'Yes', 'Total land surface': '2667 m²', 'Sewer Connection': 'Yes', 'Gas': 'No', 'Running water': 'Yes', 'Rain water tank': 'Yes', 'Swimming pool': 'No', 'Specific primary energy consumption': '223 kWh/m²/year', 'Yearly total primary energy consumption': '77067 kWh/year', 'EPC/PEB reference': '20251022003880', 'Validity date EPC/PEB': '22/10/2035', 'Certification - Electrical installation': 'No, certificate does not comply', 'Certification - Electrical installation : validity': '22/12/2036', 'Certification - Gasoil tank': 'Not applicable', 'Building permission granted': 'Yes', 'Planning permission granted': 'Yes', 'Preemption right': 'No', 'Description of urbanism infraction': 'en ordre', 'Certification "As-Build"': 'No', 'Flooding Area type': 'no flooding area', 'Demarcated flooding area': '(information not available)', 'Water sensitive open space areas': 'No', 'The property and/or its surroundings are protected.': 'No'}
#print(property_data_output(test_dict))
to_csv(property_data_output(test_dict))