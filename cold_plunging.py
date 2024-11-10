import streamlit as st
import folium
import os
from streamlit_folium import st_folium
import pandas as pd

deception_pass_url = f"https://raw.githubusercontent.com/christyheaton/cold_plunging_streamlit/refs/heads/main/static/deception_pass.jpg"
lake_wenatchee_url = f"https://raw.githubusercontent.com/christyheaton/cold_plunging_streamlit/refs/heads/main/static/lake_wenatchee.jpg"

data = pd.DataFrame({
    'location': ['Deception Pass', 'Lake Wenatchee'],
    'latitude': [48.4012729, 47.8067988],
    'longitude': [-122.66431, -120.7265622],
    'photo_url': [deception_pass_url, lake_wenatchee_url],
    'description': ['Deception Pass', 'Lake Wenatchee']
})
st.table(data)

m = folium.Map(location=[47.6062, -122.3321], zoom_start=8)

for _, row in data.iterrows():
    folium.Marker(
    [row['latitude'], row['longitude']],
    icon=folium.DivIcon(html=f"""<div style="font-size: 24px;">🌊</div>"""),
    popup=folium.Popup(f"<strong>{row['location']}</strong><br><img src='{row['photo_url']}' width='150'><br>{row['description']}", max_width=300)
).add_to(m)

st.title("Cold Plunge Locations")
st_folium(m, width=725)
