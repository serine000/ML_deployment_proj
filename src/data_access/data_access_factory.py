from abc import ABC, abstractmethod

from src.data_access.csv_data_source import CSVDataSource
from src.data_access.data_source import DataSource


class DataAccessFactory(ABC):

    @staticmethod
    @abstractmethod
    def create_data_source_component() -> DataSource:
        pass


class CSVDataSourceFactory(DataAccessFactory):
    @staticmethod
    def create_data_source_component() -> DataSource:
        return CSVDataSource()
