"""Main module."""
from dataclasses import dataclass

@dataclass
class Price:
    """All about price."""
    def __init__(self, price):
        self.price: float
        
        try:
            self.price = float(price)
        except ValueError as e:
            self.price = 0.00
            print(f'Price must be floating point. Set price to {self.price}') # expect 0.00

    def price_difference(self, higher_price):
        """A simple calculation on the increase / decrease of crypto price."""
        diff = (higher_price.price - self.price) / self.price
        return diff
