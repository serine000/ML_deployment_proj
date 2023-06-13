from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.config.configurations import Configuration
from src.data_access.data_access_factory import CSVDataSourceFactory

if __name__ == "__main__":
    # initializing objects
    data_source = CSVDataSourceFactory.create_data_source_component()
    configuration = Configuration()

    # Start data ingestion
    data_ingestion = DataIngestion(data_source, configuration)
    train_data, test_data = data_ingestion.initiate_data_ingestion()

    # Start data transformation
    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    # Find best model on transformed data
    model_trainer = ModelTrainer(configuration)
    model_trainer.initiate_model_training(train_arr, test_arr)
    model_trainer.get_best_model_accuracy()
