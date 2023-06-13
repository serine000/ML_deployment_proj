"""
This module is responsible for reading data from a source and saving it into artifacts.
"""
import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_access.data_source import DataSource
from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "raw_data.csv")


class DataIngestion:
    def __init__(self, data_source: DataSource):
        self.ingestion_config = DataIngestionConfig()
        self.data_source = data_source

    def save_data_artifacts(self, data, data_path, create_dir_flag: bool) -> None:
        """Saves data as CSV artifacts"""

        if create_dir_flag:
            # Ensure there is a directory to store the artifacts.
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok = True)

        # Save the input raw data in a csv file in the artifact folder.
        data.to_csv(
                data_path,
                index = False,
                header = True
                )

    def initiate_data_ingestion(self):
        """Extract the data from the dataset source
        and ingest/save them as artifacts for later use."""

        logging.info("Entered the data ingestion method")
        try:
            # Fetch data to be ingested in a dataframe form
            input_dataframe = self.data_source.fetch_input_data(
                    'notebook/data/StudentsPerformance.csv'
                    )
            logging.info("Read the dataset as a Pandas dataframe")

            # Save raw input data fetched.
            self.save_data_artifacts(input_dataframe, self.ingestion_config.raw_data_path, True)

            logging.info("Train test split is initiated")
            train_set, test_set = train_test_split(
                    input_dataframe,
                    test_size = 0.2,
                    random_state = 42
                    )

            # Save the train-test split of the input data.
            self.save_data_artifacts(train_set, self.ingestion_config.train_data_path, False)
            self.save_data_artifacts(test_set, self.ingestion_config.test_data_path, False)
            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )

        except Exception as e:
            raise CustomException(e, sys)
