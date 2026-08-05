# Credit Risk Assessment System

> **AI-Powered Credit Risk Assessment for Financial Institutions**

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-red?logo=flask)](https://flask.palletsprojects.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## Overview

Financial institutions face significant challenges in identifying potential loan defaulters. The **Credit Risk Assessment System** leverages machine learning to predict customer creditworthiness using financial and demographic data.

### Key Features
- **AI-Powered**: Random Forest classifier trained on 10,000+ synthetic samples
- **Real-time**: Instant risk assessment in milliseconds
- **Secure**: Privacy-focused - no sensitive data stored
- **Modern UI**: Dark-themed, responsive interface
- **Multiple Deployment Options**: Flask server or static demo

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/akshata-yadav-20/Credit-Risk-Assessment.git
cd Credit-Risk-Assessment

# Install dependencies
pip install -r requirements.txt

# Train the model
python ml/train_model.py

# Start the server
python run.py

# Open http://localhost:5000
```

---

## Files

| File | Description |
|------|-------------|
| `app/__init__.py` | Flask backend with API endpoints |
| `app/templates/index.html` | Main UI (Flask-enabled) |
| `app/templates/index_static.html` | Standalone demo (works without backend) |
| `ml/__init__.py` | ML model loading |
| `ml/train_model.py` | Model training script |
| `run.py` | Entry point |
| `requirements.txt` | Python dependencies |
| `README.md` | Documentation |
| `LICENSE` | MIT License |
| `.github/workflows/pages.yml` | CI/CD for GitHub Pages |

---

## Model Details

**Algorithm**: Random Forest Classifier  
**Training Samples**: 10,000 synthetic customer profiles  
**Accuracy**: ~95%  
**Features**: 10 input features (demographic and financial)

### Input Features
| Feature | Description | Range |
|---------|-------------|-------|
| age | Customer age | 18-75 |
| income | Annual income ($) | $0+ |
| loan_amount | Requested loan ($) | $0+ |
| credit_score | Credit score | 300-850 |
| employment_length | Years employed | 0-30+ |
| debt_to_income | Debt-to-income ratio | 0.1-0.8 |
| existing_loans | Number of existing loans | 0-5 |
| education | Education (0=HS, 1=Bach, 2=Mast, 3=PhD) | 0-3 |
| marital_status | Status (0=Single, 1=Married, 2=Div) | 0-2 |
| home_ownership | Home (0=Rent, 1=Own, 2=Mortgage) | 0-2 |

---

## Demo

### Option 1: Local Demo (No Installation Required)
Simply open `app/templates/index_static.html` in any modern browser to run the standalone demo.

### Option 2: Full Flask App
Start the Flask server and visit `http://localhost:5000` for full API integration.

### Option 3: GitHub Pages
The project includes GitHub Actions workflow for automatic deployment to GitHub Pages. To enable:
1. Go to repo Settings → Pages
2. Select source: `main` branch, `/ (root)` folder
3. Click "Save"

---

## API Usage

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

---

## License
MIT License - see [LICENSE](LICENSE) file for details.

---

## Contact
**Akshata Yadav** - [@akshata-yadav-20](https://github.com/akshata-yadav-20)  
Project: [github.com/akshata-yadav-20/Credit-Risk-Assessment](https://github.com/akshata-yadav-20/Credit-Risk-Assessment)