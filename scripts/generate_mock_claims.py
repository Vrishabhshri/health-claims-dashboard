import os
import random
from datetime import datetime, timedelta
import numpy as np 
import pandas as pd 
from faker import Faker 

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, "claims.csv")

fake = Faker()

n_rows = 2000

PROCS = [
    # code, description, base_charge_mean, base_charge_std, denial_prob
    ("99213", "Office/outpatient visit est", 150, 30, 0.05),
    ("99214", "Office/outpatient visit est, moderate", 250, 40, 0.06),
    ("70450", "CT head/brain w/o contrast", 900, 120, 0.08),
    ("73030", "X-ray shoulder 2+ views", 120, 20, 0.04),
    ("93000", "Electrocardiogram complete", 75, 15, 0.03),
    ("45378", "Diagnostic colonoscopy", 1800, 250, 0.11),
    ("29881", "Knee arthroscopy meniscectomy", 4500, 600, 0.12),
    ("71046", "Chest X-ray 2 views", 110, 18, 0.03),
    ("87086", "Urine culture", 65, 10, 0.05),
    ("88305", "Pathology tissue exam", 350, 60, 0.07),
]

PAYER_TYPES = [
    ("Commercial", 0.55, 0.80, 0.95),  # label, share, min%, max%
    ("Medicare",   0.25, 0.60, 0.85),
    ("Medicaid",   0.15, 0.50, 0.80),
    ("SelfPay",    0.05, 0.10, 0.50),
]

if __name__ == "__main__":
    main()