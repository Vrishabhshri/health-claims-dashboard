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

payer_labels = [p[0] for p in PAYER_TYPES]
payer_weights = [p[1] for p in PAYER_TYPES]

start_date = datetime.today() - timedelta(days=365)
end_date = datetime.today()

def random_date(start, end):
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def draw_reimbursement(billing_amount, payer):
    p = next(p for p in PAYER_TYPES if p[0] == payer)
    paid_pct = random.uniform(p[2], p[3])
    return round(billing_amount * paid_pct, 2)

def main():
    rows = []

    for i in range(1, n_rows + 1):

        claim_id = f"C{i:06d}"
        patient_id = f"P{random.randint(1000, 1999)}"
        proc = random.choice(PROCS)
        code, desc, mu, sigma, denial_prob = proc

        amount = max(10, np.random.normal(mu, sigma))
        amount = round(amount, 2)

        payer = random.choices(payer_labels, weights=payer_weights, k=1)[0]
        dos = random_date(start_date, end_date).date()

        is_denied = 1 if random.random() < denial_prob else 0

        reimb = 0.0 if is_denied else draw_reimbursement(amount, payer)

        if random.random() < 0.01:
            factor = random.choice([3, 4, 5])
            amount = round(amount * factor, 2)
            if is_denied == 0:
                reimb = draw_reimbursement(amount, payer)

        rows.append({
            "claim_id": claim_id,
            "patient_id": patient_id,
            "procedure_code": code,
            "procedure_desc": desc,
            "billing_amount": amount,
            "insurance_reimbursement": reimb,
            "denial_flag": is_denied,
            "payer_type": payer,
            "date_of_service": str(dos)
        })

        df = pd.DataFrame(rows)
        df.to_csv(OUT_PATH, index=False)
        print(f"Wrote {len(df)} rows to {OUT_PATH}")

if __name__ == "__main__":
    main()