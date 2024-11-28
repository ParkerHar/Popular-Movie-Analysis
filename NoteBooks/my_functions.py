import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

def linear_model(df,dependant,features):
    y = dependant
    X = features
    X = sm.add_constant(X) 

    model = sm.OLS(y, X) 
    results = model.fit()
    print(results.summary())
