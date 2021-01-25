# imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier

from templates import TemplatesModel

# sets
PATH = "../Datasets/Modified/mod_UCI_Credit_Card.csv"
# df
df = pd.read_csv(PATH)


class Log_REgObject(TemplatesModel):
    def __init__(self, dataf: pd.DataFrame):
        TemplatesModel.__init__(self, dataf)
        self.df = dataf


if __name__ == "__main__":

    dtc = DecisionTreeClassifier()

    # defining X and y
    X = df.drop("Default payment", axis=1)
    y = df["Default payment"].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Creating instance of the classifier
    dtc = DecisionTreeClassifier()
    dtc.fit(X_train, y_train)
    # scores
    score = dtc.score(X_test, y_test)
    y_pred = dtc.predict(X_test)

    print(classification_report(y_test, y_pred))

    print("Model is accurate at {}%".format(round(score * 100, 3)))
