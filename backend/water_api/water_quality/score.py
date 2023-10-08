import xml.etree.ElementTree as ET
import requests


def get_biological_data(HUC):
    url = f"https://www.waterqualitydata.us/data/BiologicalMetric/search?huc={HUC}&mimeType=xml"
    timeout = 10
    response = requests.get(url, timeout=timeout)

    if response.status_code == 200:
        data = response.text
        
        root = ET.fromstring(data)
        ns = {'wqx': 'https://www.waterqualitydata.us/data/schemas/WQX-Outbound/2_0'}  # Define the namespace
        # Search for QHEI linked INDEX Score Number
        qhei_score = None
        for index in root.findall(".//wqx:BiologicalHabitatIndex", namespaces=ns):
            index_type = index.find(".//wqx:IndexTypeIdentifier", namespaces=ns)
            index_score = index.find(".//wqx:IndexScoreNumeric", namespaces=ns)
            
            if index_type is not None and index_type.text == "QHEI":
                qhei_score = index_score.text
                break  # Stop searching once QHEI is found
                
        return round(float(qhei_score))
    # Return None if the data does not contain QHEI or if there was an issue with the request
    return None
