import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> BeautifulSoup | None:
    """
    Fetches the content of a website and returns a BeautifulSoup object for parsing.
    
    Args:
    url: The URL of the website to scrape.
    
    Returns:
    A BeautifulSoup object if the page was retrieved successfully, otherwise None.
    """
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        return BeautifulSoup(response.content, 'html.parser')
    else:
        # Log an error message with the failed status code
        print(f'Failed to retrieve the webpage. Status Code: {response.status_code}')
        return None

def extract_elements(soup: BeautifulSoup) -> list[dict[str, str]]:
    """
    Extracts elements with the 'selecta' class and returns a list of dictionaries 
    containing the 'type' and 'value' of each element.
    
    Args:
    soup: The BeautifulSoup object containing the webpage content.
    
    Returns:
    A list of dictionaries with the extracted information.
    """
    # Find all 'select' elements with class 'selecta'
    select_elements = soup.find_all('select', class_='selecta')
    
    # Initialize an empty list to store the dictionaries
    extracted_info = []
    for select in select_elements:
        select_name = select.get('name')
        for option in select.find_all('option', value=True):  # only iterate options with value
            option_value = option.get('value', '').strip()
            if option_value:  # Check if option has a non-empty value
                extracted_info.append({"type": select_name, "value": option_value})
    return extracted_info

def format_raw_elements(raw_elements: list[dict[str, str]]) -> dict[str, list[str]]:
    """
    Formats a list of raw element dictionaries to a structured dictionary 
    with types as keys and lists of options as values.
    
    Args:
    raw_elements: A list of dictionaries containing 'type' and 'value' keys for each element.
    
    Returns:
    A dictionary with types as keys and a list of respective 'value's as values.
    """
    # Initialize the formatted elements dictionary with empty lists for each type
    formatted_elements = {
        "male_character": [],
        "male_adjective": [],
        "male_action": [],
        "female_character": [],
        "female_adjective": [],
        "female_action": []
    }
    # Mapping from old types to new types
    mapping_type = {
        "protagotronH1": "male_character",
        "protagotronH2": "male_adjective",
        "protagotronM1": "male_action",
        "protagotronF1": "female_character",
        "protagotronF2": "female_adjective",
        "protagotronM2": "female_action"
    }
    # Iterate over the raw elements and reassign them to the new structure
    for item in raw_elements:
        new_type = mapping_type.get(item['type'])
        if new_type and item["value"] not in formatted_elements:
            formatted_elements[new_type].append(item['value'])
    return formatted_elements
