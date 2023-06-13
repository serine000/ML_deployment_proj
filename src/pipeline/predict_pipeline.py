import sys
from dataclasses import dataclass

import pandas as pd

from src.exception import CustomException
from src.utils import load_object


@dataclass
class PredictPipelineConfig:
    model_path = "artifacts/model.pkl"
    preprocessor_path = 'artifacts/preprocessor.pkl'


@dataclass
class CustomDataObject:
    gender = None
    race_ethnicity = None
    parental_level_of_education = None
    lunch = None
    test_preparation_course = None
    reading_score = None
    writing_score = None


class PredictPipeline:
    def __init__(self, custom_data: CustomDataObject):
        self.prediction_config = PredictPipelineConfig()
        self.custom_data = custom_data

    def prepare_prediction_data(self):
        try:
            custom_data_input_dict = {
                "gender": [self.custom_data.gender],
                "race_ethnicity": [self.custom_data.race_ethnicity],
                "parental_level_of_education": [self.custom_data.parental_level_of_education],
                "lunch": [self.custom_data.lunch],
                "test_preparation_course": [self.custom_data.test_preparation_course],
                "reading_score": [self.custom_data.reading_score],
                "writing_score": [self.custom_data.writing_score],
                }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        """Run the predictions on the input features"""

        try:
            print("Starting prediction")
            model = load_object(self.prediction_config.model_path)
            preprocessor = load_object(self.prediction_config.preprocessor_path)

            print("preprocessing data")
            data_scaled = preprocessor.transform(features)

            print("running prediction")
            model_prediction = model.predict(data_scaled)
            return model_prediction

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(
            self,
            gender: str,
            race_ethnicity: str,
            parental_level_of_education,
            lunch: str,
            test_preparation_course: str,
            reading_score: int,
            writing_score: int
            ):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
