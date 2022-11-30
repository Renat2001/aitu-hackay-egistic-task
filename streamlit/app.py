import streamlit as st
from utils import *

column_1, column_2 = st.columns(2)

with st.sidebar:
    record_dates = get_record_dates()
    record_date = st.selectbox("Record dates:", record_dates)
    day, month, year = retrieve_numbers_from_date(record_date)

single_matrix = request_single_matrix(day, month, year)
segmented_single_matrix = request_segmented_single_matrix(day, month, year)

column_1.header("NDVI single matrix image")
single_figure = plot_image(single_matrix)
column_1.pyplot(single_figure)

column_2.header("NDVI segmented single matrix image")
segmented_single_figure = plot_segmented_image(segmented_single_matrix)
column_2.pyplot(segmented_single_figure)

total_matrix = request_total_matrix()
segmented_total_matrix = request_segmented_total_matrix()

column_1.header("NDVI total matrix image")
total_figure = plot_image(total_matrix)
column_1.pyplot(total_figure)

column_2.header("NDVI segmented total matrix image")
total_segmented_figure = plot_segmented_image(segmented_total_matrix)
column_2.pyplot(total_segmented_figure)