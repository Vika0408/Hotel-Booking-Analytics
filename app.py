import os
import pickle
import faiss
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# Load Google API Key from environment variables
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("⚠️ GOOGLE_API_KEY is missing. Set it in your environment variables.")

genai.configure(api_key=google_api_key)

# Initialize the Gemini AI model
gemini_model = genai.GenerativeModel("gemini-1.5-pro-latest") 


# Load analytics data
with open("analytics.pkl", "rb") as f:
    analytics = pickle.load(f)

# Convert dictionary keys to string format
def convert_keys_to_str(d):
    if isinstance(d, dict):
        return {str(k): convert_keys_to_str(v) for k, v in d.items()}
    elif isinstance(d, list):
        return [convert_keys_to_str(i) for i in d]
    elif isinstance(d, pd.Period):
        return str(d)
    return d

analytics = convert_keys_to_str(analytics)

# Compute average booking price if revenue data exists
if "revenue_trend" in analytics:
    total_revenue = sum(analytics["revenue_trend"].values())
    total_bookings = analytics.get("total_bookings", 1)
    analytics["average_booking_price"] = total_revenue / total_bookings if total_bookings > 0 else 0

# Load FAISS index
try:
    index = faiss.read_index("faiss_index.bin")
except Exception as e:
    print(f"Error loading FAISS index: {e}")
    index = None

# Load sentence transformer model (rename to avoid conflicts)
try:
    with open("sentence_transformer.pkl", "rb") as f:
        sentence_model = pickle.load(f)  # Renamed to avoid conflict
except Exception as e:
    print(f"Error loading Sentence Transformer model: {e}")
    sentence_model = None

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analytics", methods=["GET"])
def get_analytics():
    return jsonify(analytics)

def generate_ai_response(query):
    """Uses Google's Gemini API to generate intelligent responses."""
    prompt = f"""
    You are an AI assistant. Answer based on the following analytics:

    {analytics}

    Question: {query}
    Answer:
    """
    try:
        gemini_model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Correct model
        response = gemini_model.generate_content(prompt)
        return response.text if hasattr(response, "text") else response
    except Exception as e:
        print(f"AI response failed: {e}")
        return "Error processing AI response."


@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json
        query = data.get("query", "")

        response = generate_ai_response(query)
        return jsonify({"answer": response})
    except Exception as e:
        print("Google AI API Error:", str(e))
        return jsonify({"answer": f"Error processing AI response: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
