from fuzzywuzzy import fuzz
import re
import requests


def closest_location(latitude, longitude):
    """
    Params : latitude (float), longitude(float)
    Take a request to find all bodies within x miles (radius)
    Limit at 65 miles, double each iteration
    Returns location HUC, latitude and longitude
    """

    radius = 0.25
    timeout = 10
    loc_huc = ""
    loc_lat = 0
    loc_long = 0
    loc_name = ""
    loc_found = False

    while radius < 65 and loc_found is False:
        url = f"https://www.waterqualitydata.us/data/Station/search?lat={latitude}&long={longitude}&within={radius}&siteType=Lake, Reservoir, Impoundment&siteType=Stream&mimeType=geojson"
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            data = response.json()
            if len(data["features"]) >= 1:
                for i in range(0, len(data["features"])):
                    location_name = data["features"][i]["properties"][
                        "MonitoringLocationName"
                    ]
                    pattern = r"\b(r\*r|r|lake|LK)\b"
                    if re.search(pattern, location_name, re.IGNORECASE):
                        loc_huc = data["features"][i]["properties"]["HUCEightDigitCode"]
                        loc_lat = data["features"][i]["geometry"]["coordinates"][1]
                        loc_long = data["features"][i]["geometry"]["coordinates"][0]
                        loc_name = data["features"][i]["properties"][
                            "MonitoringLocationName"
                        ]
                        loc_found = True
        else:
            print(f"Request failed with status code: {response.status_code}")
            break
        radius *= 2
    return loc_huc,loc_lat,loc_long,loc_name

def fuzzy_search(search: str):
    """Does a fuzzy search on the waterbodies dictionary and returns the closest match."""
    waterbodies = {
        'Atlantic': 'Atlantic Ocean',
        'Pacific': 'Pacific Ocean',
        'Mississippi-Missouri': 'Mississippi-Missouri River',
        'Missouri': 'Missouri River',
        'Mississippi': 'Mississippi River',
        'Arkansas': 'Arkansas River',
        'Colorado': 'Colorado River',
        'Columbia': 'Columbia River',
        'California Current': 'California Current',
        'Gulf of Mexico': 'Gulf of Mexico',
        'Great Lakes': 'Great Lakes',
        'Northeast U.S. Continental Shelf': 'Northeast U.S. Continental Shelf',
        'Gulf of Maine': 'Gulf of Maine',
        'Nearctic': 'Nearctic',
        'Penobscot Bay': 'Penobscot Bay',
        'Pacific Coastal Complex': 'Pacific Coastal Complex',
        'Great Basin': 'Great Basin',
        'Colorado Complex': 'Colorado Complex',
        'Puget Sound': 'Puget Sound',
        'Chesapeake Bay': 'Chesapeake Bay',
        'Strait of Juan de Fuca': 'Strait of Juan de Fuca',
        'Klamath': 'Klamath River',
        'Gila': 'Gila River',
        'Green': 'Green River',
        'Platte': 'Platte River',
        'Pecos': 'Pecos River',
        'Brazos': 'Brazos River',
        'Cumberland': 'Cumberland River',
        'Alabama': 'Alabama River',
        'Ohio': 'Ohio River',
        'Apalachicola': 'Apalachicola River',
        'Potomac': 'Potomac River',
        'Pee Dee': 'Pee Dee River',
        'Connecticut': 'Connecticut River',
        'Hudson': 'Hudson River',
        'Superior': 'Lake Superior',
        'Michigan': 'Lake Michigan',
        'Huron': 'Lake Huron',
        'Erie': 'Lake Erie',
        'Ontario': 'Lake Ontario',
        'Bear': 'Bear River',
        'Kansas': 'Kansas River',
        'Neuse': 'Neuse River',
        'New': 'New River',
        'Holston': 'Holston River',
        'Coosa': 'Coosa River',
        'Carolinian': 'Carolinian',
        'Floridian': 'Floridian',
        'Mohawk': 'Mohawk River',
        'Kentucky': 'Kentucky River',
        'Cheyenne': 'Cheyenne River',
        'Allegheny': 'Allegheny River',
        'Genesee': 'Genesee River',
        'Great Miami': 'Great Miami River',
        'Little Miami': 'Little Miami River',
        'Pontchartrain': 'Lake Pontchartrain',
        'Guadalupe': 'Guadalupe River',
        'Altamaha': 'Altamaha River',
        'Champlain': 'Lake Champlain',
        'Escambia': 'Escambia River',
        'James': 'James River',
        'Chowan': 'Chowan River',
        'Cape Fear': 'Cape Fear River',
        'Edisto': 'Edisto River',
        'Nueces': 'Nueces River',
        'Clear': 'Clear Lake',
        'Pajaro': 'Pajaro River',
        'Little Red': 'Little Red River',
        'Hiwassee': 'Hiwassee River',
        'Black Warrior': 'Black Warrior River',
        'Muskingum': 'Muskingum River',
        'Navidad': 'Navidad River',
        'Little': 'Little River',
        'Big Black': 'Big Black River',
        'Bayou Pierre': 'Bayou Pierre River',
        'Chattahoochee': 'Chattahoochee River',
        'Choctawhatchee': 'Choctawhatchee River',
        'Ouachita': 'Ouachita River',
        'Devils': 'Devils River',
        'Pearl': 'Pearl River',
        'Cahaba': 'Cahaba River'
    }

    high_score = ("", 0)
    for waterbody in waterbodies:
        score = fuzz.ratio(search.lower(), waterbody.lower())
        if score > high_score[1]:
            high_score = (waterbody, score)

    return waterbodies[high_score[0]]
