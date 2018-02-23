class Room(object):
    def __init__(self, name, north, east, south, west, item, description):
        self.name = name
        self.description = description
        self.item = item
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
back_mall = Room("Back of the Mall", 'TARGET', None, 'FRONT_STORE', None, None,
                 "You are in the back of the mall. You see Target in the North and the front of a store to the \n "
                 "south.")

front_store = Room("Back Of Mall", 'BACK_MALL', 'WOODWORK_SECTION', None, 'SIDE_ENTRANCE', None,
                   "The store is a convenient store that has been here for a while. To the North is the back of \n a "
                   "mall, to the East is the Woodwork section, and to the West is an entrance to an abandoned \n house."
                   "")

target = Room("Target", 'WALMART', 'HOME_D', 'BACK_MALL', 'OFFICE_D', None,
              "You have entered Target and walked through. You have triggered the metal detector and was \n kicked out"
              "of the store. Walmart is in the North, Home Depot is in the East, Office Depot \n is in the West, and"
              "to the South is the back of the mall.")

office_D = Room("Office Depot", 'APPLE', 'HOME_D', None, 'CAR', None,
                "You have entered Office Depot and didn't want to go thought because of what happened with \n Target."
                "To the West is Target and to the East is the left of the mall.")

car = Room("The Car", None, 'OFFICE_D', None, 'PARKING', None,
           "You found your car. But you left your keys in an unknown area, so you can't get in. To the \n East is"
           "Office Depot and to the West in the Parking lot.")

parking = Room("Parking Lot", 'CAVE', 'CAR', 'FRONT_HOUSE', 'TRUCK', None,
               "You have reached the parking lot. Their are a lot of cars in the parking lot to visit the \n bat cave."
               "To the North is the bat cave, to the East is were your car is at, to the South is \n the front of a"
               "house and to the west is a taco truck.")

truck = Room("Taco Truck", None, 'PARKING', None, None, None,
             "You smell a the tacos that are in the truck. You want to buy a taco because you are hungry \n but you"
             "don't have any money. To the East is the parking lot.")

apple = Room("The Apple Store", 'SERVER_R', None, 'OFFICE_D', None, None,
             "You have reached the famous store from the Apple company. You want to go in but you don't \n have any"
             "intentions their. To the North is a fence that is locked with unbreakable chains \n with a lock on a door"
             "that doesn't look like a normal key. To the South is Office Depot.")
