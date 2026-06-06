# main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

templates = Jinja2Templates(directory="templates")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("owner_encoder.pkl", "rb") as f:
    owner_encoder = pickle.load(f)

with open("transmission_encoder.pkl", "rb") as f:
    transmission_encoder = pickle.load(f)

with open("name_encoder.pkl", "rb") as f:
    name_encoder = pickle.load(f)

with open("fuel_encoder.pkl", "rb") as f:
    fuel_encoder = pickle.load(f)

class CarData(BaseModel):

    Name: str
    Year: int
    Kilometers_Driven: int
    Fuel_Type: str
    Transmission: str
    Owner_Type: str
    Mileage: float
    Engine: int
    Power: float
    Seats: int

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"request": request}
)

@app.post("/predict")
async def predict(data: CarData):

    try:
        features = pd.DataFrame([{

            "Name": data.Name.strip(),
            "Year": data.Year,
            "Kilometers_Driven": data.Kilometers_Driven,
            "Fuel_Type": data.Fuel_Type.strip(),
            "Transmission": data.Transmission.strip(),
            "Owner_Type": data.Owner_Type.strip(),
            "Mileage": data.Mileage,
            "Engine": data.Engine,
            "Power": data.Power,
            "Seats": data.Seats

        }])

        features["Name"] = features["Name"].str.replace(" ", "")

        features["Name"] = name_encoder.transform(
            features["Name"]
        )
        features["Fuel_Type"] = fuel_encoder.transform(
            features["Fuel_Type"]
        )
        features["Transmission"] = transmission_encoder.transform(
            features["Transmission"]
        )
        features["Owner_Type"] = owner_encoder.transform(
            features["Owner_Type"]
        )

        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)[0]

        return JSONResponse({
            "prediction": round(float(prediction), 2)

        })

    except Exception as e:
        print("ERROR:", e)
        return JSONResponse({
            "error": str(e)
        }, status_code=500)