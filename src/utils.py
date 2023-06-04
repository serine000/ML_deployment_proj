"""
This module is responsible for grouping utility functions used throught the project.
"""
import os
import sys
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(destination_save_path, object_to_save):
    """
    Save the object_to_save into the destination_save_path as a pickled object.
    """
    try:
        dir_path = os.path.dirname(destination_save_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(destination_save_path, "wb") as file_obj:
            dill.dump(object_to_save, file_obj)

    except Exception as error_pickling_object:
        raise CustomException(error_pickling_object, sys)

def evaluate_models(train_features, test_features, train_labels, test_labels, models, params) -> dict():
    """Function that evaluates a model given its parameters and training data."""
    
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=params[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv=3)
            gs.fit(train_features, train_labels)

            model.set_params(**gs.best_params_)
            model.fit(train_features, train_labels)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(train_features)
            y_test_pred = model.predict(test_features)

            train_model_score = r2_score(train_labels, y_train_pred)
            test_model_score = r2_score(test_labels, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)