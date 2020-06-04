from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

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
print("\n Chose what you want to do with: \n 'n' to go NORTH, 's' to go SOUTH, w to go 'WEST', 'e' to go EAST, 's' to search within the room, and 'q' to QUIT \n")



while playerOne.move != "q":
    print(playerOne.currentRoom.attributes)
    playerOne.move = input(" ").strip().lower()
    attribute = playerOne.move + "_to"

#GOING NORTH
    if playerOne.move == "n":
        if hasattr(playerOne.currentRoom, attribute):
            print("You went NORTH")
            playerOne.currentRoom = playerOne.currentRoom.n_to
        else:
            print(f"\n There are no rooms North of {playerOne.currentRoom} \n")

#GOING EAST
    elif playerOne.move == "e":
        if hasattr(playerOne.currentRoom, attribute):
            print("You went EAST")
            playerOne.currentRoom = playerOne.currentRoom.e_to
        else:
            print(f"\n There are no rooms East of {playerOne.currentRoom} \n")

#GOING SOUTH
    elif playerOne.move == "s":
        if hasattr(playerOne.currentRoom, attribute):
            print("You went SOUTH")
            playerOne.currentRoom = playerOne.currentRoom.s_to
        else:
            print(f"\n There are no rooms South of {playerOne.currentRoom} \n")

#GOING WEST 
    elif playerOne.move == "w":
        if hasattr(playerOne.currentRoom, attribute):
            print("You went WEST")
            playerOne.currentRoom = playerOne.currentRoom.w_to
        else:
            print(f"\n There are no rooms West of {playerOne.currentRoom} \n")

#QUITING
    elif playerOne.move == "q":
        print("You RAGED QUIT")

#any other type of input
    else:
        print("Enter in a valid direction, I'm not programmed to read acutal words or something.")