# Credit Risk Assessment System

![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-red?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-f7931e?logo=scikit-learn)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Demo Status](https://img.shields.io/badge/Demo-LIVE-green)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-blue?logo=githubpages)

## AI-Powered Credit Risk Assessment for Financial Institutions 🏦

[![Live Demo](https://img.shields.io/badge/Demo-Live%20Site-blue?style=for-the-badge)](https://akshata-yadav-20.github.io/Credit-Risk-Assessment/)
[![View on GitHub](https://img.shields.io/badge/GitHub-Checkout%20Repo-black?style=for-the-badge&logo=github)](https://github.com/akshata-yadav-20/Credit-Risk-Assessment)

### 🔥 LIVE DEMO: https://akshata-yadav-20.github.io/Credit-Risk-Assessment/

---

## Overview

Financial institutions face significant challenges in identifying potential loan defaulters. The **Credit Risk Assessment System** is an AI-powered solution that leverages machine learning to predict customer creditworthiness using financial and demographic data, helping financial institutions make data-driven lending decisions.

---

## 🎯 Key Features

- ✅ **AI-Powered**: Random Forest classifier trained on 10,000+ synthetic samples
- ✅ **Real-time**: Instant risk assessment in milliseconds
- ✅ **Secure**: Privacy-focused - no sensitive data stored or transmitted
- ✅ **Modern UI**: Dark-themed, responsive interface with real-time validation
- ✅ **Multiple Deployment Options**: Flask server, static HTML, or GitHub Pages
- ✅ **Live Demo**: Try it now at https://akshata-yadav-20.github.io/Credit-Risk-Assessment/

---

## 🚀 Quick Start

### Option 1: Use the Live Demo (No Installation Required)
Simply visit: **https://akshata-yadav-20.github.io/Credit-Risk-Assessment/**

The demo runs entirely in your browser - fill in customer details and get instant risk assessment!

### Option 2: Run Locally

```bash
# Clone the repository
git clone https://github.com/akshata-yadav-20/Credit-Risk-Assessment.git
cd Credit-Risk-Assessment

# Install dependencies
pip install -r requirements.txt

# Train the model (first time only)
python ml/train_model.py

# Start the Flask server
python run.py

# Open http://localhost:5000 in your browser
```

---

## 💻 Usage

### Web Interface
1. Open https://akshata-yadav-20.github.io/Credit-Risk-Assessment/
2. Fill in customer details (Age, Income, Loan Amount, Credit Score, etc.)
3. Click **Assess Credit Risk**
4. View the risk assessment result with probability and recommendation

### API Usage

```bash
curl -X POST http://localhost:5000/assess \
  -H "Content-Type: application/json" \
  -d '{
    "age": 35,
    "income": 50000,
    "loan_amount": 15000,
    "credit_score": 650,
    "employment_length": 5,
    "debt_to_income": 0.3,
    "existing_loans": 1,
    "education": 1,
    "marital_status": 1,
    "home_ownership": 0
  }'
```

### Response Format
```json
{
  "success": true,
  "risk_level": "LOW RISK",
  "probability": 85.5,
  "confidence": 92.3,
  "recommendation": "Approve Loan",
  "prediction_class": 0
}
```

---

## 🤖 Model Details

### Algorithm
**Random Forest Classifier** - An ensemble learning method that operates by constructing multiple decision trees.

### Training Data
- **Samples**: 10,000 synthetic customer profiles
- **Features**: 10 input features (demographic and financial)
- **Target**: Binary classification (Low Risk / High Risk)

### Input Features

| Feature | Description | Range/Type |
|---------|-------------|------------|
| `age` | Customer age | 18-75 years |
| `income` | Annual income | $0+ |
| `loan_amount` | Requested loan amount | $0+ |
| `credit_score` | Credit score | 300-850 |
| `employment_length` | Years employed | 0-30+ |
| `debt_to_income` | Debt-to-income ratio | 0.1-0.8 |
| `existing_loans` | Number of existing loans | 0-5 |
| `education` | Education level | 0-3 (High School to PhD) |
| `marital_status` | Marital status | 0-2 (Single to Divorced) |
| `home_ownership` | Home ownership type | 0-2 (Rent to Mortgage) |

### Performance Metrics
- **Accuracy**: ~95%
- **Precision**: ~0.94
- **Recall**: ~0.93
- **F1-Score**: ~0.93

---

## 📡 API Reference

### POST /assess
Assess credit risk for a customer.

**Request Body:**
```json
{
  "age": 35,
  "income": 50000,
  "loan_amount": 15000,
  "credit_score": 650,
  "employment_length": 5,
  "debt_to_income": 0.3,
  "existing_loans": 1,
  "education": 1,
  "marital_status": 1,
  "home_ownership": 0
}
```

**Response:**
```json
{
  "success": true,
  "risk_level": "LOW RISK",
  "probability": 85.5,
  "confidence": 92.3,
  "recommendation": "Approve Loan",
  "prediction_class": 0
}
```

### GET /api/features
Get information about input features.

---

## 📁 Project Structure

```
credit-risk-assessment/
├── app/
│   ├── __init__.py              # Flask application with API endpoints
│   └── templates/
│       ├── index.html           # Main UI (Flask backend integration)
│       └── index_static.html    # Standalone demo (client-side only)
├── ml/
│   ├── __init__.py              # Model loading and inference
│   └── train_model.py           # Model training script
├── models/                      # Directory for saved ML models
├── data/                        # Directory for datasets
├── .github/workflows/           # GitHub Actions CI/CD
├── demo.html                    # Single-file demo version
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
├── pyproject.toml               # Project configuration
└── README.md                    # This file
```

---

## 🛠️ Development

```bash
# Clone the repository
git clone https://github.com/akshata-yadav-20/Credit-Risk-Assessment.git
cd Credit-Risk-Assessment

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python run.py
```

### Model Training
```bash
python ml/train_model.py
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Contact

**Akshata Yadav** - [@akshata-yadav-20](https://github.com/akshata-yadav-20)

- **Live Demo**: https://akshata-yadav-20.github.io/Credit-Risk-Assessment/
- **GitHub**: https://github.com/akshata-yadav-20/Credit-Risk-Assessment

---

## 🙏 Acknowledgments

- **Framework**: [scikit-learn](https://scikit-learn.org/)
- **Backend**: [Flask](https://flask.palletsprojects.com/)
- **Frontend**: [Bootstrap 5](https://getbootstrap.com/)
- **Icons**: [Font Awesome 6](https://fontawesome.com/)