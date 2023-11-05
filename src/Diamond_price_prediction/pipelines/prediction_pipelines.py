from src.Diamond_price_prediction.utils.utils import load_object
import pandas as pd
import numpy as np
from src.Diamond_price_prediction.logger import logging
from src.Diamond_price_prediction.exception import CustomException
import os
import sys

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,feature):
        try:
            preprocessor_path = os.path.join('artifacts','preprocessor.pkl')
            model_path = os.path.join('artifacts','model.pkl')

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            scaled_data = preprocessor.transform(feature)

            pred = model.predict(scaled_data)
            return pred
    
        except Exception as e:
            raise CustomException(e,sys) 

class CustomData:
    def __init__(self,
                carat:float,
                depth:float,
                table:float,
                x:float,
                y:float,
                z:float,
                cut:str,
                color:str,
                clarity:str
                ):
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.carat],
                'depth':[self.depth],
                'table':[self.table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.cut],
                'color':[self.color],
                'clarity':[self.clarity] 
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame Gathered')

            return df
        except Exception as e:
            logging.info('Exception occured in prediction pipeline')
            raise CustomException(e,sys)
           