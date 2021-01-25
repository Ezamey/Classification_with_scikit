# challenge-classification

## What

A few first steps in the magical world of machine learning. This small exercice was about learning and understanding the basic implementation
of differents models using the powerful [sickit library](https://scikit-learn.org/stable/index.html) and of course the importance of data preprocessing,
data cleaning, and features engineering using [Pandas](https://pandas.pydata.org/)

## Why
- Start to being familiar with scikit. 
- See the difference between models and their possible applications.
- Understand the importance of tuning your model.
- Discover the limitations, pro and cons of some models.
- Being frustated :stuck_out_tongue_closed_eyes:
  
## How

Mostly with [Pandas](https://pandas.pydata.org/),[Sickit](https://scikit-learn.org/stable/index.html) and [Jupyter](https://jupyter.org/)

- EDA and data cleaning steps are in the [EDA notebook](app/Notebooks/EDA.ipynb)
- [Decision Tree](app/Notebooks/Decision_tree_.ipynb)
- [Knn](app/Notebooks/KNN_.ipynb)
- [Logistic Regression](app/Notebooks/Log_Reg_.ipynb)
- [Random Forest](app/Notebooks/Random_Forest__.ipynb)

### To use it :

__Requirements__ :

In the root folder, in a terminal :
```
pip install requirements.txt
```

In the [models](app/models) folder
```
py random_forest_m.py #if you want to see the Random Forest model
```
## Who
[Christian Melot](https://github.com/Ezamey) - Becode Trainee
## When
20/01/2021 to 23/01/2021

## TODO :

- Put this work into a flask app.
- Refine code so that the user can tune some parameters and have acces of the result of the differents models outside a console screen.
- Deploy it.