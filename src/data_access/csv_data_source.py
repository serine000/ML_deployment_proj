"""
This module is in charge of implementing the data extraction from a CSV file.
"""
import pandas as pd

from src.data_access.data_source import DataSource
from src.utils import check_file_exists


class CSVDataSource(DataSource):
    """This class includes the methods to read/extract data from a saved CSV file."""

    def fetch_input_data(self, file_path) -> pd.DataFrame:
        """Extract and reads the data from a CSV file"""
        if check_file_exists(file_path):
            dataframe = pd.read_csv(file_path)
            return dataframe
        else:
            raise Exception("The CSV file you are referencing is not found.")
