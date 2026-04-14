# Industrial Sentinel: Machine Failure Prediction System 🏭🤖

**Industrial Sentinel** is an end-to-end Machine Learning web application designed to predict and visualize catastrophic machine failures in industrial environments *before* they happen. Built entirely in Python, this capstone project integrates a robust K-Nearest Neighbors (KNN) classification model with a custom-designed, highly interactive Streamlit dashboard.

---

## 🌟 Key Features

* **Real-time Predictive Analytics:** Uses custom sliders (simulating sensor inputs) for Air Temperature, Process Temperature, Rotational Speed, Torque, and Tool Wear to instantly calculate machine failure probability.
* **Live Telemetry Dashboard:** Generates dynamic, simulated real-time data streams for thermal loads, hydrostatic pressure, and acoustic vibrations, mapping engine confidence over time.
* **Automated Alerting System:** Dynamically logs critical incidents, anomalies, and routine sync checks using realistic auto-generated timestamps.
* **Advanced UI UI/UX:** Built with a custom futuristic "glassmorphism" design system. The app operates as a seamless **Single Page Application (SPA)** strictly through advanced Streamlit session states, avoiding typical multi-page loading stutters.

## 🛠️ Technology Stack

* **Backend / Machine Learning:** `scikit-learn` (KNN Classifier), `pandas`, `numpy`, `joblib`
* **Frontend / UI:** `streamlit` (Refactored Single Page Architecture)
* **Styling:** Custom CSS injected via Markdown (Dark mode, glassmorphism, gradient animations)
* **Deployment:** Hosted live on Streamlit Community Cloud

## 🧠 How The Model Works

The prediction engine is trained on standard industrial predictive maintenance parameters. It predicts dual states (**NOMINAL** vs **CRITICAL**) by taking continuous numeric features (temperatures, speed, torque) and categorical machine types. 
The system doesn't only predict a binary outcome, it uses `predict_proba` to calculate a responsive risk score, giving operators a gradient failure probability (%) to schedule preemptive maintenance accurately.

## 💻 Running it Locally

If you'd like to run the app localy, ensure you have Python 3.8+ installed.

1. Clone the repository
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit server:
   ```bash
   streamlit run app.py
   ```
