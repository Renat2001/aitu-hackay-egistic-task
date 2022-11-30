import os
import requests
import pandas as pd
import numpy as np
import matplotlib.colors as mc
import matplotlib.pyplot as plt
import streamlit as st

URL = "http://localhost:8000"
NDVI_SINGLE_MATRIX = URL + "/ndvi/single/matrix"
NDVI_TOTAL_MATRIX = URL + "/ndvi/total/matrix"
NDVI_SEGMENTED_SINGLE_MATRIX = URL + "/ndvi/single/segmented_matrix"
NDVI_SEGMENTED_TOTAL_MATRIX = URL + "/ndvi/total/segmented_matrix"
DIRECTORY = "./data/"

def get_record_dates():
    record_dates = []
    for filename in os.listdir(DIRECTORY):
        year = filename[0:4]
        month = filename[4:6]
        day = filename[6:8]
        record_date = f"{day}.{month}.{year}"
        record_dates.append(record_date)
    return record_dates

def retrieve_numbers_from_date(date: str):
    day, month, year = date.split(".")
    return day, month, year

@st.cache
def request_single_matrix(day: int, month: int, year: int):
    parameters = {"day": day, "month": month, "year": year}
    response = requests.get(NDVI_SINGLE_MATRIX, parameters)
    data = response.json()
    data = pd.DataFrame(data)
    data = data.to_numpy()
    return data

@st.cache
def request_total_matrix():
    response = requests.get(NDVI_TOTAL_MATRIX)
    data = response.json()
    data = pd.DataFrame(data)
    data = data.to_numpy()
    return data

@st.cache
def request_segmented_single_matrix(day: int, month: int, year: int):
    parameters = {"day": day, "month": month, "year": year}
    response = requests.get(NDVI_SEGMENTED_SINGLE_MATRIX, parameters)
    data = response.json()
    data = pd.DataFrame(data)
    data = data.to_numpy()
    return data

@st.cache
def request_segmented_total_matrix():
    response = requests.get(NDVI_SEGMENTED_TOTAL_MATRIX)
    data = response.json()
    data = pd.DataFrame(data)
    data = data.to_numpy()
    return data

def plot_image(data):
    figure = plt.figure(figsize=[10, 10])
    plt.imshow(data, cmap="PiYG", vmin=-1, vmax=1)
    plt.colorbar(shrink=0.6)
    plt.axis("off")
    plt.show()
    return figure

def plot_segmented_image(data):
    cmap = mc.LinearSegmentedColormap.from_list("", 
                                                ["grey", "red", "yellow", "green"],
                                                4)
    figure = plt.figure(figsize=[10, 10])
    plt.imshow(data, cmap=cmap, vmin=0, vmax=3)
    plt.colorbar(shrink=0.6)
    plt.axis("off")
    plt.show()
    return figure
