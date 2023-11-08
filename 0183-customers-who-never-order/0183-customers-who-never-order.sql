# Write your MySQL query statement below
SELECT name AS customers 
FROM customers 
WHERE id not in (SELECT customerID from orders)