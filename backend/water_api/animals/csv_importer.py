"""
File to parse the ecosystem data into the SQLite Database.
Note: append the absolute path to the water_api directory if you wish to use this script.
"""

import os, sys, csv, django

sys.path.append(
    "/mnt/c/Users/nicho/OneDrive/Desktop/github/changethislater/backend/water_api"
)
os.environ["DJANGO_SETTINGS_MODULE"] = "water_api.settings"

django.setup()

# WARNING: Order is important. Do not import any Django models before calling django.setup()
from animals.models import Ecosystem


def import_data_from_csv(csv_file_path):
    with open(csv_file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Create an instance of the Ecosystem model and populate it with data from the CSV
            ecosystem = Ecosystem.objects.create(
                E_CODE=row["E_CODE"],
                EcosystemName=row["EcosystemName"],
                EcosystemType=row["EcosystemType"],
                Location=row["Location"],
                Salinity=row["Salinity"],
                NorthernLat=row["NorthernLat"] if row["NorthernLat"] != "nan" else None,
                NrangeNS=row["NrangeNS"],
                SouthernLat=row["SouthernLat"] if row["SouthernLat"] != "nan" else None,
                SrangeNS=row["SrangeNS"],
                WesternLat=row["WesternLat"] if row["WesternLat"] != "nan" else None,
                WrangeEW=row["WrangeEW"],
                EasternLat=row["EasternLat"] if row["EasternLat"] != "nan" else None,
                ErangeEW=row["ErangeEW"],
                Climate=row["Climate"] if row["Climate"] != "nan" else None,
                TotalCount=int(row["TotalCount"])
                if row["TotalCount"] != "nan"
                else None,
                TotalFamCount=int(row["TotalFamCount"])
                if row["TotalFamCount"] != "nan"
                else None,
                TotalComplete=int(row["TotalComplete"])
                if row["TotalComplete"] != "nan"
                else None,
                LatDegFill=int(row["LatDegFill"])
                if row["LatDegFill"] != "nan"
                else None,
                LatMinFill=int(row["LatMinFill"])
                if row["LatMinFill"] != "nan"
                else None,
                NorthSouthFill=row["NorthSouthFill"],
                LongDegFill=int(row["LongDegFill"])
                if row["LongDegFill"] != "nan"
                else None,
                LongMinFill=int(row["LongMinFill"])
                if row["LongMinFill"] != "nan"
                else None,
                EastWestFill=row["EastWestFill"],
            )


if __name__ == "__main__":
    csv_file_path = (
        "extracted_ecosystems.csv"  # Replace with the actual path to your CSV file
    )
    import_data_from_csv(csv_file_path)
