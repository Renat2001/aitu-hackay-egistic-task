import streamlit as st
from utils import *

with st.sidebar:
    year = st.slider("Year:", 2017, 2022, step=1)
    months = find_record_months(year)
    month = st.select_slider("Month: ", months)
    days = find_record_days(year, month)
    day = st.select_slider("Day: ", days)

data = request_matrix(day, month, year)
figure = plot_image(data)
st.pyplot(figure)

segmented_data = request_segmented_matrix(day, month, year)
segmented_figure = plot_segmented_image(segmented_data)
st.pyplot(segmented_figure)