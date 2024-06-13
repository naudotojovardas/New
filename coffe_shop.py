class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item_name):
        for item in self.menu:
            if item['item'] == item_name:
                self.orders.append(item_name)
                return f"{item_name} added to the order!"
        return "This item is currently unavailable!"

    def fulfill_order(self):
        if self.orders:
            item = self.orders.pop(0)
            return f"The {item} is ready!"
        return "All orders have been fulfilled!"

    def list_orders(self):
        return self.orders

    def due_amount(self):
        total = 0
        for order in self.orders:
            for item in self.menu:
                if item['item'] == order:
                    total += item['price']
        return total

    def cheapest_item(self):
        cheapest = min(self.menu, key=lambda x: x['price'])
        return cheapest['item']

    def drinks_only(self):
        return [item['item'] for item in self.menu if item['type'] == 'drink']

    def food_only(self):
        return [item['item'] for item in self.menu if item['type'] == 'food']

menu = [
    {"item": "Latte", "type": "drink", "price": 3.5},
    {"item": "Espresso", "type": "drink", "price": 2.5},
    {"item": "Croissant", "type": "food", "price": 2.0},
    {"item": "Sandwich", "type": "food", "price": 4.5},
]

shop = CoffeeShop("Kavutes", menu)

print(shop.add_order("Latte"))
print(shop.add_order("Sandwich")) 
print(shop.add_order("Tea")) 

print(shop.fulfill_order())
print(shop.fulfill_order())
print(shop.fulfill_order())

print(shop.list_orders()) 
print(shop.due_amount())
print(shop.cheapest_item())

print(shop.drinks_only())
print(shop.food_only())

        