SELECT customer.full_name
FROM customer
LEFT JOIN "order" orders ON orders.customer_id = customer.customer_id
WHERE orders.order_no IS NULL;