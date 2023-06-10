SELECT customer.name AS customer_name, orders.order_no
FROM "order" orders
JOIN customer on customer.customer_id = orders.customer_id
WHERE orders.manager_id IS NULL;