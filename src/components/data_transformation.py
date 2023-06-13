"""
This module is in charge of handling the data processing of the data 
and generate a processing pickle object.
"""
import os
import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.config.configurations import Configuration

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, read_csv_artifacts


@dataclass
class DataTransformationConfig():
    """Configurations for data transformation"""
    preprocessor_obj_path = os.path.join('artifacts', "preprocessor.pkl")


class DataTransformation():
    """Data transformation class"""

    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        self.configuration = Configuration()

    def create_data_processor(self):
        """This functions applies data processing on numerical and categorical data"""

        try:
            numerical_columns = self.configuration.numerical_columns
            categorical_columns = self.configuration.categorical_columns

            num_pipeline = Pipeline(
                    steps = [
                        ("imputer", SimpleImputer(strategy = "median")),
                        ("scaler", StandardScaler(with_mean = False))
                        ]
                    )
            cat_pipeline = Pipeline(
                    steps = [
                        ("imputer", SimpleImputer(strategy = "most_frequent")),
                        ("ome_hot_encoding", OneHotEncoder()),
                        ("scaler", StandardScaler(with_mean = False))
                        ]
                    )
            logging.info("Categorical & numerical columns encoding completed")

            preprocessor = ColumnTransformer(
                    [
                        ("num_pipeline", num_pipeline, numerical_columns),
                        ("cat_pipeline", cat_pipeline, categorical_columns)
                        ]
                    )

            logging.info("Saved preprocessing object.")
            save_object(
                    destination_save_path = self.data_transformation_config.preprocessor_obj_path,
                    object_to_save = preprocessor
                    )

            return preprocessor

        except Exception as error_data_processor_initiation:
            raise CustomException(error_data_processor_initiation, sys)

    def initiate_data_transformation(self, train_path, test_path):
        """Apply the data transformation on the train and test splits"""

        try:
            train_df = read_csv_artifacts(train_path)
            test_df = read_csv_artifacts(test_path)

            logging.info("Read train and test data completed")

            preprocessor_object = self.create_data_processor()
            logging.info("Obtaining preprocessing object")

            target_column_name = self.configuration.target_column

            # Prepare training features & target columns
            input_feature_train_df = train_df.drop([target_column_name], axis = 1)
            target_feature_train_df = train_df[target_column_name]

            # Prepare testing features & target columns
            input_feature_test_df = test_df.drop(columns = [target_column_name], axis = 1)
            target_feature_test_df = test_df[target_column_name]

            logging.info(
                    "Applying preprocessing object on training dataframe and testing dataframe."
                    )

            # preprocess the training and testing features
            processed_training_features = preprocessor_object.fit_transform(input_feature_train_df)
            processed_testing_features = preprocessor_object.transform(input_feature_test_df)

            train_data_array = np.c_[
                processed_training_features, np.array(target_feature_train_df)
            ]
            test_data_array = np.c_[processed_testing_features, np.array(target_feature_test_df)]

            return (
                train_data_array,
                test_data_array,
                self.data_transformation_config.preprocessor_obj_path
                )

        except Exception as error_initiating_data_transformation:
            raise CustomException(error_initiating_data_transformation, sys)
