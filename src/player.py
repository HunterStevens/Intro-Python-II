# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, move, currentRoom='outside'):
        self.currentRoom = currentRoom
        self.move = move
