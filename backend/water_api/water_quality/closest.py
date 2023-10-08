import requests

def closest_location(latitude, longitude):
    """
    Params : latitude (float), longitude(float)
    Take a request to find all bodies within x miles (radius)
    Limit at 10 miles, double each iteration
    Returns location HUC, latitude and longitude
    """

    radius = 0.25
    timeout = 10
    loc_huc = ""
    loc_lat = 0
    loc_long = 0
    loc_found = False

    while radius < 10 and loc_found is False:
        url = f"https://www.waterqualitydata.us/data/Station/search?lat={latitude}&long={longitude}&within={radius}&siteType=Lake, Reservoir, Impoundment&siteType=Estuary&siteType=Ocean&siteType=Spring&siteType=Stream&mimeType=geojson"
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            data = response.json()
            print(len(data['features']))
            if len(data['features']) >= 1:
                loc_huc = data['features'][0]['properties']['HUCEightDigitCode']
                loc_lat = data['features'][0]['geometry']['coordinates'][1]
                loc_long = data['features'][0]['geometry']['coordinates'][0]
                loc_found = True
        else:
            print(f"Request failed with status code: {response.status_code}")
            break
        radius *= 2
    return loc_huc,loc_lat,loc_long
