"""
This module is an interface used to implement different types of data sources 
to be used by the application to extract data.
"""
import pandas as pd
from abc import abstractmethod, ABC

class DataSource(ABC):
    """Blueprint for a data source object"""
    @abstractmethod
    def read_data():
        """Extract and reads the data from the source"""
        pass

    @abstractmethod
    def transform_to_pandas_dataframe(data) -> pd.DataFrame:
        """Takes extracted data and transforms it into a pandas dataframe."""
        pass
    