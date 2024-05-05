# Main function:
#   1. Suggestion items based on the frequency for fixed total price
#
# Details:
#   1. One item may be used for serveral times with changing prices.
#     Use the latest item price to update.
#
# Keys:
#   1. The algorithm of recommendation items.
#   2. The display method for a better appearance. 

class Scheduler:
    def __init__(self):
        self.items = {} # key: item_name; value: item_frequency
        self.target_total_price = None

    def update_total_price(self, total_price):
        self.target_total_price = total_price

    def set_total_price(self, total_price):
        self.update_total_price(total_price)

    def add_items(self):
        Item.get_latest_item()
        
    def recommend_items(self):
        pass

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def get_latest_item(cls):
        # Sample case
        name = "Sample name"
        price = 1.00
        return cls(name, price)


def main():
    scheduler = Scheduler()    
    scheduler.set_total_price = 99
    scheduler.add_items()
    scheduler.add_items()
    scheduler.add_items()


if __file__ == '__main__':
    main()