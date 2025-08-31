import os
import random
from datetime import datetime, timedelta
import numpy as np 
import pandas as pd 
from faker import Faker 

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "claims.csv")

