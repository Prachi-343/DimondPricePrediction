from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.components.model_trainer import ModelTrainer

import os
import sys
import numpy as np
import pandas as pd
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

class TrainingPipeline:  # Corrected the class name
    def start_data_ingestion(self):
        try:
            data_ingest = DataIngestion()
            train_data_path, test_data_path = data_ingest.initate_data_ingestion()  # Corrected the method name
            return train_data_path, test_data_path
        except Exception as e:
            raise customexception(e, sys)
        
    def start_data_transformation(self, train_data_path, test_data_path):
        try:
            data_transformation = DataTransformation()
            train_arr, test_arr = data_transformation.initate_data_transformations(train_data_path, test_data_path)  # Corrected the method name
            return train_arr, test_arr
        except Exception as e:
            raise customexception(e, sys)
        
    def start_model_training(self, train_arr, test_arr):
        try:
            model_trainer = ModelTrainer()
            model_trainer.initate_model_training(train_arr, test_arr)  # Assuming the method name is correct
        except Exception as e:
            raise customexception(e, sys)

    def start_training(self):
        try:
            train_data_path, test_data_path = self.start_data_ingestion()
            train_arr, test_arr = self.start_data_transformation(train_data_path, test_data_path)
            self.start_model_training(train_arr, test_arr)
        except Exception as e:
            raise customexception(e, sys)

if __name__ == "__main__":
    training_obj = TrainingPipeline()  # Corrected the object instantiation
    training_obj.start_training()
