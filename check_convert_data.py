import re
import csv

def clean_property_data_output(property_info: dict) -> dict:
    #output = {"id" : property_info["id"], "locality" : property_info['property type'], "postcode" :  property_info[], "price" :  int(''.join(filter(str.isdigit, property_info['price']))), "type" :  property_info[], "subtype" :  property_info[], "sale_type" :  property_info[], "nb_rooms" :  int(property_info['Number of bedrooms']), "area" :  property_info[], "equipped_kitchen" :  property_info['Kitchen equipment'], "furnished" :  property_info[], "open_fire" :  property_info[], "terrace" :  property_info[], "garden" :  property_info[], "facades":  property_info[], "pool" :  property_info[], "state" : property_info['State of the property']}
    def _to_bool(text: str | None):
        if text is None:
            return None
        t = (text or "").strip().lower()
        return True if t == "yes" else False if t == "no" else text

    def _to_int(text: str | None):
        if text is None:
            return None
        m = re.search(r"(\d+)", text or "")
        return int(m.group(1)) if m else None

    def _money_to_int(text: str | None):
        if text is None:
            return None
        digits = re.sub(r"\D", "", text or "")
        return int(digits) if digits else None
    
    output = {
        "Property ID" : property_info["Id"] if property_info.get('Id') else None,
        "Locality name" : property_info['Locality'] if property_info.get('Locality') else None,
        "Postal code" :  property_info['Postcode'] if property_info.get('Postcode') else None,
        "Price" :  property_info['Price'] if property_info.get('Price') else None, 
        "Type of property" :  property_info['Property type'] if property_info.get('Property type') else None, 
        "Subtype of property" :  property_info['Subtype'] if property_info.get('Subtype') else None, 
        "Type of sale" :  property_info['Sale type'] if property_info.get('Sale type') else None, 
        "Number of rooms" :  int(property_info['Number of bedrooms']) if property_info.get('Number of bedrooms') else None, 
        "Living area" : re.sub(r"m²" , "",property_info['Livable surface']) if property_info.get('Livable surface') else None,
        "Equipped kitchen" : (1 if re.search(r"equipped", property_info['Kitchen equipment']) else 0) if property_info.get('Kitchen equipment') else None,
        "Furnished" : _to_bool(property_info['Furnished']) if property_info.get('Furnished') else None,
        "Open fire" : _to_bool(property_info['Fireplace']) if property_info.get('Fireplace') else None, 
        "Terrace" : (property_info['Surface terrace'] if property_info.get('Surface terrace') else _to_bool(property_info['Terrace']) if property_info.get('Terrace') else None),
        "Garden" : (property_info['Surface garden'] if property_info.get('Surface garden') else _to_bool(property_info['Garden']) if property_info.get('Garden') else None), 
        "Number of facades": int(property_info['Number of facades']) if property_info.get('Number of facades') else None, 
        "Swimming pool" :  _to_bool(property_info['Swimming pool']) if property_info.get('Swimming pool') else None, 
        "State of building" : property_info['State of the property'] if property_info.get('State of the property') else None
    }
    return output



# def all_properties_data_output(all_properties_info: dict) -> list[dict]:
#     for property_id in all_properties_info:
#         output.append(property_data_output(all_properties_info[property_id]))
#     return output

# #
#     with open("data.csv", "a") as f:
#         pass

