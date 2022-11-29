import os
import requests
import pandas as pd
import numpy as np
import matplotlib.colors as mc
import matplotlib.pyplot as plt

URL = "http://localhost:8000"
NDVI_MATRIX = URL + "/ndvi/matrix"
NDVI_SEGMENTED_MATRIX = URL + "/ndvi/segmented_matrix"
DIRECTORY = "../data/"

def find_record_months(year: int):
    year = str(year)
    months = []
    for filename in os.listdir(DIRECTORY):
        if filename.startswith(year):
            month = filename[4:6]
            month = int(month)
            months.append(month)
    months = set(months)
    return months

def find_record_days(year: int, month: int):
    year = str(year)
    month = str(month).zfill(2)
    days = []
    for filename in os.listdir(DIRECTORY):
        if filename.startswith(year + month):
            day = filename[6:8]
            day = int(day)
            days.append(day)
    return days

def request_matrix(day: int, month: int, year: int):
    parameters = {"day": day, "month": month, "year": year}
    response = requests.get(NDVI_MATRIX, parameters)
    data = response.json()
    data = pd.DataFrame(data)
    data = data.to_numpy()
    return data

def request_segmented_matrix(day: int, month: int, year: int):
    parameters = {"day": day, "month": month, "year": year}
    response = requests.get(NDVI_SEGMENTED_MATRIX, parameters)
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
                                                ["red", "yellow", "green"],
                                                3)
    figure = plt.figure(figsize=[10, 10])
    plt.imshow(data, cmap=cmap, vmin=0, vmax=2)
    plt.colorbar(shrink=0.6)
    plt.axis("off")
    plt.show()
    return figure
