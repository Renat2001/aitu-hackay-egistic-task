from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from segmentation.utils import *

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.get("/ndvi/single/matrix")
def ndvi_matrix(day: str, month: str, year: str):
    matrix = find_json_data(day, month, year)
    matrix = process_data(matrix)
    matrix = convert_to_json(matrix)
    return matrix

@app.get("/ndvi/total/matrix")
def ndvi_total_matrix():
    total_matrix = load_total_matrix()
    total_matrix = convert_to_json(total_matrix)
    return total_matrix

@app.get("/ndvi/single/segmented_matrix")
def ndvi_segmented_matrix(day: str, month: str, year: str):
    matrix = find_json_data(day, month, year)
    matrix = process_data(matrix)
    matrix = cluster_matrix(matrix)
    matrix = convert_to_json(matrix)
    return matrix

@app.get("/ndvi/total/segmented_matrix")
def ndvi_segmented_total_matrix():
    total_matrix = load_total_matrix()
    segmented_total_matrix = cluster_matrix(total_matrix)
    segmented_total_matrix = convert_to_json(segmented_total_matrix)
    return segmented_total_matrix

    