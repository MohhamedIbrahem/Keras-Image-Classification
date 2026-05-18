from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from tensorflow.keras.models import load_model

from PIL import Image

import numpy as np
import io

app = FastAPI()

# Load Models
classifier = load_model("classifier.keras")
feature_extractor = load_model("feature_extractor.keras")

# Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Classes
class_names = [
    "mountain",
    "street",
    "glacier",
    "buildings",
    "sea",
    "forest"
]


# Home Route
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# Image Preprocessing
def preprocess_image(image):

    # IMPORTANT:
    # Change this if your model trained on another size
    image = image.resize((150, 150))

    image = np.array(image)

    image = image / 255.0

    image = np.expand_dims(image, axis=0)

    return image


# Prediction Route
@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")

    processed_image = preprocess_image(image)

    # Extract Features
    features = feature_extractor.predict(processed_image)

    # Classification
    prediction = classifier.predict(features)

    predicted_index = np.argmax(prediction)

    predicted_class = class_names[predicted_index]

    confidence = float(np.max(prediction) * 100)


    # Confidence Threshold
    if confidence < 70:

        predicted_class = "Unknown Image"


    return {
        "prediction": predicted_class,
        "confidence": round(confidence, 2)
    }