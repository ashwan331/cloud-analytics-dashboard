# ☁️ Cloud Analytics Dashboard

A full-stack analytics dashboard built using React, Flask, and MySQL to visualize sales data through interactive charts and KPI metrics.

---

## 📌 Project Overview

Organizations need dashboards to monitor and analyze business performance. This project provides an analytics dashboard that retrieves sales data from a MySQL database through a Flask REST API and displays insights using React and Chart.js.

The dashboard enables users to:

- View sales records
- Monitor key business metrics
- Visualize sales trends
- Analyze product performance
- Explore data through interactive charts

---

## 🚀 Features

### Dashboard KPIs
- Total Revenue
- Total Sales Records
- Total Products
- Average Sale Value

### Data Visualization
- Bar Chart for Product Sales
- Pie Chart for Sales Distribution
- Dynamic Data Rendering

### Backend Features
- REST API using Flask
- MySQL Database Integration
- JSON Data Response
- CORS Enabled

### Frontend Features
- React Components
- Axios API Integration
- Responsive Dashboard UI
- Real-Time Data Fetching

---

## 🛠️ Technology Stack

### Frontend
- React.js
- Axios
- Chart.js
- React Chartjs 2

### Backend
- Python
- Flask
- Flask-CORS

### Database
- MySQL

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```text
cloud-dashboard/

├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── Dashboard.js
│   │   └── index.js
│   ├── package.json
│   └── public/
│
├── README.md
└── .gitignore
```

---

## 🗄️ Database Schema

### Sales Table

| Column | Type |
|----------|----------|
| id | INT |
| product | VARCHAR |
| city | VARCHAR |
| amount | INT |
| sale_date | DATE |

---

## 🔌 API Endpoints

### Get All Sales

```http
GET /sales
```

### Sample Response

```json
[
  [1, "Laptop", "Hyderabad", 50000],
  [2, "Phone", "Delhi", 30000],
  [3, "Tablet", "Mumbai", 20000]
]
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/ashwan331/cloud-analytics-dashboard.git
```

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Backend runs on:

```text
http://127.0.0.1:5000
```

### Frontend Setup

```bash
cd frontend

npm install

npm start
```

Frontend runs on:

```text
http://localhost:3000
```

---

## 🔄 Application Workflow

```text
MySQL Database
       ↓
Flask Backend API
       ↓
Axios Requests
       ↓
React Frontend
       ↓
Charts & KPI Dashboard
```

---

## 🎯 Learning Outcomes

Through this project, I learned:

- React Fundamentals
- REST API Development
- Flask Backend Development
- MySQL Database Integration
- Data Visualization using Chart.js
- Axios API Calls
- Git & GitHub Workflow
- Full-Stack Application Architecture

---

## 🔮 Future Enhancements

- AWS Deployment
- Amazon RDS Integration
- AWS Lambda Integration
- Real-Time Data Streaming with Amazon Kinesis
- User Authentication
- Advanced Dashboard Filters
- Export Reports to PDF/Excel

---

## 👨‍💻 Author

**Ashwan**

B.Tech Student | Aspiring Data Analyst | Full Stack & Cloud Enthusiast

GitHub: https://github.com/ashwan331

---

## ⭐ Project Status

✅ Completed

Cloud Analytics Dashboard v1.0