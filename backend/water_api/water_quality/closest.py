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
            if len(data['features']) >= 1:
                for i in range (0, len(data['features'])):
                    location_name = data['features'][i]['properties']['MonitoringLocationName']
                    pattern = r'\b(r\*r|r|lake|LK)\b'
                    if re.search (pattern, location_name,re.IGNORECASE):
                        loc_huc = data['features'][i]['properties']['HUCEightDigitCode']
                        loc_lat = data['features'][i]['geometry']['coordinates'][1]
                        loc_long = data['features'][i]['geometry']['coordinates'][0]
                        loc_name = data['features'][i]['properties']['MonitoringLocationName']
                        loc_found = True
        else:
            print(f"Request failed with status code: {response.status_code}")
            break
        radius *= 2
    return loc_huc,loc_lat,loc_long,loc_name