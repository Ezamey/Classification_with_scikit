import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

from templates import TemplatesModel
from utils import get_best_correlators

#sets
PATH = "../Datasets/Modified/mod_UCI_Credit_Card.csv"
#df
df = pd.read_csv(PATH)
#correlation matrix
corr = df.corr()
#features
features = get_best_correlators(corr,"Default payment")


class RandomForestObject(TemplatesModel):
    def __init__(self,dataf:pd.DataFrame):
        TemplatesModel.__init__(self,dataf)
        self.df = dataf

    @classmethod
    def pick_n(self,X_train, y_train,X_test, y_test,n_:int=10):
        """#choose the best number for x up to 10 estimators

        Returns:
            [int]: best number of n for RandomForestClassifier
        """
        train_score = []
        test_score = []
        k_vals = []

        for k in range(1, n_):
            k_vals.append(k)
            rfc = RandomForestClassifier(n_estimators = n_)
            rfc.fit(X_train, y_train)

            tr_score = rfc.score(X_train, y_train)
            train_score.append(tr_score)

            te_score = rfc.score(X_test, y_test)
            test_score.append(te_score)

        max_test_score = max(test_score)
        max_test_scores_ind = [i for i, v in enumerate(test_score) if v == max_test_score]
        print('Max test score {} and k = {}'.format(max_test_score * 100, list(map(lambda x: x + 1, max_test_scores_ind))))
        opt_n = list(map(lambda x: x + 1, max_test_scores_ind))[0]   
        return opt_n

if __name__ == "__main__":
    rfcobject = RandomForestObject(df)
    X,y = rfcobject.set_up_x_and_y(features=features)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    n_number = rfcobject.pick_n(X_train,y_train,X_test, y_test,n_=5)

    rfc = RandomForestClassifier(n_estimators=n_number)
    rfc.fit(X_train, y_train)

    #scores
    score = rfc.score(X_test, y_test)
    y_pred = rfc.predict(X_test)

    print(classification_report(y_test, y_pred))
    print("Model is accurate at {}%".format(round(score*100,3)))