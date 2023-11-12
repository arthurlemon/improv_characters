import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> BeautifulSoup:
    # Send a GET request to the webpage
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f'Failed to retrieve the webpage. Status Code: {response.status_code}')

def extract_elements(soup:BeautifulSoup) -> list[dict[str, str]]:
    extracted_info = []
    select_elements = soup.find_all('select', class_='selecta')
    for element in select_elements:
        select_name = element.get('name')
        
        for option in element.find_all('option'):
            option_value = option.get('value', '').strip()
            
            if option_value:
                    extracted_info.append({"type": select_name, "value": option_value})

    return extracted_info

def format_raw_elements(raw_elements):
    formatted_elements = {
        "male_character": [],
        "male_adjective": [],
        "male_action": [],
        "female_character": [],
        "female_adjective": [],
        "female_action": []
    }
    
    mapping_type = {
        "protagotronH1": "male_character",
        "protagotronH2": "male_adjective",
        "protagotronM1": "male_action",
        "protagotronF1": "female_character",
        "protagotronF2": "female_adjective",
        "protagotronM2": "female_action"
    }
    # Iterate over the original data and populate the refactored_info
    for item in raw_elements:
        # Map the 'type' to the new structure
        if item['type'] in mapping_type:
            new_type = mapping_type[item['type']]
            formatted_elements[new_type].append(item['value'])
    return formatted_elements


