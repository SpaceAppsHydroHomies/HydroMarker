from django.http import JsonResponse
from water_quality.closest import closest_location


def index(response):
    return JsonResponse({"test": "data"})


def get_data(request):
    if request.method == "GET":
        lat, long = request.GET.get("lat"), request.GET.get("long")
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
        HUC, revised_lat, revised_long = closest_location(lat, long)
        # TODO: Return the data for that HUC
        # TODO: Get the colloquial name of the body of water we're in
        return JsonResponse({"lat": lat, "long": long})
