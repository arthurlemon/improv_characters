import random

def generate_random_character(formatted_elements: dict[str, list[str]], sex: str | None = None, 
                              adjective: bool = False, action: bool = False) -> str:
    """
    Generate a random character description based on specified attributes.
    
    This function creates a random combination of character attributes for improvisational purposes. 
    It allows the user to specify a sex ('male', 'female'), and whether to include an adjective and/or an action.
    
    Args:
        formatted_elements: A dictionary with keys as attribute types and values as lists of corresponding options.
        sex: The sex of the character to generate ('male', 'female', or 'any'/'None' for no preference).
        adjective: A boolean indicating whether to include an adjective in the description.
        action: A boolean indicating whether to include an action in the description.
        
    Returns:
        A string with the randomly generated character description.
    """
    
    
    translation = {"homme": "male", "femme": "female"}
    sex = translation.get(sex)
    
    if sex in ['male', 'female']:
        character_type = f"{sex}_character"
        adjective_type = f"{sex}_adjective" if adjective else ''
        action_type = f"{sex}_action" if action else ''
    else:  # If sex is not specified or is 'any', choose randomly
        sex = random.choice(['male', 'female'])
        character_type = f"{sex}_character"
        adjective_type = f"{sex}_adjective" if adjective else ''
        action_type = f"{sex}_action" if action else ''

    # Random selection of character, adjective, and action
    character = random.choice(formatted_elements[character_type])
    adjective = random.choice(formatted_elements[adjective_type]) if adjective else ''
    action = random.choice(formatted_elements[action_type]) if action else ''

    # Combine the results and return them
    return ' '.join(part for part in [character, adjective, action] if part).strip()