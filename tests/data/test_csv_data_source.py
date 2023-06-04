import pytest
from src.data_access.csv_data_source import CSVDataSource

class TestCSVDataSource:
    
    def setup_method(self):
        self.csv_data_source = CSVDataSource()
    
    def test_file_exists_check(self):
        file_not_found = self.csv_data_source.check_file_exists("something.txt")
        assert file_not_found == False
        
    def test_file_does_not_exists_check(self):
        file_found = self.csv_data_source.check_file_exists("requirements.txt")
        assert file_found == True