from room import Room
from player import Player
from items import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("little_feather", "it's your lucky charm from your childhood. Why couldn't you remember that?")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("telescope", "a device probably used for skywatching")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].north_to = room['foyer']
room['foyer'].south_to = room['outside']
room['foyer'].north_to = room['overlook']
room['foyer'].east_to = room['narrow']
room['overlook'].south_to = room['foyer']
room['narrow'].west_to = room['foyer']
room['narrow'].north_to = room['treasure']
room['treasure'].south_to = room['narrow']

# Main

def player_take(Taking_item):
    for i in playerOne.currentRoom.items:
        if i.name == Taking_item:
            found_item = i
        playerOne.add_item(found_item)
        playerOne.currentRoom.drop_item(found_item)
    else:
        print(f"{Taking_item} does not exist in this room")

# Make a new player object that is currently in the 'outside' room.
playerOne = Player("player", "nowhere", room['outside'], [])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
playerOne.name = input("What's your name kid?  -> ")
print(playerOne)
print("\n Chose what you want to do with: \n north, south, west, east, \n 'inspect' to look within the room, and 'q' to QUIT \n")


quit_game = False
while not quit_game:
    print(playerOne.currentRoom.attributes)
    playerOne.move = input(" ").strip().lower().split(" ")
    
#Check for directional input first
    playerOne.direction()
#Search Room
    if "inspect" in playerOne.move:
        print(f"{playerOne.currentRoom.name} currently has {playerOne.currentRoom.get_items()}")

#Take an item in the room
    elif "take" in playerOne.move:
        print(playerOne.move)
        choice = playerOne.move[1]
        player_take(choice)

#Checking inventory
    elif "inventory" in playerOne.move:
        print

#QUITING
    elif "q" in playerOne.move:
        print("You RAGED QUIT")
        quit_game = True

#any other type of input
    else:
        print("Enter in a valid choice, I'm not programmed to read acutal words or something.")