import pandas as pd
import numpy as np
from src.Diamond_price_prediction.logger import logging
from src.Diamond_price_prediction.exception import CustomException
import os 
import sys

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path


class DataIngestionConfig:
    raw_data:str = os.path.join('artifacts','raw_data.csv')
    train_data:str = os.path.join('artifacts','train_data.csv')
    test_data:str = os.path.join('artifacts','test_data.csv')


class DataIntegration:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_integration(self):
        logging.info("data ingestion started")

        try:
            data = pd.read_csv(Path(os.path.join('notebooks/data','gemstone.csv')))
            logging.info('I have read dataset as a df')

            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data)),exist_ok = True)
            data.to_csv(self.ingestion_config.raw_data,index = False)
            logging.info('I have saved the raw dataset in artifact folder')

            logging.info("Here i have performed train test splits")
            
            train_data, test_data = train_test_split(data,random_state= 42,test_size= 0.25)
            logging.info("train_test_split completed")
            train_data.to_csv(self.ingestion_config.train_data,index = False)
            test_data.to_csv(self.ingestion_config.test_data,index = False)

            logging.info("Data ingestion part completed.")
        except Exception as e:
            logging.info('EXCEPTION DURING OCCURED AT DATA INGESTION STAGE.')

            raise CustomException(e,sys)
