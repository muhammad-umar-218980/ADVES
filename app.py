
import streamlit as st

st.set_page_config(
    page_title="ADVES",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ ADVES")
st.subheader(
    "Aviation Diagnostic & Verification Expert System"
)

st.write(
    "An educational, rule-based aviation diagnostic system."
)

st.warning(
    "Educational simulation only. Not for real aircraft "
    "maintenance or flight-safety decisions."
)

st.success("ADVES application initialized successfully!")
