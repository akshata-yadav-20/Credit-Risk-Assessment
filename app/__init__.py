from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the model and scaler
model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'credit_risk_model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'scaler.pkl')

# Initialize model (will be created if not exists)
from ml import model, scaler, FEATURE_NAMES

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assess', methods=['POST'])
def assess_credit_risk():
    try:
        data = request.get_json()
        
        # Prepare features
        features = [
            int(data['age']),
            float(data['income']),
            float(data['loan_amount']),
            int(data['credit_score']),
            int(data['employment_length']),
            float(data['debt_to_income']),
            int(data['existing_loans']),
            int(data['education']),
            int(data['marital_status']),
            int(data['home_ownership'])
        ]
        
        # Scale features
        features_scaled = scaler.transform([features])
        
        # Predict
        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0]
        
        risk_level = 'HIGH RISK' if prediction == 1 else 'LOW RISK'
        risk_probability = float(probability[1] if prediction == 1 else probability[0])
        confidence = float(max(probability))
        recommendation = 'Approve Loan' if prediction == 0 else 'Review Required - Refer to Senior Officer'
        
        return jsonify({
            'success': True,
            'risk_level': risk_level,
            'probability': round(risk_probability * 100, 2),
            'confidence': round(confidence * 100, 2),
            'recommendation': recommendation,
            'prediction_class': int(prediction)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/api/features')
def get_features():
    return jsonify({
        'features': FEATURE_NAMES,
        'feature_details': {
            'age': 'Customer age',
            'income': 'Annual income ($)',
            'loan_amount': 'Requested loan amount ($)',
            'credit_score': 'Credit score (300-850)',
            'employment_length': 'Years of employment',
            'debt_to_income': 'Debt-to-income ratio',
            'existing_loans': 'Number of existing loans',
            'education': 'Education level (0=High School, 1=Bachelor, 2=Master, 3=PhD)',
            'marital_status': 'Marital status (0=Single, 1=Married, 2=Divorced)',
            'home_ownership': 'Home ownership (0=Rent, 1=Own, 2=Mortgage)'
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)