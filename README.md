# sap-maintenance-demand-forecasting
Random Forest machine learning model predicting maintenance part demand from SAP usage logs. Features automated feature engineering using Pandas and a Tableau dashboard for inventory optimization.
# Maintenance Demand Forecasting & Inventory Optimization

## 📌 Project Overview
This project leverages historical maintenance usage logs extracted from SAP to forecast future part demand. By implementing a Random Forest predictive model, the system anticipates stock depletion trajectories, ensuring critical maintenance components are reordered proactively rather than reactively. 

**Business Impact:**
* Achieved **85%+ forecast accuracy** on held-out test data.
* Reduced manual stock review time from **~5 hours/week to under 1 hour**.
* Integrated with a Tableau dashboard for visual tracking of 50+ SKU inventory levels and reorder alerts.

*Note: Due to confidentiality agreements, the original SAP datasets have been omitted. A synthetic data generator is provided in the `/data` directory to reproduce the model's functionality.*

## 🛠️ Tech Stack
* **Language:** Python 3.9+
* **Data Engineering:** Pandas, NumPy, openpyxl (for SAP Excel exports)
* **Machine Learning:** Scikit-Learn (RandomForestRegressor)
* **Visualization:** Tableau (Deployed for stakeholder dashboarding)

## 🧠 Feature Engineering
Raw SAP logs were processed to extract meaningful predictive indicators:
1. **Seasonality Flags:** Capturing cyclical maintenance trends (e.g., end-of-year preventative maintenance).
2. **Rolling Consumption Averages:** 7-day, 30-day, and 90-day moving averages for baseline usage.
3. **Failure-Proximity Indicators:** Time-decay features indicating the likelihood of part failure based on historical lifecycle data.

## 🚀 How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Generate synthetic SAP data: `python data/mock_sap_data_gen.py`
3. Train the model and output predictions: `python src/train_rf_model.py`
