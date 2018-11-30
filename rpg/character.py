class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        """Prints a string describing the character to the console"""
        print(self.name + " is here!")
        print(self.description)

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """Sets the conversation attribute of the character to the given string"""
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        """Prints the conversation string of the character to the console"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        """Returns True and prints string about fight message to console"""
        print(self.name + " doesn't want to fight with you")
        return True


class Enemy(Character):
    dead_enemies: int = 0

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        """Sets a string containing the weekness of the enemy"""
        self.weakness = weakness

    def get_weakness(self):
        """Returns a string containing the weekness of the enemy"""
        return self.weakness

    def fight(self, combat_item):
        """Returns a boolean, True if you won the fight, false otherwise"""
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            Enemy.dead_enemies += 1
            print(Enemy.dead_enemies)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def get_dead_enemies(self):
        """Returns an int reflecting the number of dead enemies"""
        return self.dead_enemies


class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.hugReady = True

    def hug(self):
        """Returns a boolean, True if Character wants to be hugged, False otherwise"""
        if self.hugReady:
            print(self.name + " hugs you!")
            return True
        else:
            print(self.name + " does not hug you!")
            return False
