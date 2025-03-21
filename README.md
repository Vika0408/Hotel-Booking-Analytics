# Hotel Booking Analytics & Q&A System

**📌 Overview**

This project is an AI-powered Hotel Booking Analytics & QA System, built as part of the Solvei8 AI/ML Internship Assignment. The system provides insightful analytics on hotel bookings and allows users to ask questions about the data using a retrieval-augmented question-answering (RAG) system. The backend is implemented in Flask, and the AI-powered Q&A functionality is driven by Google Gemini.


**✨ Features**

Interactive Hotel Booking Analytics Dashboard 📊

Retrieval-Augmented Question Answering (RAG) 🤖

Semantic Search using FAISS 🔍

AI-powered responses via Google Gemini 🚀

Optimized API response time ⚡

Fast and efficient data retrieval 🔄


**🛠 Tech Stack**

Backend: Flask, FastAPI

AI Model: Google Gemini API

Vector Database: FAISS

Machine Learning: Sentence Transformers

Data Processing: Pandas, Numpy

Version Control: Git, GitHub

## Setup Instructions
### 1️⃣ Clone the Repository
```sh
 git clone https://github.com/Vika0408/Hotel-Booking-Analytics.git
 cd Hotel-Booking-Analytics
```

### 2️⃣ Install Dependencies
```sh
 pip install -r requirements.txt
```

### 3️⃣ Set Up API Key (Google Gemini)
Set your API key as an environment variable:
```sh
export GOOGLE_API_KEY='your_api_key_here'
```
(For Windows, use `set GOOGLE_API_KEY=your_api_key_here` in cmd.)

### 4️⃣ Run the Application
```sh
 python app.py
```

### 5️⃣ Access the Dashboard
Open your browser and go to:
```
http://127.0.0.1:5000/
```

## API Endpoints
| Endpoint      | Method | Description |
|--------------|--------|-------------|
| `/` | GET | Load the home page |
| `/analytics` | GET | Fetch booking analytics data |
| `/ask` | POST | Get AI-generated responses |

![screencapture-127-0-0-1-5000-2025-03-21-14_50_49](https://github.com/user-attachments/assets/29a1a0e9-2b72-48a2-a2ad-532404c0e52b)


## Example Queries & Responses
### **1️⃣ Analytics Data** (`/analytics`)
📌 **Sample Output:**  
```json
{
  "total_bookings": 1250,
  "average_booking_price": 120.5,
  "revenue_trend": {
    "January": 10000,
    "February": 12000,
    "March": 15000
  }
}
```

### **2️⃣ AI Q&A Response** (`/ask`)
**Example Query:**
```json
{
  "query": "What is the total revenue for March?"
}
```
📌 **Sample Output:**  
```json
{
  "answer": "The total revenue for March is $15,000."
}
```

## Performance Optimization
✅ **Reduced API latency** by optimizing FAISS queries  
✅ **Improved AI response accuracy** using structured prompts  
✅ **Compressed data for faster retrieval**  

## Screenshots
![screencapture-127-0-0-1-5000-2025-03-21-14_51_18](https://github.com/user-attachments/assets/4124406c-5049-4e9c-bf90-dda12979b82a)
![screencapture-127-0-0-1-5000-2025-03-21-14_53_33](https://github.com/user-attachments/assets/6df40bcb-c606-4dd7-bd5f-86394c4b5389)
![screencapture-127-0-0-1-5000-2025-03-21-14_54_14](https://github.com/user-attachments/assets/1f893b55-46bf-4daa-8634-71ffe3e75826)


📊 Performance Evaluation

✅ Accuracy of Q&A Responses: Evaluated based on sample queries.

⚡ API Response Time: Optimized for fast retrieval.

🔥 Future Enhancements

✅ Improve NLP capabilities with additional LLMs.

✅ Implement better caching mechanisms for faster response.

✅ Enhance the frontend with interactive charts.

---
👨‍💻 **Developed by:** Vanshika ✨  
📌 **GitHub Repo:** [Hotel-Booking-Analytics](https://github.com/Vika0408/Hotel-Booking-Analytics)

