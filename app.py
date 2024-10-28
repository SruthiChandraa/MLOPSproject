from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load the model and vectorizer
with open('model.pkl', 'rb') as model_file, open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    model = pickle.load(model_file)
    tfidf_vectorizer = pickle.load(vectorizer_file)

@app.route('/')
def home():
    return send_file('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    text = data['text']
    tfidf_text = tfidf_vectorizer.transform([text])
    prediction = model.predict(tfidf_text)[0]
    return jsonify({'emotion': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
