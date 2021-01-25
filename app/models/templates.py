import pandas as pd


class TemplatesModel:
    def __init__(self, dataf: pd.DataFrame):
        self.df = dataf

    @classmethod
    def pick_n(self, X_train, y_train, X_test, y_test, n_: int):
        """#choose the best number for x up to 20 nearest neighbors

        Returns:
            [int]: best number of n for knn
        """
        train_score = []
        test_score = []
        k_vals = []

        for k in range(1, n_):
            k_vals.append(k)
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train, y_train)

            tr_score = knn.score(X_train, y_train)
            train_score.append(tr_score)

            te_score = knn.score(X_test, y_test)
            test_score.append(te_score)

        max_test_score = max(test_score)
        max_test_scores_ind = [
            i for i, v in enumerate(test_score) if v == max_test_score
        ]
        print(
            "Max test score {} and k = {}".format(
                max_test_score * 100, list(map(lambda x: x + 1, max_test_scores_ind))
            )
        )
        opt_n = list(map(lambda x: x + 1, max_test_scores_ind))[0]
        return opt_n

    def set_up_x_and_y(self, features: list):
        """Choosing features and target

        return a tuple(X,y)
        """
        y = self.df["Default payment"].values
        X = self.df[features]

        return (X, y)
