# 🌟 ALUPREDICT – Aluminium Wire Rod Property Prediction System

An AI-powered predictive system for real-time quality assessment in aluminium wire rod manufacturing.

---

## 🚀 Project Overview

**ALUPREDICT** is a machine learning–based system designed to predict critical physical properties of aluminium wire rods:

- **Ultimate Tensile Strength (UTS)**
- **Elongation**
- **Conductivity**
- **Final Grade Classification**

The project helps manufacturers reduce dependency on destructive testing by offering fast, accurate, real-time predictions based on process parameters such as:

- Emulsion conditions  
- Motor readings  
- Cooling water flow  
- Quenching metrics  
- Chemical composition  

---

## ✔️ System Features

- ✔ **Machine Learning models** (LightGBM, XGBoost, Gradient Boost, Random Forest, Extra Trees)  
- ✔ **Flask-based backend**  
- ✔ **Responsive HTML/CSS/JS frontend**  
- ✔ **SQLite database for logs**  
- ✔ **Batch history + PDF report generation**  
- ✔ **Production dashboard**  
- ✔ **Cloud deployment via Render.com**

---

## 🧠 Motivation

Traditional QC methods for aluminium wire rods are slow, destructive, and require skilled labour. With Industry 4.0 advancements, there is a need for non-destructive, real-time, data-driven solutions.

**ALUPREDICT** bridges this gap by predicting mechanical properties using machine learning models trained on synthetic industrial-like datasets.

---

## 🔧 Tech Stack

### **Backend**
- Python 3.12  
- Flask  
- SQLite  
- Pickle / Joblib  

### **Frontend**
- HTML5, CSS3  
- Bootstrap 5  
- JavaScript  
- Chart.js  
- jsPDF  

### **Machine Learning**
- LightGBM  
- XGBoost  
- Random Forest  
- Extra Trees  
- Gradient Boosting  
- Pandas, NumPy, Scikit-learn  

### **Deployment**
- Render.com (Public cloud hosting)

---

## 📊 Features

### 🔹 Machine Learning Predictions  
Predict UTS, Elongation, and Conductivity based on **12+ process parameters**.

### 🔹 Grade Classification  
Automatic grade assignment using predicted values.

### 🔹 User-Friendly Interface  
- Worker Login  
- Data Entry Forms  
- Real-Time Predictions  

### 🔹 Data Storage  
All predictions saved in **predictions.db** containing:  
- Worker ID  
- Date & Time  
- Process Inputs  
- Predicted Values  
- Final Grade  
- Pass/Fail status  

### 🔹 Visual Dashboard  
- Total workers  
- Batch count  
- Pass/fail distribution  
- Star worker of the month  
- Grade distribution charts  

### 🔹 Batch History & PDF Reports  
Download batch reports with **one click**.

---

## 👥 Team Members

- **Sanjana Patil**
- **Lavanya Talele**
- **Aditya Raj**

**Supervisor:** Ms. Hemlata Biradar  
