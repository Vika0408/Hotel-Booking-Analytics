# Hotel Booking Analytics & Q&A System

## Overview
This project is a **hotel booking analytics and AI-powered Q&A system** that provides insights from booking data and allows users to ask questions about hotel performance using **Google's Gemini AI**. The system features:

- 📊 **Booking Analytics Dashboard** (Revenue trends, booking patterns, etc.)
- 🤖 **AI-Powered Q&A** (Answer questions using Gemini AI)
- ⚡ **Efficient Data Retrieval** (Using FAISS for similarity search)
- 🚀 **Fast API Responses** (Optimized with Flask)

## Features
- **Interactive analytics dashboard** to explore booking trends
- **AI Q&A system** to answer queries based on hotel data
- **FAISS-based similarity search** for quick information retrieval
- **Optimized API performance** for seamless experience

## Tech Stack
- **Backend:** Flask, Google Gemini AI, FAISS, Sentence Transformers
- **Database:** Pickle-based storage for analytics data
- **Frontend:** HTML, CSS, JavaScript (for the dashboard)

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


## Future Enhancements
- ✅ Deploy on **Render/Vercel** for live access
- ✅ Enhance UI with **React.js**
- ✅ Add support for **multilingual AI responses**

---
👨‍💻 **Developed by:** Vanshika ✨  
📌 **GitHub Repo:** [Hotel-Booking-Analytics](https://github.com/Vika0408/Hotel-Booking-Analytics)

