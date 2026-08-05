import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

# Set random seed for reproducibility
np.random.seed(42)

def generate_synthetic_data(n_samples=10000):
    """Generate synthetic credit risk data"""
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
    
    # Create target variable with realistic patterns
    # Higher credit score = lower risk
    # Higher loan amount = higher risk
    # Higher debt to income = higher risk
    default_prob = (
        -0.005 * df['credit_score'] +
        0.00003 * df['loan_amount'] +
        0.5 * df['debt_to_income'] -
        0.01 * df['employment_length'] +
        np.random.normal(0, 0.1, n_samples)
    )
    
    # Normalize to probability
    default_prob = 1 / (1 + np.exp(-(default_prob - 0.3) * 3))
    df['credit_risk'] = np.where(default_prob > 0.5, 1, 0)  # 1 = High Risk, 0 = Low Risk
    
    return df

def preprocess_data(df):
    """Preprocess data for training"""
    # Map categorical variables
    education_map = {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3}
    marital_map = {'Single': 0, 'Married': 1, 'Divorced': 2}
    home_map = {'Rent': 0, 'Own': 1, 'Mortgage': 2}
    
    df_processed = df.copy()
    df_processed['education'] = df_processed['education'].map(education_map)
    df_processed['marital_status'] = df_processed['marital_status'].map(marital_map)
    df_processed['home_ownership'] = df_processed['home_ownership'].map(home_map)
    
    return df_processed

def train_model():
    """Train the credit risk model"""
    print("Generating synthetic data...")
    df = generate_synthetic_data(10000)
    
    print("Preprocessing data...")
    df_processed = preprocess_data(df)
    
    # Separate features and target
    X = df_processed.drop('credit_risk', axis=1)
    y = df_processed['credit_risk']
    
    # Save original data for reference
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/credit_data.csv', index=False)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train Random Forest model
    print("Training model...")
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=50,
        min_samples_leaf=20,
        random_state=42,
        class_weight='balanced'
    )
    
    model.fit(X_train_scaled, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    
    print(f"\nModel Performance:")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"\nClassification Report:\n{classification_report(y_test, y_pred)}")
    print(f"\nConfusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    print(f"\nFeature Importance:\n{feature_importance}")
    
    # Save the model and scaler
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/credit_risk_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')
    
    print("\nModel saved to models/credit_risk_model.pkl")
    print("Scaler saved to models/scaler.pkl")
    
    return model, scaler, X.columns.tolist()

def predict_credit_risk(model, scaler, features):
    """Predict credit risk for new customer"""
    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0]
    
    risk_level = 'HIGH RISK' if prediction == 1 else 'LOW RISK'
    risk_probability = probability[1] if prediction == 1 else probability[0]
    
    return {
        'risk_level': risk_level,
        'probability': float(risk_probability),
        'recommendation': 'Approve Loan' if prediction == 0 else 'Review Required / Refer'
    }

if __name__ == '__main__':
    model, scaler, feature_names = train_model()
    print(f"\nFeature names: {feature_names}")