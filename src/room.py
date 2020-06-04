# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, attributes, items=[]):
        self.name = name
        self.attributes = attributes
        self.items = items

    def __str__(self):
        return f"{self.name}"

    def add_item(self, newItem):
        self.items.append(newItem)
        return f"{newItem} was added to {self.name}"
    
    def drop_item(self, pick):
        for i in self.items:
            if self.items[i] == int(pick):
                self.items.remove(i)
            else:
                pass