import joblib
import numpy as np

with open("autompg/model/autompg.pkl", "rb") as file:
    model = joblib.load(file)

data = [4,97,92,2288,17,72,3]
data = np.array(data).reshape(-1, 7)
result = model.predict(data)[0]
print(result)