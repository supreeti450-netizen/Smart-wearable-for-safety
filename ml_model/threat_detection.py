import joblib

model = joblib.load("threat_model.pkl")

def detect_threat(hr, accel):
    prediction = model.predict([[hr, accel]])
    return prediction[0]

print(detect_threat(120, 3.1))
