# Write your MySQL query statement below
SELECT Emp.name AS Employee FROM Employee emp, Employee mgr
WHERE Emp.managerId = mgr.id AND emp.salary > mgr.salary