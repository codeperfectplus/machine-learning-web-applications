import joblib
with open("server/model/classifier.pkl", 'rb') as file:
    model = joblib.load(file)

import numpy as np
arr= np.array([2,3,2,1]).reshape(-1,4)
print(arr.shape)
print(model.predict(arr))