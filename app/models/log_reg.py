# imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from utils import get_best_correlators
from templates import TemplatesModel

# sets
PATH = "../Datasets/Modified/mod_UCI_Credit_Card.csv"
# df
df = pd.read_csv(PATH)
# correlation matrix
corr = df.corr()
# features
features = get_best_correlators(corr, "Default payment")


class Log_REgObject(TemplatesModel):
    def __init__(self, dataf: pd.DataFrame):
        TemplatesModel.__init__(self, dataf)
        self.df = dataf


if __name__ == "__main__":

    lin_reg = LinearRegression()

    # defining X and y
    X = df[features]
    y = df["Default payment"].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    # scores
    score = lin_reg.score(X_test, y_test)
    y_pred = lin_reg.predict(X_test)

    print("Model is accurate at {}%".format(round(score * 100, 3)))
