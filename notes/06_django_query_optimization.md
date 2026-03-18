# Django Query Optimization

# Lazy Loading Vs Eager Loading
## Lazy Loading
Lazy loading means related data is not loaded until it's explicitly accessed. This is the default behavior in Django ORM.

### Example
```py
orders = Order.objects.all()
for order in orders:
    print(order.customer.name)  # Triggers a DB query for each customer
```
### Problem
If we have 10 orders, and each order is linked to a customer, it will run 1 query for orders + 10 queries for customers = 11 queries. This is known as the `N+1` problem.

## Eager Loading
Eager loading means related data is fetched at the same time using `SQL JOINs` or additional queries. Django uses tools for eager loading:
- select_related() for `ForeignKey` and `OneToOne`
-prefetch_related() for `ManyToMany` and `reverse ForeignKey`

### Example(select_related)
```py
orders = Order.objects.select_related('customer').all()
for order in orders:
    print(order.customer.name)  # No extra query for each customer
```

### Example(prefetch_related)
```py
orders = Order.objects.prefetch_related('items').all()
for order in orders:
    for item in order.items.all():
        print(item.name)
```


# `select_related` vs `prefetch_related`

| Feature |	select_related | prefetch_related |
|---------|----------------|------------------|
| Use Case | ForeignKey, OneToOneField | ManyToMany, reverse ForeignKey |
| Query Type | Single JOIN query | Separate query + Python joining |
| Performance | Faster when joining single objects | Better for many-to-many or reverse relationships |
| Eager Loading? | Yes | Yes |