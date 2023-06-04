"""
This module is responsible for grouping utility functions used throught the project.
"""
import os
import sys
import dill
from src.exception import CustomException


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
