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