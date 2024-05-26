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

    def __str__(self):
        return f'(name: {self.name}; price: {self.price})'


class ItemCorpus:
    def __init__(self):
        self.item_lst = []

    def add_item(self, item):
        # Remove the old item and use the item name
        # to identifiy item
        for i, item_2 in enumerate(self.item_lst):
            if item.name == item_2.name:
                self.item_lst.pop(i)
                break

        self.item_lst.append(item)

        # print(item)

    def remove_item(self, item):
        for i, item in enumerate(self.item_lst):
            if item.name == item.name:
                self.item_lst.pop(i)
                break

    def refresh(self, item):
        self.remove_item(item)
        self.add_item(item)

    def __iter__(self):
        self.index = len(self.item_lst) - 1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            res = self.item_lst[self.index]
            self.index -= 1
            return res


        

