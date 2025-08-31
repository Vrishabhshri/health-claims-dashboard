import os
import sqlite3
import pandas as pd 
from pathlib import Path 

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
SQL = ROOT / "sql"

DB_PATH = DATA / "claims.sqlite"
CSV_PATH = DATA / "claims.csv"

def run_sql(conn, path):
    with open(path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def df_from_query(conn, path):
    with open(path, "r", encoding="utf-8") as f:
        q = f.read()
    return pd.read_sql_query(q, conn)

def main():
    DATA.mkdir(exist_ok=True, parents=True)
    if not CSV_PATH.exists():
        raise SystemExit(f"Missing {CSV_PATH}. Run scripts/generate_mock_claims.py first.")

    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)

    run_sql(conn, SQL / "schema_sqlite.sql")

    df = pd.read_csv(CSV_PATH)
    df.to_sql("claims", conn, index=False, if_exists="append")

    revenue = df_from_query(conn, SQL / "revenue_by_procedure.sql")
    denial = df_from_query(conn, SQL / "denial_rates.sql")
    anomalies = df_from_query(conn, SQL / "anomalies_sqlite.sql")

    revenue.to_csv(DATA / "agg_revenue_by_procedure.csv", index=False)
    denial.to_csv(DATA / "agg_denial_rates.csv", index=False)
    anomalies.to_csv(DATA / "detected_anomalies.csv", index=False)

    print(f"SQLite DB: {DB_PATH}")
    print("Exported:")
    print(f" - {DATA / 'agg_revenue_by_procedure.csv'}")
    print(f" - {DATA / 'agg_denial_rates.csv'}")
    print(f" - {DATA / 'detected_anomalies.csv'}")

    conn.close()

if __name__ == "__main__":
    main()