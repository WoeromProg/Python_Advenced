SELECT orders.order_no, customer.full_name AS customer_name, manager.full_name AS manager_name
FROM "order" orders
JOIN customer ON orders.customer_id = customer.customer_id
JOIN manager ON manager.manager_id = orders.manager_id
WHERE customer.city != manager.city;