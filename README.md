Healthcare Claims Dashboard

A reproducible mini-project to simulate healthcare claims, run SQL analyses, and visualize insights in Tableau or Power BI.

Goals:
 - Mock dataset of claims (patient, procedure, charges, reimbursements, denials, payer, DOS)
 - SQL to compute:
    - Revenue by procedure
    - Denial rates
    - Anomaly detection (high charges)
- Dashboard in Tableau / Power BI

Quickstart

```bash
git clone https://github.com/Vrishabhshri/healthcare-claims-dashboard.git
cd healthcare-claims-dashboard
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt