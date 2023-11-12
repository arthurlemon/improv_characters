import streamlit as st
import json
from generation import generate_random_character

@st.cache_data
def load_data():
    with open('character_list.json', 'r') as f:
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