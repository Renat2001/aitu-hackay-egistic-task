import json
import numpy as np
import pandas as pd
import pickle
import os

PATH = "data/"
TOTAL_MATRIX_PATH = "segmentation/total_matrix.txt"

def get_all_json_data():
    all_data = []
    for filename in os.listdir(PATH):
        filepath = PATH + filename
        with open(filepath) as f: 
            data = json.load(f)
        data = np.array(data)
        data = data[0, :, :]
        all_data.append(data)
    return all_data

def process_matrices(matrices):
    matrices = tuple(matrices)
    total_matrix = np.dstack(matrices)
    total_matrix = np.mean(total_matrix, 2)
    return total_matrix

def find_json_data(day: str, month: str, year: str):
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

def cluster_matrix(matrix):
    non_vegetation = matrix<=0
    weak = (matrix>0) & (matrix<=0.05)
    moderate = (matrix>0.05) & (matrix<=0.25)
    good = matrix>0.25
    matrix[non_vegetation] = 0
    matrix[weak] = 1
    matrix[moderate] = 2
    matrix[good] = 3
    return matrix

def load_total_matrix():
    with open(TOTAL_MATRIX_PATH, "rb") as f:
        total_matrix = pickle.load(f)
    return total_matrix
