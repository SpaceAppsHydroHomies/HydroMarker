from django.shortcuts import render
from django.http import JsonResponse
from animals.models import Ecosystem
from animals.helper_functions import scrape_fishbase_ecosystem, scrape_fishbase_fish


def get_endangered_species_data(response, ecosystem_name: str) -> JsonResponse:
    response = {}
    endangered_species_list = []
    try:
        ecosystem = Ecosystem.objects.get(EcosystemName=ecosystem_name)
        scrape_ecosystem = scrape_fishbase_ecosystem(ecosystem.E_CODE)
        for key, value in scrape_ecosystem.items():
            scrape_fish = scrape_fishbase_fish(key)
            fish_data = {}
            fish_data["Id"] = key
            fish_data["Scientific Name"] = value
            fish_data["Common Name"] = scrape_fish.get("Common Name")
            fish_data["Salinity"] = scrape_fish.get("Salinity")
            fish_data["Resilience"] = scrape_fish.get("Resilience")
            fish_data["Fishing Vulnerability"] = scrape_fish.get(
                "Fishing Vulnerability"
            )
            fish_data["IUCN Red List Status"] = scrape_fish.get("IUCN Red List Status")
            fish_data["Threats To Humans"] = scrape_fish.get("Threats To Humans")
            endangered_species_list.append(fish_data)
        response["Endangered Species"] = endangered_species_list
    except Ecosystem.DoesNotExist:
        return JsonResponse({})

    return JsonResponse(response)
