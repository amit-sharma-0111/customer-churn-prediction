# 📊 Customer Churn Prediction — ML Web App

![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-blue)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-red)
![Python](https://img.shields.io/badge/Python-3.x-green)
![Status](https://img.shields.io/badge/Status-Live-success)

🌐 **Live Demo:** [Click here to open app](https://customer-churn-prediction-qkhqckxgslf4zqxau7ny6j.streamlit.app/)

---

## 📌 About the Project

A **Customer Churn Prediction** system built using **Random Forest Machine Learning**. It predicts whether a customer is likely to leave a service based on their behavior and subscription data. Deployed as an interactive web app using **Streamlit Cloud**.

---

## ✨ Features

- ✅ Real-time customer churn prediction
- ✅ Probability-based churn **Risk Score (%)**
- ✅ 🎯 Visual **Risk Meter** (Low / Medium / High)
- ✅ ⚠️ Smart **Input Validation Warnings**
- ✅ 🔄 Reset button to clear inputs
- ✅ 🕐 **Prediction History** table with all past predictions
- ✅ 🗑️ Clear history option
- ✅ Responsive 2-column layout

---

## 🛠 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Scikit-learn | ML model (Random Forest) |
| Pandas & NumPy | Data processing |
| Streamlit | Web app & deployment |
| Joblib | Model serialization |

---

## 📂 Project Structure

```
customer-churn-prediction/
│
├── app.py                          # Main Streamlit app
├── requirements.txt                # Python dependencies
├── models/
│   └── churn_model.pkl             # Trained ML model
├── data/
│   ├── customer_churn_dataset-train.csv
│   └── customer_churn_dataset-test.csv
└── notebooks/
    └── churn_training.ipynb        # Model training notebook
```

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/amit-sharma-0111/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

---

## 📊 Input Features

| Feature | Description |
|---------|-------------|
| Age | Customer's age |
| Gender | Male / Female |
| Tenure | Months as a customer |
| Usage Frequency | How often they use the service |
| Support Calls | Number of support calls made |
| Payment Delay | Days payment was delayed |
| Subscription Type | Basic / Standard / Premium |
| Contract Length | Length of contract in months |
| Total Spend | Total amount spent |
| Last Interaction | Days since last interaction |

---

## 🎯 Model Performance

- **Algorithm:** Random Forest Classifier
- **Dataset:** 4,00,000+ customer records
- **Output:** Churn (1) / Stay (0) + Risk Probability %
