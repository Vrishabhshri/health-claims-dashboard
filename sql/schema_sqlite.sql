DROP TABLE IF EXISTS claims;

CREATE TABLE claims (
    claim_id TEXT PRIMARY KEY,
    patient_id TEXT NOT NULL,
    procedure_code TEXT NOT NULL,
    procedure_desc TEXT,
    billing_amount REAL NOT NULL,
    insurance_reimbursement REAL NOT NULL,
    denial_flag INTEGER NOT NULL CHECK (denial_flag IN (0,1)),
    payer_type TEXT NOT NULL,
    date_of_service TEXT NOT NULL
);

CREATE INDEX idx_claims_proc ON claims(procedure_code);
CREATE INDEX idx_claims_dos ON claims(date_of_service);
CREATE INDEX idx_claims_denial on claims(denial_flag);