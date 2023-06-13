from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.data_access.data_access_factory import CSVDataSourceFactory
from src.data_access.data_source import DataSource

if __name__ == "__main__":
    data_source = CSVDataSourceFactory.create_data_source_component()
    data_ingestion = DataIngestion(data_source)
    train_data, test_data = data_ingestion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))
