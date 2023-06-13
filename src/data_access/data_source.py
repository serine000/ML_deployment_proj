"""
This module is an interface used to implement different types of data sources 
to be used by the application to extract data.
"""
from abc import abstractmethod, ABC


class DataSource(ABC):
    """Blueprint for a data source object"""

    @abstractmethod
    def fetch_input_data(self, *args):
        """Extract and reads the data from the source"""
        pass
