import os
import sys
import numpy as np
import pandas as pd
from source.exception import UserException
from source.logger import logging
from sklearn.preprocessing import MinMaxScaler
from source.commons import save_object
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    scaler_obj_path:str = os.path.join('elements','scaler.pkl')
    
class DataTransformation:
    def __init__(self):
        self.data_trans_config = DataTransformationConfig()
        
    def get_scaler_obj(self):
        try:
            logging.info('Obtaining the encoder object')
            scaler = MinMaxScaler()
            return scaler
        except Exception as e:
            raise UserException(e,sys)

        
    def start_data_transformation(self,train_data_path,test_data_path):
        try:
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)
            logging.info('Successfully read trin and test set')
            logging.info('Obtaining scaler object')
            
            scaler_obj = self.get_scaler_obj()
            target_column = 'label'
            
            logging.info('Separating into independent and dependent features for both sets')
            input_feature_train_df = train_df.drop(target_column,axis=1)
            dependent_feature_train_df = train_df[target_column]
            
            input_feature_test_df = test_df.drop(target_column,axis=1)
            dependent_feature_test_df = test_df[target_column]
            
            logging.info('Fitting preprocessor object on the data')
            
            input_feature_train_arr = scaler_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = scaler_obj.transform(input_feature_test_df)
            logging.info('Concatenating splits into 2D arrays')
            
            train_arr = np.c_[input_feature_train_arr,np.array(dependent_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(dependent_feature_test_df)]
            
            save_object(
                file_path = self.data_trans_config.scaler_obj_path,
                obj = scaler_obj)
            
            return(
                train_arr,
                test_arr,
            )
            
        except Exception as e:
            raise UserException(e,sys)
            
            