import joblib
import numpy as np

with open("autompg/model/autompg.pkl", "rb") as file:
    model = joblib.load(file)

data = [4,71,65,1836,21,74,3]
data = np.array(data).reshape(-1, 7)
print(data)
result = model.predict(data)
print(result)