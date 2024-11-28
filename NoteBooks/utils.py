{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def linear_model(df,dependant,features):\n",
    "    y = df[dependant]\n",
    "    X = df[features]\n",
    "    X = sm.add_constant(X)\n",
    "\n",
    "    model = sm.OLS(y, X) \n",
    "    results = model.fit()\n",
    "    print(results.summary())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def linear_model_scaled(df,dependant,features):\n",
    "    y = df[dependant]\n",
    "    X = df[features]\n",
    "    scaler = StandardScaler()\n",
    "    X_scaled = scaler.fit_transform(X) \n",
    "    X_scaled = sm.add_constant(X_scaled)\n",
    "\n",
    "    model = sm.OLS(y, X_scaled) \n",
    "    results = model.fit()\n",
    "    print(results.summary())"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "first_env",
   "language": "python",
   "name": "first_env"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
