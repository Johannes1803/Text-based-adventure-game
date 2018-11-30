class Item():
    def __init__(self, name):
        self.name = name
        self.description = None

    def set_name(self, name):
        """Sets the name attribute of the item to the given String"""
        self.name = name

    def get_name(self):
        """returns a string containing the name of the item"""
        return self.name

    def set_description(self, description):
        """Sets the description attribute of the item to the given String"""
        self.description = description

    def get_description(self):
        """Returns a string containing the description of the item"""
        return self.description

    def describe(self):
        """Prints a string describing the item to the console"""
        print(self.get_name())
        print(self.get_description())
