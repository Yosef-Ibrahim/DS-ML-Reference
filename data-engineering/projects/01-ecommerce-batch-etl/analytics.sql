-- Daily revenue and customer analytics for the batch ETL example.
-- Author: Youssef Ibrahim Mohamed Soliman | https://github.com/Yosef-Ibrahim

SELECT
    substr(order_ts, 1, 10) AS order_date,
    currency,
    COUNT(*) AS order_count,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS gross_revenue
FROM orders
GROUP BY substr(order_ts, 1, 10), currency
ORDER BY order_date, currency;

SELECT
    customer_id,
    COUNT(*) AS order_count,
    ROUND(SUM(quantity * unit_price), 2) AS customer_revenue,
    MAX(order_ts) AS last_order_ts
FROM orders
GROUP BY customer_id
ORDER BY customer_revenue DESC;
