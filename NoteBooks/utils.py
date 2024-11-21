import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

#unscaled linear model
def linear_model(df,dependant,features):
    y = df[dependant]
    X = df[features]
    X = sm.add_constant(X)

    model = sm.OLS(y, X) 
    results = model.fit()
    print(results.summary())


#scaled linear model
def linear_model_scaled(df,dependant,features):
    y = df[dependant]
    X = df[features]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X) 
    X_scaled = sm.add_constant(X_scaled)

    model = sm.OLS(y, X_scaled) 
    results = model.fit()
    print(results.summary())