"""
This module is responsible for training the ML model.
"""
import os
import sys
from dataclasses import dataclass

from sklearn.metrics import r2_score

from src.config.configurations import Configuration
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")
    trained_processor_file_path = os.path.join("artifacts", "preprocessor.pkl")


class ModelTrainer:
    def __init__(self, configuration: Configuration):
        self.model_trainer_config = ModelTrainerConfig()
        self.configuration = configuration
        self.best_model_name = None
        self.best_model_accuracy_score = None

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info("Split training and testing data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
                )

            models = self.configuration.models
            params = self.configuration.params

            # Evaluate all candidates models on the data
            # Find the one with the best accuracy score
            model_report = evaluate_models(X_train, X_test, y_train, y_test, models, params)
            best_model_score = max(sorted(model_report.values()))

            # Fetch the best model chosen
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            self.best_model_name = best_model_name
            best_model = models[best_model_name]

            if best_model_score < self.configuration.model_score_threshold:
                raise CustomException("No best model found", sys)

            logging.info("We found a great model !")

            # if a good model is found, save it to the artifacts
            save_object(
                    self.model_trainer_config.trained_model_file_path,
                    best_model
                    )

            # Save the best model's accuracy score
            predicted = best_model.predict(X_test)
            self.best_model_accuracy_score = r2_score(y_test, predicted)

        except Exception as e:
            raise CustomException(e, sys)

    def get_best_model_accuracy(self):
        """Return the best accuracy score found"""
        print(f"The best model is {self.best_model_name}"
              f" and it has an accuracy of {self.best_model_accuracy_score}"
              )
