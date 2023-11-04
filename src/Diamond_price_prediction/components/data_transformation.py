import pandas as pd
import numpy as np
from src.Diamond_price_prediction.logger import logging
from src.Diamond_price_prediction.exception import CustomException
import os 
import sys
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder, StandardScaler

from src.Diamond_price_prediction.utils.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
         
        # Define which columns should be ordinal-encodded and which should be scaled
        categorical_cols = ["cut", 'color', 'clarity']
        numerical_cols = ['carat','depth' ,'table',"x",'y','z'] 

        # Define the customs ranking for each ordinal variable
        cut_map = ['Fair', 'Good', 'Very Good','Premium','Ideal']
        clarity_map = ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
        colore_map = ["D","E","F","G","H","I","J"]

        logging.info('Pipeline Initiated')

        # numerical pipeline
        num_pipeline = Pipeline(steps= [
            ("imputer",SimpleImputer(strategy= 'median')),
            ("scalar",StandardScaler())
        ])

        # Categorical pipeline
        cat_pipeline = Pipeline(steps = [
            ('imputer',SimpleImputer(strategy='most_frequent')),
            ('ordinalencodder',OrdinalEncoder(categories= [cut_map,colore_map,clarity_map]))
        ])

        # Now implementing this pipelines
        preprocessor = ColumnTransformer(
            [
                ('num_pipeline',num_pipeline,numerical_columns),
                ('cat_pipeline',cat_pipeline,Categorical_columns)
            ]
        )

        return preprocessor


    def get_data_transformation(self):
        try:
            logging.info("Data transformation initiated")

        except Exception as e:
            logging.info("Exception occured in the intiate_datatransformation")
            raise CustomException(e,sys) 

    def initialize_data_transformation(self,train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df= pd.resd_csv(test_path)

            logging.info("read train and test data complete")
            logging.info(f"Train DataFrame Head :\n{train_df.head().to_string()}")
            logging.info(f"Test DataFrame Head :\n{test_df.head().to_string()}")

            preprocessor_obj = self.get_data_transformation()
            target_column = 'price'
            drop_columns = [target_column_name,'id']

            input_feature_train_df = train_df.drop(columns=drop_columns,axis =1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)
            logging.info("Applying preproccesing object on training abd testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
                )
            logging.info("Preproccessing picklefile saved")
            return(
                train_arr,
                test_arr
            )

        except Exception as e:
            logging.info("Exception occured in the intiate_datatransformation")
            raise CustomException(e,sys) 