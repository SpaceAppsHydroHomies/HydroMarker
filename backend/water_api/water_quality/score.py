import xml.etree.ElementTree as et
import requests
from typing import Union

from .constants import *


def get_biological_data(huc):
    url = f"https://www.waterqualitydata.us/data/BiologicalMetric/search?huc={huc}&mimeType=xml"
    timeout = 10
    response = requests.get(url, timeout=timeout)

    if response.status_code == 200:
        data = response.text
        
        root = et.fromstring(data)
        ns = {'wqx': 'https://www.waterqualitydata.us/data/schemas/WQX-Outbound/2_0'}  # Define the namespace
        # Search for QHEI linked INDEX Score Number
        qhei_score = None
        for index in root.findall(".//wqx:BiologicalHabitatIndex", namespaces=ns):
            index_type = index.find(".//wqx:IndexTypeIdentifier", namespaces=ns)
            index_score = index.find(".//wqx:IndexScoreNumeric", namespaces=ns)
            
            if index_type is not None and index_type.text == "QHEI":
                qhei_score = index_score.text
                break  # Stop searching once QHEI is found
        if qhei_score is None:
            for index in root.findall(".//wqx:BiologicalHabitatIndex", namespaces=ns):
                index_type = index.find(".//wqx:IndexTypeIdentifier", namespaces=ns)
                index_score = index.find(".//wqx:IndexScoreNumeric", namespaces=ns)
                
                if index_type is not None and index_score is not None:
                    qhei_score = index_score.text
                    break  # Stop searching once QHEI is found
        if qhei_score is not None:
            qhei_score = round(float(qhei_score))
        
        # Return None if the data does not contain QHEI or if there was an issue with the request
        return qhei_score
    return None


def get_rating(attainment_code_name) -> int:
    match attainment_code_name:
        case 'Fully Supporting':
            return 2
        case 'Not Supporting':
            return 1
        case _:
            return 0


def get_activity(name):
    match name:
        case 'Domestic Water Supply':
            return 'drinking'
        case 'AQUATIC LIFE USE':
            return 'organisms'
        case _:
            return 'recreation'


def get_biological_data_refactor(huc, state, water_code) -> Union[int, dict]:
    """If a QHEI score is found, return that score, otherwise use a formula to develop our own score

    :param huc: huc of the body of water
    :param state: state
    :param water_code:
    :return: score
    """
    state_code = STATE_CODES.get(state) if state in STATE_CODES else state
    assessment_units_url = f'{ATTAINS_API}/assessmentUnits?HUC={huc}&stateCode={state_code}&statusIndicator=A'
    timeout = 10
    response = requests.get(assessment_units_url, timeout=timeout)
    response_json = response.json()
    if response.status_code != 200 or not response_json['items']:
        return -1
    assessment_unit_id = ''
    organization_id = ''
    found_auid = False
    for item in response_json['items']:
        for assessment_unit in item['assessmentUnits']:
            if huc in assessment_unit['locationDescriptionText'] and water_code in assessment_unit['waterTypes'][0]['waterTypeCode']:
                assessment_unit_id = assessment_unit['assessmentUnitIdentifier']
                organization_id = item['organizationIdentifier']
                found_auid = True
                break
        if found_auid:
            break

    if not found_auid:
        return -2

    assessments_url = f'{ATTAINS_API}/assessments?assessmentUnitIdentifier={assessment_unit_id}&state={state_code}&organizationIdentifier={organization_id}'
    response = requests.get(assessments_url, timeout=timeout)
    if response.status_code != 200:
        return -3

    item = response.json()['items'][0]
    attainments = item['assessments'][0]['useAttainments']
    result = [{get_activity(a['useName']): get_rating(a['useAttainmentCodeName'])} for a in attainments]
    result_dict = {}
    for it in result:
        result_dict.update(it)
    return result_dict
