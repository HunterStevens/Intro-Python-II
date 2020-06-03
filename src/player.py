# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, move, currentRoom, items):
        self.currentRoom = currentRoom
        self.move = move
        self.items = items
    def __str__(self):
        return f"you are Currently in: {self.currentRoom} with the items: \n {self.items}"