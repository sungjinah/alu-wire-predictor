from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import sqlite3
from datetime import datetime
import joblib

app = Flask(__name__)
CORS(app)

# 🔄 Load models and objects
with open("lgb_model_uts.pkl", "rb") as f:
    model_uts = pickle.load(f)
with open("lgb_model_elongation.pkl", "rb") as f:
    model_elong = pickle.load(f)
with open("lgb_model_conductivity.pkl", "rb") as f:
    model_cond = pickle.load(f)

scaler = joblib.load("scaler.pkl")

# ⛔ Replace this with your actual feature column names (must match model training)
features = joblib.load("features.pkl")
feature_names = features.columns.tolist()

# 📦 Setup SQLite DB
DB_FILE = "predictions.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        worker_name TEXT,
        batch_number TEXT,
        input_data TEXT,
        uts REAL,
        elongation REAL,
        conductivity REAL,
        grade TEXT,
        status TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

# 🧠 Grade logic
def classify_grade(conductivity, diameter):
    diameter = float(diameter)
    if diameter == 9.5:
        if conductivity >= 61.5:
            return "WE10"
        elif conductivity >= 61.0:
            return "WE20"
        else:
            return "WC10"
    elif diameter == 11.5:
        if conductivity >= 61.5:
            return "WE12"
        elif conductivity >= 61.0:
            return "WE22"
        else:
            return "WC12"
    return "Unknown"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # 🌐 Extract meta info
        worker_name = data.get("worker_name", "Unknown")
        batch_number = data.get("batch_number", "Unknown")
        status = data.get("status", "Pass")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 🛠️ Build feature input
        input_data = {k: float(v) for k, v in data.items() if k in feature_names}
        diameter = float(data.get("diameter", 9.5))

        input_df = pd.DataFrame([input_data])

        # ✅ Add any missing columns with 0
        for col in feature_names:
            if col not in input_df.columns:
                input_df[col] = 0

        # 🧱 Reorder columns as per training
        input_df = input_df[feature_names]

        # 🔄 Scale only numeric cols
        numeric_cols = input_df.select_dtypes(include=["float64", "int64"]).columns
        input_df[numeric_cols] = scaler.transform(input_df[numeric_cols])

        # 🤖 Predict
        uts = float(model_uts.predict(input_df)[0])
        elong = float(model_elong.predict(input_df)[0])
        cond = float(model_cond.predict(input_df)[0])
        grade = classify_grade(cond, diameter)

        # 💾 Store into SQLite
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''
            INSERT INTO predictions (date, worker_name, batch_number, input_data, uts, elongation, conductivity, grade, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (date, worker_name, batch_number, str(input_data), uts, elong, cond, grade, status)
        )
        conn.commit()
        conn.close()

        # 🔁 Return predictions
        return jsonify({
            "uts": round(uts, 2),
            "elongation": round(elong, 2),
            "conductivity": round(cond, 2),
            "grade": grade
        })

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/save", methods=["POST"])
def save_status():
    try:
        data = request.json
        worker_name = data.get("worker_name")
        batch_number = data.get("batch_number")
        status = data.get("status")

        if not all([worker_name, batch_number, status]):
            return jsonify({"success": False, "error": "Missing fields"})

        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute('''
            UPDATE predictions
            SET status = ?
            WHERE worker_name = ? AND batch_number = ?
            ORDER BY id DESC LIMIT 1
        ''', (status, worker_name, batch_number))
        conn.commit()
        conn.close()

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/get_history", methods=["GET"])
def get_history():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
    SELECT worker_name, batch_number, date, uts, elongation, conductivity, grade, status
    FROM predictions ORDER BY date DESC
    """)
    rows = c.fetchall()
    conn.close()

    result = {}
    for worker, batch, date, uts, elong, cond, grade, status in rows:
        key = (worker, date[:10], batch)
        if key not in result:
            result[key] = []
        result[key].append({
        "time": date[11:],
        "uts": round(uts, 2),
        "elong": round(elong, 2),
        "cond": round(cond, 2),
        "grade": grade,
        "status": status
          # ✅ Add this
    })

    # Format for frontend
    formatted = []
    for (worker, date, batch), records in result.items():
        formatted.append({
            "worker": worker,
            "date": date,
            "batch": batch,
            "records": records
        })

    return jsonify(formatted)

# 🌐 Serve HTML pages
@app.route("/")
def home():
    return render_template("Home.html")

@app.route("/predict_page")
def predict_page():
    return render_template("predict_page.html")

@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
