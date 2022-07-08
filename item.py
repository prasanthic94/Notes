import csv


class Item:
    
    pay_rate = 0.8 
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        
        
        # Run validations to the received arguments
        assert price >=0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >=0, f"Quantity {quantity} is not greater than or equal to zero!"
        
        #Assign to self object
        self. _name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
    
    @property
    # Property Decorator = Read-only Attribute
    def name(self):
        return self._name
    
    def calculate_total_price(self):
        return self.price * self.quantity
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
        
    @classmethod
    def instantiate_from_csv(cls):...
                             
    @staticmethod
    def is_integer(num):...
                             
    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}',{self.price}, {self.quantity})"
    
    