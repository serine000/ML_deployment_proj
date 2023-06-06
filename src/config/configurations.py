"""
This module contains general configurations used throughout the code
"""
from dataclasses import dataclass

@dataclass
class Configruation():
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
