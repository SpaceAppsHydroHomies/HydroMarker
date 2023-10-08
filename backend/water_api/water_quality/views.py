from django.http import JsonResponse
from .closest import closest_location, fuzzy_search
from .score import get_biological_data_refactor


def index(response):
    return JsonResponse({"test": "data"})


def get_data(request, lat, long):
    if request.method == "GET":
        lat = float(lat)
        long = float(long)

        if not isinstance(lat, (float, int)) or not isinstance(long, (float, int)):
            return JsonResponse(
                {"status": 400, "reason": "lat or long was not an int or float"},
                status=400,
            )
        if lat > 180 or lat < -180 or long < -180 or long > 180:
            return JsonResponse(
                {
                    "status": 400,
                    "reason": "latitude and longitude should be between -180 and 180",
                },
                status=400
            )
        location = closest_location(lat, long)
        if not location or isinstance(location, int):
            return JsonResponse(
                {
                    "status": 400,
                    "reason": "No bodies of water found near the latitude and longitude"
                }
            )
        # TODO: Return the data for that HUC
        water_score = get_biological_data_refactor(location['huc'], location['state'], location["water_code"].upper())
        return JsonResponse({'lat': location['lat'], 'long': location['long'],
                             'score': water_score,
                             'displayName': location['name'],
                             'name': fuzzy_search(location['name']),
                             'huc': location['huc'],
                             'water_code': location['water_code']})
