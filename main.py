import sys
from src.components.data_ingestion import DataIngestion
from src.exception import NetworkSecurityException
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig,TrainingPipelineConfig


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiate the data ingestion")

        dataingestionartifact =data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)