import requests
import re
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

regex_remove_parenthesis = r"\([^)]*\)"


def scrape_fishbase_ecosystem(e_code: int) -> dict:
    """
    Scrape for endangered fish species from an ecosystem code.
    Returns a dictionary of species id and species name
    """
    url = f"https://www.fishbase.org.au/TrophicEco/FishEcoList.php?ve_code={e_code}"
    species_data = {}

    try:
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")

            # Find all <a> elements in the HTML
            html_links = soup.find_all("a")

            for html in html_links:
                href = html.get("href")
                if href and "SpeciesSummary" in href:
                    # Extract species ID from the href
                    species_id = int(href.split("=")[1])

                    # Extract species name from the text of the link
                    species_name = html.get_text()

                    species_data[species_id] = species_name

            # Return the dictionary of species IDs and names
            print(species_data)
            return species_data

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def scrape_fishbase_fish(id: int) -> dict:
    """Scrape for a fish's info based on their ID."""
    url = f"https://www.fishbase.org.au/summary/SpeciesSummary.php?id={id}"
    fish_details = {}
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            small_space_div = soup.find_all("div", {"class": "smallSpace"})
            for env in small_space_div:
                if (
                    "Marine;" in env.get_text()
                    or "Freshwater;" in env.get_text()
                    or "Saltwater;" in env.get_text()
                    or "Brackish;" in env.get_text()
                ):
                    fish_details["Salinity"] = env.get_text().split(";")[0].strip()
                if "Resilience" in env.get_text():
                    resilience = env.get_text().split(":")[1].strip()
                    cleaned_text = re.sub(regex_remove_parenthesis, "", resilience)
                    fish_details["Resilience"] = cleaned_text
                if "Fishing Vulnerability" in env.get_text():
                    fish_details["Fishing Vulnerability"] = (
                        env.get_text().split(":")[1].strip()
                    )
                if "Date assessed" in env.get_text():
                    fish_details["IUCN Red List Status"] = (
                        env.get_text().split(";")[0].strip().replace("\xa0", " ")
                    )
                else:
                    fish_details["IUCN Red List Status"] = "Not Evaluated"
                if (
                    "Traumatogenic" in env.get_text()
                    or "Potential" in env.get_text()
                    or "Harmless" in env.get_text()
                    or "Reports" in env.get_text()
                    or "Other" in env.get_text()
                    or "Venom" in env.get_text()
                    or "Poison" in env.get_text()
                ):
                    fish_details["Threats To Humans"] = (
                        env.get_text().strip().replace("\xa0", " ")
                    )
            common_name = soup.find_all("title")
            for name in common_name:
                fish_details["Common Name"] = name.get_text().split(",")[1].strip()
            print(fish_details)
        return fish_details

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {}


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
