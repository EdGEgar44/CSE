class Room(object):
    def __init__(self, name, description, item, north, east, south, west):
        self.name = name
        self.description = description
        self.item = item
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def item(self):

