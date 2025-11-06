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
        "Property ID" : property_info.get('Id', None),
        "Locality name" : property_info.get('Locality', None),
        "Postal code" :  property_info.get('Postcode', None),
        "Price" :  float(property_info.get('Price', 0)) if property_info.get('Price', None) is not None else None,
        "Type of property" :  property_info.get('Property type', None),
        "Subtype of property" :  property_info.get('Subtype', None),
        "Type of sale" :  property_info.get('Sale type', None),
        "Number of rooms" :  int(property_info.get('Number of bedrooms', 0)) if property_info.get('Number of bedrooms', None) is not None else None,
        "Living area" : re.sub(r"m²" , "",property_info.get('Livable surface', None)), 
        "Equipped kitchen" : 1 if property_info.get('Kitchen equipment', "").strip().lower() == "equipped" else 0,
        "Furnished" :  _to_bool(property_info.get('Furnished',None)),
        "Open fire" :  _to_bool(property_info.get('Fireplace', None)), 
        "Terrace" : _to_bool(property_info.get('Terrace', None)),
        "Garden" :  _to_bool(property_info.get('Garden', None)), 
        # "Terrace" :  0 if property_info['Terrace'] == "No" else _money_to_int(property_info['Surface terrace']), 
        # "Garden" :  0 if property_info['Garden'] == "No" else _money_to_int(['Surface garden']), 
        "Number of facades":  _to_int(property_info.get('Number of facades', None)),
        "Swimming pool" :  _to_bool(property_info.get('Swimming pool', None)), #Heloise will check if this is correct
        "State of building" : property_info.get('State of the property', None)
    }

    return output



# def all_properties_data_output(all_properties_info: dict) -> list[dict]:
#     for property_id in all_properties_info:
#         output.append(property_data_output(all_properties_info[property_id]))
#     return output

# #
#     with open("data.csv", "a") as f:
#         pass

