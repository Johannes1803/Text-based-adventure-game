class Room:

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None

    def set_description(self, room_description):
        """Sets the description of the room as a string"""
        self.description = room_description

    def get_description(self):
        """Returns a string containing the description of the room"""
        return self.description

    def set_name(self, name):
        """ Sets the name of the room as a string"""
        self.name = name

    def get_name(self):
        """Returns a string containing the name of the room"""
        return self.name

    def describe(self):
        """Prints a string describung the room to the console"""
        print(self.description)

    def link_room(self, room_to_link, direction):
        """Links the room the other room given as input in the specified direction, """
        self.linked_rooms[direction] = room_to_link
        # print(self.name + " linked rooms :" + repr(self.linked_rooms))

    def get_details(self):
        """Returns a string describing the linked rooms and their directions"""
        self.describe()
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        """Returns the room in the given direction, or returns the current room if there is no such room"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You cant go that way")
            return self

    def set_character(self, character):
        """Sets the Character object in the room"""
        self.character = character

    def get_character(self):
        """Returns the character object in the room"""
        return self.character

    def set_item(self, item):
        """Sets the item object in the room"""
        self.item = item

    def get_item(self):
        """Returns the item object in the room"""
        return self.item
