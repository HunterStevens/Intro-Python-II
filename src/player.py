# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, move, currentRoom, items):
        self.currentRoom = currentRoom
        self.name = name
        self.move = move
        self.items = items
    def __str__(self):
        return f"Hello kid- er, {self.name}, you are Currently in: {self.currentRoom} with the items: \n {self.items}"

    def get_items(self):
        list = []
        for i in self.items:
            list.append(i.name)
        return list
    
    def get_specific_item(self, choice):
        for i in self.items:
            if choice == i.name:
                return f"{i.name}: {i.description}"
            else:
                print(f"not {i}")
        return f"Unfortunately, the item {choice} is not in your inventory."

    def add_item(self, newItem):
        self.items.append(newItem)
        return f"{self.name}, you just obtained {newItem}"

    def drop_item(self, pick):
        print(f"pick: {pick}")
        self.items.remove(pick)

    def direction(self):
        if "north" in self.move or "east" in self.move or "south" in self.move or "west" in self.move:
            attribute = self.move[0] + "_to"
            if hasattr(self.currentRoom, attribute):
                self.currentRoom = getattr(self.currentRoom, attribute)
                print(f"You moved to {self.currentRoom}")
            else:
                print(f"\n There are no rooms {self.move} of {self.currentRoom} \n")