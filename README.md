# Credit Risk Assessment System

![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-red?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.0-f7931e?logo=scikit-learn)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![Demo](https://img.shields.io/badge/Demo-Live%20Site-blue)](https://akshata-yadav-20.github.io/Credit-Risk-Assessment/)

## AI-Powered Credit Risk Assessment for Financial Institutions

A comprehensive machine learning system that predicts customer creditworthiness using financial and demographic data, helping financial institutions identify potential loan defaulters.

---

## 🎯 Key Features

- **AI-Powered**: Random Forest classifier trained on 10,000+ synthetic samples
- **Real-time**: Instant risk assessment in milliseconds
- **Secure**: Privacy-focused - no sensitive data stored or transmitted
- **Modern UI**: Dark-themed, responsive interface with real-time validation
- **Multiple Deployment Options**: Flask server, static HTML, or GitHub Pages

---

## 🚀 Live Demo

**[🔗 Click here to access the live demo](https://akshata-yadav-20.github.io/Credit-Risk-Assessment/)**

The demo runs entirely in your browser - no installation required. Simply open the link, fill in customer details, and get instant credit risk assessment.

### Demo Screenshots

<img src="https://via.placeholder.com/800x400/1a365d/ffffff?text=Credit+Risk+Assessment+Demo" alt="Demo Preview" width="100%" style="border-radius: 8px;" />

---

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [API Reference](#api-reference)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## ⚙️ Installation

### Prerequisites
- Python 3.9+
- pip

### Setup Steps

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

1. Start the server: `python run.py`
2. Navigate to `http://localhost:5000`
3. Fill in customer details:
   - Age
   - Annual Income
   - Loan Amount
   - Credit Score (300-850)
   - Employment Length (years)
   - Debt-to-Income Ratio
   - Existing Loans
   - Education Level
   - Marital Status
   - Home Ownership
4. Click **Assess Credit Risk**
5. View the risk assessment result with probability and recommendation

### API Usage

```bash
# Send a POST request to the assessment endpoint
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
**Random Forest Classifier** - An ensemble learning method that operates by constructing multiple decision trees at training time.

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

### `POST /assess`

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

### `GET /api/features`

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

### Project Setup for Development

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

This will:
1. Generate 10,000 synthetic customer profiles
2. Preprocess the data
3. Train the Random Forest classifier
4. Save the model and scaler to `models/` directory

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Dataset**: Synthetic data generated for demonstration purposes
- **ML Framework**: [scikit-learn](https://scikit-learn.org/)
- **Backend**: [Flask](https://flask.palletsprojects.com/)
- **Frontend**: [Bootstrap 5](https://getbootstrap.com/)
- **Icons**: [Font Awesome 6](https://fontawesome.com/)

---

## 📞 Contact

**Akshata Yadav** - [@akshata-yadav-20](https://github.com/akshata-yadav-20)

Project Link: [https://github.com/akshata-yadav-20/Credit-Risk-Assessment](https://github.com/akshata-yadav-20/Credit-Risk-Assessment)

Demo: [https://akshata-yadav-20.github.io/Credit-Risk-Assessment/](https://akshata-yadav-20.github.io/Credit-Risk-Assessment/)

---

### 🏦 Banking Domain Project
> **Problem Statement**: Financial institutions face challenges in identifying loan defaulters. Develop an AI model that predicts customer creditworthiness using financial and demographic data.

### 🔍 Solution Approach
This project implements an AI-powered credit risk assessment system using a Random Forest classifier to predict the likelihood of loan defaults. The model considers various financial indicators (credit score, income, debt-to-income ratio, etc.) to identify high-risk customers, enabling financial institutions to make data-driven lending decisions.