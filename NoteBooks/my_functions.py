import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

def linear_model(df,dependant,features):
    y = df[dependant]
    X = df[features]
    X = sm.add_constant(X) 

    model = sm.OLS(y, X) 
    results = model.fit()
    print(results.summary())
