SELECT customer.full_name AS customer_name, manager.full_name AS manager_name, orders.purchase_amount, orders.date
FROM "order" orders
JOIN customer ON orders.customer_id = customer.customer_id
LEFT JOIN manager ON orders.manager_id = manager.manager_id OR manager.manager_id IS NULL;
