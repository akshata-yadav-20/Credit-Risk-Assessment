import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Generate dataset on first import
data_path = 'data/credit_data.csv'
model_path = 'models/credit_risk_model.pkl'
scaler_path = 'models/scaler.pkl'

if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    np.random.seed(42)
    
    # Generate synthetic data
    n_samples = 10000
    data = {
        'age': np.random.randint(18, 75, n_samples),
        'income': np.random.normal(50000, 15000, n_samples).astype(int),
        'loan_amount': np.random.normal(15000, 8000, n_samples).astype(int),
        'credit_score': np.random.randint(300, 850, n_samples),
        'employment_length': np.random.randint(0, 30, n_samples),
        'debt_to_income': np.random.uniform(0.1, 0.8, n_samples),
        'existing_loans': np.random.randint(0, 5, n_samples),
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_samples),
        'marital_status': np.random.choice(['Single', 'Married', 'Divorced'], n_samples),
        'home_ownership': np.random.choice(['Rent', 'Own', 'Mortgage'], n_samples)
    }
    df = pd.DataFrame(data)
    education_map = {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}
    marital_map = {'Single': 0, 'Married': 1, 'Divorced': 2}
    home_map = {'Rent': 0, 'Own': 1, 'Mortgage': 2}
    df['education'] = df['education'].map(education_map)
    df['marital_status'] = df['marital_status'].map(marital_map)
    df['home_ownership'] = df['home_ownership'].map(home_map)
    default_prob = -0.005 * df['credit_score'] + 0.00003 * df['loan_amount'] + 0.5 * df['debt_to_income'] - 0.01 * df['employment_length'] + np.random.normal(0, 0.1, n_samples)
    default_prob = 1 / (1 + np.exp(-(default_prob - 0.3) * 3))
    df['credit_risk'] = np.where(default_prob > 0.5, 1, 0)
    
    X = df.drop('credit_risk', axis=1)
    y = df['credit_risk']
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
    model.fit(X_scaled, y)
    
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

# Load model and scaler
model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

FEATURE_NAMES = ['age', 'income', 'loan_amount', 'credit_score', 'employment_length', 
                 'debt_to_income', 'existing_loans', 'education', 'marital_status', 'home_ownership']