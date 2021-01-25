import pandas as pd


def get_best_correlators(
    dataframe_corr: pd.DataFrame,
    to_cor: str = "Default payment",
    n2: int = 1,
    n3: int = 0,
):
    """Function to find the best correlations possible

    Args:
        dataframe_corr (pd.DataFrame): a pd.corr() object.
        to_cor (str): the column name you want the correlations with.

    Returns:
        [type]: a list of correlators based on the passed arguments
    """
    correlators_list = []
    for k, v in dataframe_corr[to_cor].items():
        n = str(abs(v))
        if int(n[2]) >= n2 and int(n[3]) >= 0:
            correlators_list.append(k)

    return correlators_list
