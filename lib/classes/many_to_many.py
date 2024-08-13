class Coffee:

    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and not hasattr(self, 'name'):
            self._name = value
    
        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list(set([order.customer for order in self.orders()]))
    
    def num_orders(self):
       total_orders = 0 
       for order in Order.all:
           if order.coffee == self:
               total_orders += 1
       return total_orders
    
    def average_price(self):
        total_price = 0
        total_orders = 0
        for order in Order.all:
            if order.coffee == self:
                total_price += order.price  # Sum up the prices
                total_orders += 1  # Count the number of orders
        # Calculate the average price, return 0 if no orders
        return total_price / total_orders if total_orders > 0 else 0


class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if(isinstance(value, str) and 1 <= len(value) <= 15):
            self._name = value

        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))
    
    def create_order(self, coffee, price):
        return Order(customer=self, coffee= coffee, price = price)
    
class Order:

    all = [] 

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and 1.0 <= value <= 10.0 and not hasattr(self, 'price'):
            self._price = value

    @property 
    def customer(self):
        return self._customer 
    
    @customer.setter
    def customer(self, value):
        if(isinstance(value, Customer)):
            self._customer = value
    
    @property 
    def coffee(self):
        return self._coffee 
    
    @coffee.setter
    def coffee(self, value):
        if(isinstance(value, Coffee)):
            self._coffee = value


