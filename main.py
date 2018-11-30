from rpg.room import Room
from rpg.item import Item
from rpg.character import Enemy, Friend

# number of enemies to defeat before victory
to_be_killed = 2

# Define the map

# define rooms
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

ballroom = Room("Ballroom")
ballroom.set_description("Where we chill, yo!")

dining_hall = Room("Dining hall")
dining_hall.set_description("The room where we eat delicious meals!")

kitchen.link_room(dining_hall, "south")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

current_room = kitchen

# add items
sword = Item("sword")
sword.set_name("excalibur")
# sword.get_name()
sword.set_description("sword of King Arthur")
# sword.get_description()
# put sword in kitchen
kitchen.set_item(sword)

cucumber = Item("Cucumber")
cucumber.set_name("cucumber")
cucumber.set_description("A delicious vegetable!")
dining_hall.set_item(cucumber)
# add a character
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Oink Oink")
dave.set_weakness("excalibur")

# put character dave in dining hall
dining_hall.set_character(dave)
# Add a new enemy
pete = Enemy("Pete", "a nasty wizard")
pete.set_conversation("Hokus Pokus")
pete.set_weakness("cucumber")

ballroom.set_character(pete)

# Add a new character
catrina = Friend("Catrina", "a friendly skeleton")

catrina.set_conversation("Hello there.")
kitchen.set_character(catrina)

dead = False
backpack = []

# the game loop
while not dead:
    print("\n")
    # describe state of room you are in
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_room.get_item()
    if item is not None:
        item.describe()
        backpack.append(item.get_name())
        current_room.set_item(None)
    # listen to user input
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # talk to current inhabitant -check whether there is one
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        # fight with inhabitant if there is one
        if inhabitant is not None:
            print("What will you fight with?")
            fight_with = input()
            # do you have the item you want to fight with in your bag?
            if fight_with in backpack:
                # Fight won?
                won_fight = inhabitant.fight(fight_with)
                if not won_fight:
                    dead = True  # You die. Game over
                else:
                    if inhabitant.get_dead_enemies() >= to_be_killed:
                        print("You win")  # you killed enough enemies to win the game
                        dead = True
                    current_room.set_character(None)
            else:
                print("This item is not in your backpack")
        else:
            print("There is no one here to fight with!")

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("bad Idea")
            elif isinstance(inhabitant, Friend):
                inhabitant.hug()
