from collections import defaultdict

class StockPrice:

    def __init__(self):
        # per-instance storage (avoid shared mutable class attributes)
        self.values = defaultdict(int)
        self.current_price = 0
        self.minimum_price = float('inf')
        self.maximum_price = float('-inf')

    def update(self, timestamp: int, price: int) -> None:
        self.current_price = price
        prev_val = self.values[timestamp]
        if prev_val and prev_val != price:
            if prev_val < price:
                self.minimum_price = min(price)
                self.maximum_price = max(self.maximum_price, price)   
            elif prev_val > price:
                self.minimum_price = min(self.minimum_price, price)
                self.maximum_price = max(self.maximum_price, price)  
        else:
            self.minimum_price = min(self.minimum_price, price)        
            self.maximum_price = max(self.maximum_price, price)        
        
        self.values[timestamp] = price

    def current(self) -> int:
        return self.current_price        

    def maximum(self) -> int:
        return self.maximum_price

    def minimum(self) -> int:
        return self.minimum_price        
    
    def get_values(self):
        """Return the stored timestamp->price mapping."""
        return self.values

# Your StockPrice object will be instantiated and called as such:
obj = StockPrice()
obj.update(1,10)
obj.update(2,0)
obj.update(3,5)
obj.update(4,1)
obj.update(1,2)
obj.update(2,3)
curr = obj.current()
max = obj.maximum()
min = obj.minimum()
print(f'Current: {curr}, Max: {max}, Min: {min}, Values: {obj.get_values()}')