# Keras Image Classification

This repository contains a FastAPI-based web application that serves a Keras image classification model. The application predicts the category of an uploaded image into one of the following 6 classes:

*   **mountain**
*   **street**
*   **glacier**
*   **buildings**
*   **sea**
*   **forest**

## Project Structure

*   `app.py`: The main FastAPI application file that handles image uploads, preprocessing, and model predictions.
*   `classifier.keras` & `feature_extractor.keras`: The pre-trained Keras models used for classification.
*   `image-classification.ipynb`: Jupyter Notebook containing the code for model training and evaluation.
*   `static/`: Directory for static assets used by the web app.
*   `templates/`: Directory containing HTML templates (e.g., `index.html`) rendered by Jinja2.
*   `requirements.txt`: List of Python dependencies required to run the project.

## Datasets

**Note: The train and test datasets are not included in this repository.**

The original datasets used to train the model are expected to be organized in two main directories:
*   `seg_train/`: Contains the training images, organized into subdirectories named after each class.
*   `seg_test/`: Contains the testing/validation images, organized similarly.

If you wish to retrain or fine-tune the model, you will need to provide your own datasets following this directory structure, or download the original dataset and place it in the `seg_train/` and `seg_test/` directories at the root of the project. The `.gitignore` file is configured to prevent these directories from being uploaded.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd Keras_Image_classification
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To start the FastAPI development server, run the following command:

```bash
uvicorn app:app --reload
```

The application will be accessible at `http://localhost:8000`. You can upload an image through the web interface to get a classification prediction and confidence score.

## API Endpoints

*   `GET /`: Serves the web interface (`index.html`).
*   `POST /predict`: Accepts an uploaded image file (`file`) and returns a JSON response containing the `prediction` and `confidence` percentage.
