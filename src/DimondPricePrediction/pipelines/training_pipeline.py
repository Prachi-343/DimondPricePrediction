
from src.DimondPricePrediction.components.data_ingestion import DataIngestion

import numpy as np
import pandas as pd
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception

data_ingestion=DataIngestion()
train_data_path,test_data_path=data_ingestion.initate_data_ingestion()

