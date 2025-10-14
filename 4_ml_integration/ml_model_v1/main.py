import pickle
import joblib 
import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Read the data 
df = pd.read_csv("housing.csv")[:,:-1].dropna()

x = df.drop(columns='median_house_value')
y = df.median_house_value.copy()

print(x.shape, y.shape)