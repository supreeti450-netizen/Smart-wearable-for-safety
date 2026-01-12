import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

data = pd.read_csv("../data/sample_sensor_data.csv")

X = data[['heart_rate', 'acceleration']]
y = data['label']

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "threat_model.pkl")
print("Model trained and saved")
