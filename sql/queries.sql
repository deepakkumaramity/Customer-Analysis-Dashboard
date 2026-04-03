-- Revenue per customer
SELECT customer_id, SUM(price * quantity) AS revenue
FROM sales
GROUP BY customer_id;

-- Top 5 customers
SELECT customer_id, SUM(price * quantity) AS total_spent
FROM sales
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5;

-- Repeat customers
SELECT customer_id, COUNT(*) AS orders
FROM sales
GROUP BY customer_id
HAVING COUNT(*) > 1;
