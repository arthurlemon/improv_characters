import streamlit as st
import json
from generation import generate_random_character

@st.cache_data
def load_data() -> dict:
    """Load character data from a JSON file into a dictionary.

    This function reads a JSON file into a dictionary and caches the result to
    prevent unnecessary file reads on subsequent calls until the file changes.

    Returns:
        The dictionary containing character data.
    """
    with open('character_list.json', 'r', encoding='utf-8') as f:  # It's good practice to specify encoding
        data = json.load(f)
    return data

character_list = load_data()

st.subheader('Improv Character Generator')

# User inputs for the character generation
sex = st.radio("Choose the character's sex", ('any', 'male', 'female'))
adjective = st.checkbox('Include an adjective')
action = st.checkbox('Include an action')

# Button to generate character
if st.button('Generate Character'):
    # Call the function to generate a random character
    character_combination = generate_random_character(character_list, sex, adjective, action)
    # Display the generated character combination
    st.subheader(character_combination)