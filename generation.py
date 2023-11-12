import random
def generate_random_character(formatted_elements, sex=None, adjective=False, action=False):
    character_type = sex + "_character" if sex in ['male', 'female'] else None
    adjective_type = sex + "_adjective" if sex in ['male', 'female'] and adjective else None
    action_type = sex + "_action" if sex in ['male', 'female'] and action else None

    if sex not in ['male', 'female']:
        sex = random.choice(['male', 'female'])
        character_type = sex + "_character"
        if adjective:
            adjective_type = sex + "_adjective"
        if action:
            action_type = sex + "_action"

    # Random selection of character, adjective, and action
    character = random.choice(formatted_elements[character_type]) if character_type in formatted_elements else ''
    adjective = random.choice(formatted_elements[adjective_type]) if adjective_type and adjective_type in formatted_elements else ''
    action = random.choice(formatted_elements[action_type]) if action_type and action_type in formatted_elements else ''

    # Create and return the final combination, ensuring non-empty selections are concatenated.
    return ' '.join(filter(None, [character, adjective, action])).strip()