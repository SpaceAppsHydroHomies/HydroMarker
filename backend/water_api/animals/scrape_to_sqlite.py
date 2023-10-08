"""
File to iterate through the SQLite database, fetch all fish data from fishbase, and store in to SQLite.
Note: append the absolute path to the water_api directory if you wish to use this script.
"""

import os, sys, csv, django

sys.path.append(
    "/mnt/c/Users/nicho/OneDrive/Desktop/github/changethislater/backend/water_api"
)
os.environ["DJANGO_SETTINGS_MODULE"] = "water_api.settings"

django.setup()

# WARNING: Order is important. Do not import any Django models before calling django.setup()
from animals.models import Ecosystem, EndangeredAnimal
from animals.helper_functions import scrape_fishbase_ecosystem, scrape_fishbase_fish

ecosystems = Ecosystem.objects.all()
for ecosystem in ecosystems:
    animals = scrape_fishbase_ecosystem(e_code=ecosystem.E_CODE)
    for id, name in animals.items():
        if (
            not EndangeredAnimal.objects.filter(FishBaseId=id).exists()
            and ecosystem.E_CODE != 8
            and ecosystem.E_CODE != 9
            and ecosystem.Salinity != "Saltwater"
            and ecosystem.Salinity != "Marine"
        ):
            data = scrape_fishbase_fish(id=id)
            print(f"Currently Storing {data}")
            if data:
                new_instance = EndangeredAnimal.objects.create(
                    FishBaseId=id,
                    ScientificName=name,
                    CommonName=data.get("Common Name"),
                    Salinity=data.get("Salinity"),
                    Resilience=data.get("Resilience"),
                    FishingVulnerability=data.get("Fishing Vulnerability"),
                    IUCNRedListStatus=data.get("IUCN Red List Status"),
                    ThreatsToHumans=data.get("Threats To Humans"),
                )
