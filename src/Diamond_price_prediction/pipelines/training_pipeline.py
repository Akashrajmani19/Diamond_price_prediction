from src.Diamond_price_prediction.components.data_integration import DataIntegration
from src.Diamond_price_prediction.components.data_transformation import DataTransformation
from src.Diamond_price_prediction.components.model_trainer import ModelTrainer
import os
import sys
from src.Diamond_price_prediction.logger import logging
from src.Diamond_price_prediction.exception import CustomException
import pandas as pd

obj=DataIntegration()

train_data_path,test_data_path=obj.initiate_data_integration()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)