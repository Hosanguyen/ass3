from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import os

app = Flask(__name__)
CORS(app)

# Constants from training
max_words = 10000
max_len = 20
basepath = os.path.dirname(__file__)
# Load trained model
model_path = os.path.join(basepath, "LSTM_model.h5")
if os.path.exists(model_path):
    print("Loading model from disk...")
model = tf.keras.models.load_model(model_path)

# Initialize tokenizer with the same parameters as in training
# tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
# Replace the tokenizer initialization line with:
with open(os.path.join(basepath,'tokenizer.pickle'), 'rb') as handle:
    tokenizer = pickle.load(handle)

# Map prediction indices to sentiment labels
sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    comment = data["comment"]
    
    # Preprocess the comment
    comment_test_seq = tokenizer.texts_to_sequences([comment])
    comment_test_pad = pad_sequences(comment_test_seq, maxlen=max_len)
    
    # Make prediction
    prediction = model.predict(comment_test_pad)
    sentiment_index = np.argmax(prediction[0])
    sentiment_label = sentiment_map[sentiment_index]
    confidence = float(prediction[0][sentiment_index])
    
    # Return only the highest prediction
    response = {
        "comment": comment,
        "sentiment": sentiment_label,
        "confidence": confidence
    }
    
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)