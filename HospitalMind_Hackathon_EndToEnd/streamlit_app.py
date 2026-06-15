
import streamlit as st
from src.digital_twin.state import hospital_state

st.title('HospitalMind')
st.metric('ICU Occupied',hospital_state['icu_occupied'])
st.metric('ICU Capacity',hospital_state['icu_capacity'])
