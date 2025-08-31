SELECT
    procedure_code,
    procedure_desc,
    COUNT(*) as n_claims,
    SUM(denial_flag) AS denied_claims,
    ROUND(100.0 * SUM(denial_flag) / COUNT(*), 2) AS denial_rate_pct
FROM claims
GROUP BY procedure_code, procedure_desc
ORDER BY denial_rate_pct DESC, n_claims DESC;