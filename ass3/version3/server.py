from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
import pandas as pd

# Load trained deep learning model
model = tf.keras.models.load_model("diabetes_model.h5")
app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  # Get JSON data from frontend
    features = np.array(data["features"]).reshape(1, -1)  # Convert to NumPy array

    # Make prediction
    prediction = model.predict(features)[0][0]
    result = "Diabetic" if prediction > 0.5 else "Non-Diabetic"
    return jsonify({"prediction": result, "probability": float(prediction)})

if __name__ == "__main__":
    app.run(debug=True, port=5000)