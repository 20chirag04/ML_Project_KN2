import sys
from src.components.data_ingestion import DataIngestion
from src.exception import NetworkSecurityException
from src.logger import logging
from src.entity.config_entity import (DataIngestionConfig,
                                        TrainingPipelineConfig,
                                        DataValidationConfig,
                                        DataTransformationConfig)
from src.components.data_tranformation import DataTransformation
from src.components.data_validation import  DataValidation

from src.components.model_trainer import ModelTrainer
from src.entity.config_entity import ModelTrainerConfig


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

        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info("Data Transformation Started")
        data_transformation = DataTransformation(data_validation_artifact,data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Completed")

        logging.info("Model Training started")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")

    except Exception as e:
        raise NetworkSecurityException(e,sys)