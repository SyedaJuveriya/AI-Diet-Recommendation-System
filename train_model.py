import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Sample training dataset (simulated health data)
data = {
    "weight":  [45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
    "height":  [150,155,160,165,170,172,175,178,180,182],
    "age":     [18, 22, 25, 28, 30, 32, 35, 38, 40, 42],
    "gender":  [0,1,0,1,1,0,1,1,0,1],   # 0 = Female, 1 = Male
    "activity":[1.2,1.375,1.55,1.725,1.9,1.2,1.375,1.55,1.725,1.9],
    "calories":[1700,2100,2000,2400,2600,1900,2300,2500,2200,2800]
}

df = pd.DataFrame(data)

X = df[["weight","height","age","gender","activity"]]
y = df["calories"]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("diet_model.pkl", "wb"))

print("Model trained and saved as diet_model.pkl")
