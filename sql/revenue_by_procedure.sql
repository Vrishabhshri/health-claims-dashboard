SELECT 
    procedure_code, 
    procedure_desc, 
    ROUND(SUM(billing_amount), 2) AS total_revenue, 
    COUNT(*) as n_claims,
    ROUND(AVG(billing_amount), 2) AS avg_charge
FROM claims
GROUP BY procedure_code, procedure_desc
ORDER BY total_revenue DESC;