from src.Diamond_price_prediction.components.data_integration import DataIntegration
import pandas as pd
import numpy as np
from src.Diamond_price_prediction.logger import logging
from src.Diamond_price_prediction.exception import CustomException
import os
import sys

obj = DataIntegration()

obj.initiate_data_integration()