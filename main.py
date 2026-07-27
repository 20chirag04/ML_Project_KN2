import sys
from src.components.data_ingestion import DataIngestion
from src.exception import NetworkSecurityException
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig,DataValidationConfig
from src.components.data_validation import  DataValidation


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")
        dataingestionartifact =data_ingestion.initiate_data_ingestion()
        logging.info("data Initiation COmpleted")
        print(dataingestionartifact)

        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("data_validation_completed")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)