import statsmodels.api as sm

def linear_model(df,dependant,features):
    """
    Fits a linear regression model.
    Args:
        df (DataFrame): The dataset.
        dependent (str): The dependent variable name.
        features (list): A list of feature column names.
    Returns:
        OLS regression results.
    """
    y = df[dependant]
    X = df[features]
    X = sm.add_constant(X) 

    model = sm.OLS(y, X).fit()
    return model
