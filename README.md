🌟 ALUPREDICT – Aluminium Wire Rod Property Prediction System

An AI-powered predictive system for real-time quality assessment in aluminium wire rod manufacturing.

🚀 Project Overview

ALUPREDICT is a machine learning–based system designed to predict the following key physical properties of aluminium wire rods:

Ultimate Tensile Strength (UTS)

Elongation

Conductivity

Final Grade Classification

It helps manufacturers reduce dependency on destructive testing by offering fast, accurate, real-time predictions based on process parameters such as:

Emulsion conditions

Motor readings

Cooling water flow

Quenching metrics

Chemical composition

🧠 Features

✔ Machine Learning Models (LightGBM, XGBoost, Random Forest, Gradient Boost, Extra Trees)
✔ Flask-based backend
✔ Responsive HTML/CSS/JS frontend
✔ SQLite database for logs
✔ Batch history + PDF report generation
✔ Production dashboard
✔ Cloud deployment via Render.com

🛠 Tech Stack
Backend

Python 3.12

Flask

SQLite

Pickle / Joblib

Frontend

HTML5, CSS3

JavaScript

Bootstrap 5

Chart.js

jsPDF

Machine Learning

LightGBM

XGBoost

Random Forest

Extra Trees

Gradient Boosting

Pandas, NumPy, Scikit-learn

📁 Project Structure
/models
/templates
/static
predictions.db
app.py
README.md

📊 Model Performance (Summary)
Property	Best Model	R² Score
UTS	LightGBM	0.9387
Elongation	LightGBM	0.9436
Conductivity	XGBoost	0.9665
💻 Installation
1️⃣ Clone the repository
git clone https://github.com/sungjinah/alu-wire-predictor.git

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Flask server
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000/

👩‍💻 Team Members

Sanjana Patil (21CE1193)

Lavanya Talele (21CE1160)

Aditya Raj (21CE1156)

Supervisor: Ms. Hemlata Biradar
Institute: Ramrao Adik Institute of Technology
