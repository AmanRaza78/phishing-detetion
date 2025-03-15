import joblib
import numpy as np

# loding the trained model.
model = joblib.load("backend/phishing_model.pkl")

# this function take a url and predict phishing 
def predict_phishing(features):
    input_data = np.array(features).reshape(1, -1)
    return model.predict(input_data)[0]
