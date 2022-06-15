from typing import List

class ShoppingCart:
    
    def __init__(self, max_size: int=5) -> None:
        
        self.max_size = max_size
        self.items: List[str] = []

    def add(self, item: str):
        
        if self.size() == self.max_size:
            raise OverflowError("Cannot add more items")
        self.items.append(item)

    def size(self) -> int:
        
        return len(self.items)

    def get_items(self) -> List[str]:
        
        return self.items

    def get_total_price(
            self, 
            price_map):
                
        return sum([price_map.get(item) for item in self.get_items()])
