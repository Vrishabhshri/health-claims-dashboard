DROP TABLE IF EXISTS claims;

CREATE TABLE claims (
  claim_id TEXT PRIMARY KEY,
  patient_id TEXT NOT NULL,
  procedure_code TEXT NOT NULL,
  procedure_desc TEXT,
  billing_amount NUMERIC(12,2) NOT NULL,
  insurance_reimbursement NUMERIC(12,2) NOT NULL,
  denial_flag INT NOT NULL CHECK (denial_flag IN (0,1)),
  payer_type TEXT NOT NULL,
  date_of_service DATE NOT NULL
);

CREATE INDEX idx_claims_proc ON claims(procedure_code);
CREATE INDEX idx_claims_dos ON claims(date_of_service);
CREATE INDEX idx_claims_denial ON claims(denial_flag);