# Write your MySQL query statement below
SELECT DISTINCT P1.email FROM Person P1, Person P2
WHERE P1.id <> P2.id AND P1.email = P2.email