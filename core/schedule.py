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

from . import item

class Scheduler:
    def __init__(self, item_corpus: item.ItemCorpus):
        # self.items = {} # key: item_name; value: item_frequency
        self.item_corpus = item_corpus
        self.item_cart = []
        self.total_price = 0
        self.target_total_price = None

    def set_target_total_price(self, target_total_price):
        self.target_total_price = target_total_price

    def meet_target_total_price(self):
        return self.total_price >= self.target_total_price

    def add_item(self, item: item.Item):
        self.item_cart.append(item)
        self.total_price += item.price
        self.item_corpus.add_item(item)
        
    def recommend_items(self):
        backup_items = []

        if self.target_total_price is None:
            return backup_items

        self.total_price = 0

        # print('-' * 10)
        # self.print_items(self.item_corpus)
        # print('-' * 10)

        for item in self.item_corpus:
            backup_items.append(item)

            # print('+' * 10)
            # print(item)
            # print('+' * 10)

            self.total_price += item.price
            if self.total_price >= self.target_total_price:
                break

        return backup_items

    # For debug infor
    @staticmethod
    def print_items(items):
        print('[' + ";".join([str(item) for item in items]) + ']')


def main():
    scheduler = Scheduler(item.ItemCorpus())    
    scheduler.set_target_total_price(45)

    item0 = item.Item('apple', 3)
    item1 = item.Item('banana', 4)
    item2 = item.Item('watermelon', 4)
    item3 = item.Item('mango', 5)
    item4 = item.Item('item4', 6)
    item5 = item.Item('item5', 7)
    item6 = item.Item('item6', 8)
    item7 = item.Item('item7', 9)
    item8 = item.Item('item8', 10)
    item9 = item.Item('item9', 11)
    item10 = item.Item('item10', 12)

    # Scheduler.print_items(scheduler.item_cart)
    scheduler.add_item(item0)
    # Scheduler.print_items(scheduler.item_cart)
    scheduler.add_item(item1)
    # Scheduler.print_items(scheduler.item_cart)
    scheduler.add_item(item2)
    # Scheduler.print_items(scheduler.item_cart)
    scheduler.add_item(item3)
    scheduler.add_item(item4)
    scheduler.add_item(item5)
    scheduler.add_item(item6)
    scheduler.add_item(item7)
    scheduler.add_item(item8)
    scheduler.add_item(item9)
    scheduler.add_item(item10)

    Scheduler.print_items(scheduler.recommend_items())


if __name__ == '__main__':
    main()