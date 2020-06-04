# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, attributes, items=[]):
        self.name = name
        self.attributes = attributes
        self.items = items

    def __str__(self):
        return f"{self.name}"

    def get_items(self):
        list = []
        for i in self.items:
            list.append(i.name)
        return list

    def add_item(self, newItem):
        self.items.append(newItem)
        return f"{newItem} was added to {self.name}"
    
    def drop_item(self, pick):
        print(f"pick: {pick}")
        self.items.remove(pick)