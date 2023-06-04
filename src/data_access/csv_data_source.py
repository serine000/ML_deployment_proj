"""
This module is in charge of implementing the data extraction from a CSV file.
"""
import os.path
import pandas as pd
from src.data_access.data_source import DataSource

class CSVDataSource(DataSource):
    """This class includes the methods to read/extract data from a saved CSV file."""
    def read_data(self, file_path):
        """Extract and reads the data from a CSV file"""
        if self.check_file_exists(file_path):
            pass
        else:
            raise Exception("The CSV file you are referencing is not found.")
       

    def transform_to_pandas_dataframe(self, data) -> pd.DataFrame:
        """Transform the data from the CSV file it into a pandas dataframe."""
        pass
    
    def check_file_exists(self, file_name):
        """Check if CSV file exists in the data directory"""
        
        return os.path.exists(file_name)
