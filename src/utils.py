import pandas as pd 
import numpy as np
import dill
from src.exception import CustomException
import os
import sys

def save_object(destination_save_path, object_to_save):
    try:
        dir_path = os.path.dirname(destination_save_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(destination_save_path, "wb") as file_obj:
            dill.dump(object_to_save, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
