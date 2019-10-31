from room import Room
from player import Player
from item import Item

# Declare all the rooms

cookies = Item("Cookies", "Feeling Hungry?") 
mojito = Item("Mojito", "Are you thirsty?")
pizza = Item("Pizza", "Its dinnertime!")
hacksaw = Item("Hacksaw", "This will cut through doors")
torch = Item("Torch", "Lets roast these marshmallows")
shoes = Item("Shoes", "Get some exercise ya goof")
pumpkin = Item("Pumpkin", "Happy Halloween")
knife = Item("Knife", "Be careful its sharp")
toilet = Item("Toilet", "Everyones gotta go eventually")
pillow = Item("Pillow", "You've been walking awhile, take a nap.")
pen = Item("Pen", "For writing")
paper = Item("Paper", "Write down clues")
pony = Item("Pony", "Lets get out of here")
candle = Item("Candle", "Need some light?")
jacket = Item("Jacket", "Its cold outside!")

room = {
    'outside':  
        Room(
            "Outside Cave Entrance", 
            "North of you, the cave mount beckons", 
            [cookies, mojito, pizza]
        ),
    'foyer':    
        Room(
            "Foyer", 
            """Dim light filters in from the south. Dusty passages run north and east.""", 
            [hacksaw, torch, shoes]
        ),
    'overlook': 
        Room(
            "Grand Overlook", 
            """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", 
            [pumpkin, knife, toilet]
        ),
    'narrow':   
        Room(
            "Narrow Passage", 
            """The narrow passage bends here from west to north. The smell of gold permeates the air.""", 
            [pillow, pen, paper]
        ),
    'treasure': 
        Room(
            "Treasure Chamber", 
            """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", 
            [pony, candle, jacket]
        ),
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
player1 = Player("Anthony", room['outside'])
# Write a loop that:
#

listed_item = [f"{i.name}: {i.description}" for i in player1.current_room.item_list]


print(player1.current_room)
for i in range(0, len(listed_item)):
    print(listed_item[i])
print(f"\n")
user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.



while not user  == "q":
    if user == "n":
        if hasattr(player1.current_room, 'n_to'):
            player1.current_room = player1.current_room.n_to
            listed_item = [f"{i.name}: {i.description}" for i in player1.current_room.item_list]
            print(f"\n\n{player1.current_room}")
            print("Available Items in this Room:")
            for i in range(0, len(listed_item)):
                print(listed_item[i])
            print(f"\n")
        else:
            print(f"\n\n*******Invalid Direction Please Select Again\n{player1.current_room}")
            print("Available Items in this Room:")
            for i in range(0, len(listed_item)):
                print(listed_item[i])
    elif user == "s":
        if hasattr(player1.current_room, 's_to'):
            player1.current_room = player1.current_room.s_to
            listed_item = [f"{i.name}: {i.description}" for i in player1.current_room.item_list]
            print(f"\n\n{player1.current_room}")
            print("Available Items in this Room:")
            print("Available Items in this Room:")
            for i in range(0, len(listed_item)):
                print(listed_item[i])
            print(f"\n")
        else:
            print(f"\n\n*******Invalid Direction Please Select Again\n{player1.current_room}") 
            print("Available Items in this Room:")
            for i in range(0, len(listed_item)):
                print(listed_item[i])
    elif user == "e":
        if hasattr(player1.current_room, 'e_to'):
            player1.current_room = player1.current_room.e_to
            listed_item = [f"{i.name}: {i.description}" for i in player1.current_room.item_list]
            print(f"\n\n{player1.current_room}")
            print("Available Items in this Room:")
            for i in range(0, len(listed_item)):
                print(listed_item[i])
            print(f"\n")
        else:
            print(f"\n\n*******Invalid Direction Please Select Again\n{player1.current_room}") 
            print("Available Items in this Room:")
            for i in range(0, len(listed_item)):
                print(listed_item[i])
    elif user == "w":
        if hasattr(player1.current_room, 'w_to'):
            player1.current_room = player1.current_room.w_to
            listed_item = [f"{i.name}: {i.description}" for i in player1.current_room.item_list]
            print(f"\n\n{player1.current_room}")
            print("Available Items in this Room:")
            for i in range(0, len(listed_item)):
                print(listed_item[i])
            print(f"\n")
        else:
            print(f"\n\n*******Invalid Direction Please Select Again\n{player1.current_room}")
            print("Available Items in this Room:")
            for i in range(0, len(listed_item)):
                print(listed_item[i])
    else:
        print("Invalid Selection: Please try again")

    user = input("[n] North  [s] South  [e] East  [w] West  [q] Quit\n")
