from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
from segmentation.utils import *

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

@app.get("/ndvi/matrix")
def ndvi_matrix(day: int, month: int, year: int):
    data = find_json_data(day, month, year)
    data = process_data(data)
    data = convert_to_json(data)
    return data

@app.get("/ndvi/segmented_matrix")
def ndvi_segmented_matrix(day: int, month: int, year: int):
    data = find_json_data(day, month, year)
    data = process_data(data)
    model = get_model()
    data = cluster_data(model, data)
    data = convert_to_json(data)
    return data

    