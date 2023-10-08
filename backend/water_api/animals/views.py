import re
from django.shortcuts import render
from django.http import JsonResponse
from animals.models import Ecosystem, EndangeredAnimal
from animals.helper_functions import scrape_fishbase_ecosystem, scrape_fishbase_fish

regex_remove_parenthesis = r"\([^)]*\)"


def get_endangered_species_data(response, ecosystem_name: str) -> JsonResponse:
    num_data_to_collect = 5
    num_data_collected = 0
    response = {}
    endangered_species_list = []

    try:
        ecosystem = Ecosystem.objects.get(EcosystemName=ecosystem_name)
        scrape_ecosystem = scrape_fishbase_ecosystem(ecosystem.E_CODE)

        queryset = EndangeredAnimal.objects.filter(
            FishBaseId__in=list(scrape_ecosystem.keys())
        )
        for item in queryset:
            fish_data = {}
            fish_data["Id"] = item.FishBaseId
            fish_data["Scientific Name"] = item.ScientificName
            fish_data["Common Name"] = str(item.CommonName).split(":")[0]
            fish_data["Salinity"] = item.Salinity
            fish_data["Resilience"] = item.Resilience
            fish_data["Fishing Vulnerability"] = item.FishingVulnerability
            fish_data["IUCN Red List Status"] = item.IUCNRedListStatus
            fish_data["Threats To Humans"] = re.sub(
                regex_remove_parenthesis, "", str(item.ThreatsToHumans).strip()
            )

            endangered_species_list.append(fish_data)
            num_data_collected += 1

            if num_data_collected >= num_data_to_collect:
                break
        if num_data_collected < num_data_to_collect:
            for key, value in scrape_ecosystem.items():
                if any(key in d for d in endangered_species_list):
                    continue

                fish_data = {}
                fish_data["Id"] = key
                fish_data["Scientific Name"] = value

                scrape_fish = scrape_fishbase_fish(key)

                fish_data["Common Name"] = scrape_fish.get("Common Name")
                fish_data["Salinity"] = scrape_fish.get("Salinity")
                fish_data["Resilience"] = scrape_fish.get("Resilience")
                fish_data["Fishing Vulnerability"] = scrape_fish.get(
                    "Fishing Vulnerability"
                )
                fish_data["IUCN Red List Status"] = scrape_fish.get(
                    "IUCN Red List Status"
                )
                fish_data["Threats To Humans"] = re.sub(
                    regex_remove_parenthesis,
                    "",
                    str(scrape_fish.get("Threats To Humans")).strip(),
                )

                endangered_species_list.append(fish_data)
                num_data_collected += 1

                if num_data_collected >= num_data_to_collect:
                    break
        response["Endangered Species"] = endangered_species_list

    except Ecosystem.DoesNotExist:
        return JsonResponse({})

    return JsonResponse(response)


def get_ecosystems(request):
    ecosystems = Ecosystem.objects.all()
    response = {}
    list_of_ecosystems = []
    for ecosystem in ecosystems:
        list_of_ecosystems.append(ecosystem.EcosystemName)
    response["Ecosystems"] = list_of_ecosystems
    return JsonResponse(response)
