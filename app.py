from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformation
import sys


if __name__=="__main__":
    logging.info("the execurion has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transformation_config=DataTransformstionConfig()
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path,test_data_path)


    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)