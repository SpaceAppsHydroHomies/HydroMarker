from django.http import JsonResponse
from water_quality.closest import closest_location, fuzzy_search
from water_quality.score import get_biological_data


def index(response):
    return JsonResponse({"test": "data"})


def get_data(request,lat,long):
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
                }
            )
        # TODO: Get the HUC of the closest body of water
        huc, huc_lat, huc_long, huc_name = closest_location(lat, long)
        # TODO: Return the data for that HUC
        water_score = get_biological_data(huc)
        # TODO: Get the colloquial name of the body of water we're in
        return JsonResponse({'lat': huc_lat, 'long': huc_long, 'score' : water_score, 'displayName' : huc_name, 'name' : fuzzy_search(huc_name)})
