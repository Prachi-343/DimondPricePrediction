
from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.components.model_trainer import ModelTrainer

import numpy as np
import pandas as pd
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

class TrainingPipeline:
    def start_data_ingestion(self):
        try:
            data_ingestion=DataIngestion()
            train_data_path,test_data_path=data_ingestion.initate_data_ingestion()
            return train_data_path,test_data_path
        except Exception as e:
            raise customexception(e,sys)
        
    def start_data_transformations(self, train_data_path,test_data_path):
        try:
            data_transformation=DataTransformation()
            train_arr,test_arr=data_transformation.initate_data_transformations(train_data_path,test_data_path)
            return train_arr,test_arr
        except Exception as e:
            raise customexception(e,sys)
        
    def start_model_training(self,train_arr,test_arr): 
        try:
            model_trainer=ModelTrainer()
            model_trainer.initate_model_training(train_arr,test_arr)
        except Exception as e:
            raise customexception(e,sys)
        
    def start_training(self):
        try:
            train_data_path,test_data_path=self.start_data_ingestion()
            train_arr,test_arr=self.start_data_transformations(train_data_path,test_data_path)
            self.start_model_training(train_arr,test_arr)    
        except Exception as e:
            raise customexception(e,sys)

training_obj=TrainingPipeline()
training_obj.start_training()