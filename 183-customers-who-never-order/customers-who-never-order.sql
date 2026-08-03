select name as Customers from customers where customers.id not in (Select customerid from orders);
