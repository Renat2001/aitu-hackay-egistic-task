import json
import numpy as np
import pandas as pd
import pickle

PATH = "data/"
MODEL_PATH = "segmentation/rid_model.pkl"

def find_json_data(day: int, month: int, year: int):
    day = str(day).zfill(2)
    month = str(month).zfill(2)
    year = str(year)
    filename = year + month + day + ".json"
    filepath = PATH + filename
    with open(filepath) as f: 
        data = json.load(f)
    return data

def process_data(data):
    data = np.array(data)
    data = data[0, :, :]
    return data

def convert_to_json(data):
    data = pd.DataFrame(data)
    data = data.to_dict()
    return data

def get_model():
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    return model

def map_labels(data):
    indices_1 = data==0
    indices_2 = data==1
    indices_3 = data==2
    data[indices_1] = 1
    data[indices_2] = 0
    data[indices_3] = 2
    return data

def cluster_data(model, data):
    height = data.shape[0]
    width = data.shape[1]
    flat_data = data.reshape((height*width, 1))
    predicted_data = model.predict(flat_data)
    predicted_data = map_labels(predicted_data)
    predicted_data = predicted_data.reshape(data.shape)
    return predicted_data
