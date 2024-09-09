import pytest
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import sys
import os

print("Current Working Directory:", os.getcwd())
print("Python Path:", sys.path)

# Assuming your main code is in a file called health_prediction.py
from .disease_prediction import train_model, load_model, predict

# 5.1 Unit Testing

def test_data_loading():
    data = pd.read_csv('Training.csv')
    assert not data.empty, "Data should not be empty"
    assert 'prognosis' in data.columns, "Data should contain 'prognosis' column"

def test_model_training():
    data = pd.read_csv('Training.csv')
    X = data.drop('prognosis', axis=1)
    y = data['prognosis']
    try:
        trained_model = train_model(X, y)
        assert trained_model is not None, "Model training should return a non-None object"
    except Exception as e:
        assert False, f"Model training failed with an exception: {e}"
def test_model_loading():
    model, label_encoder, feature_names = load_model()
    assert model is not None, "Model should be loaded successfully"
    assert label_encoder is not None, "Label encoder should be loaded successfully"
    assert feature_names is not None, "Feature names should be loaded successfully"

def test_prediction():
    model, label_encoder, feature_names = load_model()
    test_data = pd.read_csv('Testing.csv')
    X_test = test_data.drop('prognosis', axis=1)
    predictions, probabilities = predict(model, label_encoder, feature_names, X_test)
    assert predictions is not None, "Predictions should not be None"
    assert probabilities is not None, "Probabilities should not be None"

# 5.2 Integration Testing

def test_end_to_end():
    # Train the model
    train_data = pd.read_csv('Training.csv')
    X_train = train_data.drop('prognosis', axis=1)
    y_train = train_data['prognosis']
    train_model(X_train, y_train)
    
    # Load the model
    model, label_encoder, feature_names = load_model()
    
    # Make predictions
    test_data = pd.read_csv('Testing.csv')
    X_test = test_data.drop('prognosis', axis=1)
    predictions, probabilities = predict(model, label_encoder, feature_names, X_test)
    
    assert predictions is not None, "End-to-end test should produce non-None predictions"

# 5.3 Validation Methodology

def test_cross_validation():
    data = pd.read_csv('Training.csv')
    X = data.drop('prognosis', axis=1)
    y = data['prognosis']
    
    # Create a pipeline that includes preprocessing and the SVM classifier
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('svm', SVC(kernel='rbf', probability=True))
    ])
    
    # Perform 5-fold cross-validation
    scores = cross_val_score(pipeline, X, y, cv=5, scoring='accuracy')
    
    print(f"Cross-validation scores: {scores}")
    print(f"Mean accuracy: {np.mean(scores):.2f} (+/- {np.std(scores) * 2:.2f})")
    
    assert np.mean(scores) > 0.7, "Mean cross-validation accuracy should be above 0.7"

def test_performance_metrics():
    data = pd.read_csv('Training.csv')
    X = data.drop('prognosis', axis=1)
    y = data['prognosis']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Print classification report
    print(classification_report(y_test, y_pred))
    
    # Print confusion matrix
    print(confusion_matrix(y_test, y_pred))
    
    # You can add specific assertions here based on your performance goals
    assert classification_report(y_test, y_pred) is not None, "Classification report should be generated"

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])