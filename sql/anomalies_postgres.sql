WITH s AS (
    SELECT 
        AVG(billing_amount) as mu,
        STDDEV_POP(billing_amount) as sigma
    FROM claims
)

SELECT c.*,
    ROUND(s.mu::numeric, 2) AS global_mean,
    ROUND(s.sigma::numeric, 2) AS global_stddev,
    CASE
        WHEN c.billing_amount > (s.mu + 3 * s.sigma) THEN 1
        ELSE 0
    END AS is_high_outlier
FROM claims c 
CROSS JOIN s 
WHERE c.billing_amount > (s.mu + 3 * s.sigma)
ORDER BY c.billing_amount DESC;