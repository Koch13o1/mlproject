import os
import sys

import numpy as np
import pandas as pd

import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for model_name, model in models.items():
            param = params[model_name]
            
            if 'Cat' in model_name:
                gs = GridSearchCV(model, param, cv=3, verbose=0)
                gs.fit(X_train, y_train, verbose=0)
                # model.fit(X_train, y_train, verbose=0)  # Train Model
            else:
                gs = GridSearchCV(model, param, cv=3)
                gs.fit(X_train, y_train)
                # model.fit(X_train, y_train)  # Train Model
            
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)


            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report
    except Exception as e:
        raise CustomException(e, sys)
