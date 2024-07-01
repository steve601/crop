import sys
import pandas as pd
from source.commons import load_object
from source.exception import UserException
from source.logger import logging
from sklearn.preprocessing import LabelEncoder


class PredicPipeline:
    def __init__(self):
        pass
    
    logging.info('Preprocessing user input and making predictions')
    def predict(self,features):
        model_path = 'elements\model.pkl'
        scaler_path = 'elements\scaler.pkl'
        # loaeding objects
        model = load_object(model_path)
        scaler = load_object(scaler_path)
        data_scaled = scaler.transform(features)
        prediction = model.predict(data_scaled)
        
        return prediction
logging.info('This class is responsible for mapping all the inputs from html to flask')
class UserData:
    def __init__(self,
                 N,P,K,
                humidity,ph,rainfall):
        self.n = N
        self.p = P
        self.k = K
        self.hum = humidity
        self.ph = ph
        self.rain = rainfall
        
    # let's write a function that returns the user input as a numpy array
    def get_data_as_df(self):
        try:
            user_data = {
                "N":[self.n],
                "P":[self.p],
                "K":[self.k],
                "humidity":[self.hum],
                "ph":[self.ph],
                "rainfall":[self.rain]
            }
            return pd.DataFrame(user_data)
        except Exception as e:
            raise UserException(e,sys)
        