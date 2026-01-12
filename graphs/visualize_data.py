import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("../data/sample_sensor_data.csv")

plt.hist(data['heart_rate'], bins=5)
plt.title("Heart Rate Distribution")
plt.xlabel("Heart Rate")
plt.ylabel("Frequency")
plt.show()
