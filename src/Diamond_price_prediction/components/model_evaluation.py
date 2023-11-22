import os
import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score
from urllib.parse import urlparse
import  mlflow  
import mlflow.sklearn
import numpy as np
import pickle
from src.Diamond_price_prediction.utils.utils import load_object
from src.Diamond_price_prediction.logger import logging
from src.Diamond_price_prediction.exception import CustomException

class ModelEvaluation:
    def __init__(self):
        pass

    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae = mean_absolute_error(actual,pred)
        r2 = r2_score(actual,pred)
        return rmse,mae,r2
    
    def initiate_model_evaluation(self,train_array,test_array):
        try:
            X_train,X_test,Y_train,Y_test = (train_array[:,:-1],
                                            train_array[:,-1],
                                            test_array[:,:-1],
                                            test_array[:,-1]
                                             )
            model_path = os.path.join("artifacts","model.pkl")
            model = load_object(model_path) # loading our trained model



            with mlflow.start_run():
                predicted_qualities = model.predict(Y_train)
                (rmse,mae,r2) = self.eval_metrics(Y_test,predicted_qualities)

                mlflow.log_metric("rmse",rmse)
                mlflow.log_metric("mae",mae)
                mlflow.log_metric("r2",r2)
        except Exception as e:
            logging.info("Exception occured in the intiate_model_evaluation")
            raise CustomException(e,sys)


                