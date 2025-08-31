WITH stats AS (
  SELECT
    AVG(billing_amount) AS mu,
    AVG(billing_amount * billing_amount) AS ex2
  FROM claims
),
threshold AS (
  SELECT
    mu,
    -- stddev = sqrt(E[x^2] - (E[x])^2)
    CASE
      WHEN ex2 - (mu * mu) < 0 THEN 0
      ELSE sqrt(ex2 - (mu * mu))
    END AS sigma
  FROM stats
)
SELECT c.*,
       ROUND(t.mu,2) AS global_mean,
       ROUND(t.sigma,2) AS global_stddev,
       CASE WHEN c.billing_amount > (t.mu + 3 * t.sigma) THEN 1 ELSE 0 END AS is_high_outlier
FROM claims c
CROSS JOIN threshold t
WHERE c.billing_amount > (t.mu + 3 * t.sigma)
ORDER BY c.billing_amount DESC;