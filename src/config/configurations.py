"""
This module contains general configurations used throughout the code
"""
from dataclasses import dataclass

from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor


@dataclass
class Configuration:
    """Configuration dataclass with just the data"""
    numerical_columns = ["writing_score", "reading_score"]
    categorical_columns = [
        "gender",
        "race_ethnicity",
        "parental_level_of_education",
        "lunch",
        "test_preparation_course",
        ]
    target_column = "math_score"
    models = {
        "Random Forest": RandomForestRegressor(),
        "Decision Tree": DecisionTreeRegressor(),
        "Gradient Boosting": GradientBoostingRegressor(),
        "Linear Regression": LinearRegression(),
        "XGBRegressor": XGBRegressor(),
        "AdaBoost Regressor": AdaBoostRegressor(),
        }
    params = {
        "Decision Tree": {
            'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
            # 'splitter':['best','random'],
            # 'max_features':['sqrt','log2'],
            },
        "Random Forest": {
            # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],

            # 'max_features':['sqrt','log2',None],
            'n_estimators': [8, 16, 32, 64, 128, 256]
            },
        "Gradient Boosting": {
            # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
            'learning_rate': [.1, .01, .05, .001],
            'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
            # 'criterion':['squared_error', 'friedman_mse'],
            # 'max_features':['auto','sqrt','log2'],
            'n_estimators': [8, 16, 32, 64, 128, 256]
            },
        "Linear Regression": {},
        "XGBRegressor": {
            'learning_rate': [.1, .01, .05, .001],
            'n_estimators': [8, 16, 32, 64, 128, 256]
            },

        "AdaBoost Regressor": {
            'learning_rate': [.1, .01, 0.5, .001],
            # 'loss':['linear','square','exponential'],
            'n_estimators': [8, 16, 32, 64, 128, 256]
            }
        }
    model_score_threshold = 0.75
    csv_data_source_path = 'notebooks/data/StudentsPerformance.csv'
