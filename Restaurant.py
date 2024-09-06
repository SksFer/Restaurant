class Restaurant:
    def __init__(self):
        self.menu = {}
        self.reserved_tables = {}
        self.orders = {}
        
    def add_item_to_menu(self, item_name, price):
        self.menu[item_name] = price
    
    def reserve_table(self, number, client_name):
        if number not in self.reserved_tables:
            self.reserved_tables[number] = client_name
        else:
            print(f"Table {number} is already reserved by {self.reserved_tables[number]}")
    
    def add_order(self, number, item_name):
        if number not in self.orders:
            self.orders[number] = [item_name]
        else:
            self.orders[number].append(item_name)
                    
    def print_menu(self):
        print(self.menu)
    
    def print_orders(self):
        print(self.orders)
    
    def print_reserved_tables(self):
        print(self.reserved_tables)

# Uso del código corregido
restaurant = Restaurant()
restaurant.add_item_to_menu("Hamburguer", 4.5)
restaurant.add_item_to_menu("Hot Dog", 3)

restaurant.reserve_table(1, "Sack")
restaurant.reserve_table(2, "Jack")

restaurant.add_order(1, "Hamburguer")
restaurant.add_order(1, "Hot Dog")
restaurant.add_order(2, "Hot Dog")

restaurant.print_menu()
restaurant.print_orders()
restaurant.print_reserved_tables()
