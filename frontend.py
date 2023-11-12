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

st.subheader('Générateur de Personnages')

st.markdown("Utlisez-moi pour varier vos personnages en impro !")
st.write(f"Inspiré de [ce site](http://www.improse.net/res/geneperso.htm)")

# User inputs for the character generation
sex = st.radio("Choisir un genre pour le personnage", ('homme', 'femme', "peu importe"), index=2)
adjective = st.checkbox('Inclure un adjectif')
action = st.checkbox('Inclure une action')

# Button to generate character
if st.button('Créer un personnage'):
    # Call the function to generate a random character
    character_combination = generate_random_character(character_list, sex, adjective, action)
    # Display the generated character combination
    st.subheader(character_combination)