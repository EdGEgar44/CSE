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

home_D = Room("Home Depot", None, None, None, 'TARGET', None,
              "You have reached Walmart. You don't want to go inside because it you have nothing to do in \n"
              "their. To the East is the left of mall and to the West is Target.")

walmart = Room("Walmart", None, 'NORTHHOUSE', None, 'Target', None,
               "You have reached Walmart. You don't want to go inside because it you have nothing to do in \n"
               "their. To the East is the left of mall and to the West is Target.")

cave = Room("The Bat Cave", None, None, 'PARKING', None, None,
            "You have reached the bat cave but no one is here. It is strange that no one whn their is a \n"
            "full parking lot. To the South is the parking lot.")

side_entrance = Room("Side Entrance of the House", 'OREO_FACTORY', 'FRONT_STORE', 'KITCHEN', 'HALL', None,
                     "You have reached the side entrance of the house. You enter the creepy house. To the North \n"
                     "their is a Oreo cookie factory, to the East is the front of the store, to the South is the \n"
                     "kitchen and to the West is the hallway.")

kitchen = Room("Kitchen", 'SIDE_ENTRANCE', None, None, 'LIVING_R', None,
               "You have reached the kitchen. You don't see anything but a bunch of cabinets. To the North \n"
               "is the side entrance of the house and to the West is the living room.")

living_R = Room("Living Room", 'HALL', 'KITCHEN', None, 'CORRIDOR', None,
                "You reached the living room. There seem to be a maze with the couches. You pass the maze. To\n"
                "the North is the hallway, to the East is the kitchen and to the West is a corridor.")

corridor = Room("Left Corridor", 'TROPHY_R', 'LIVING_R', 'SHRINE_R', 'DARK_R', None,
                "You find yourself in a cross way inside the house. There is a door that is slightly open \n"
                "that seems to have something bright coming from the room, to the East is the living room, \n"
                "to the South is a bookshelf with books about God and to the West is a room that is dark inside.")

trophy_R = Room("Trophy Room", None, None, 'CORRIDOR', None, None,
                "You find yourself in a room filled with trophy's. You see trophy's of Swimming, Cross \n"
                "Country, Football and Soccer. There are also some posters that are all around the room \n"
                "that are athletes. All you can go is South to the corridor.")

shrine_R = Room("Shrine Room", 'CORRIDOR', None, 'SOUTH_HOUSE', None, None,
                "You push the bookshelf to find out that it is a hidden door. You found a room that seems to\n"
                "be a shrine. You see a picture of a boy that seems to be around 20 years old. You see food, \n"
                "drinks, and candles that have cobwebs around them. To the North is the secret bookshelf door \n"
                "that leads to the corridor and to the South it seems to lead outside.")

south_house = Room("South of House", 'SHRINE_R', None, None, None, None,
                   "You open the door to the outside and you you see a torch that is just sitting their. It \n"
                   "fills you up with hope just to remember that you are all alone in this town. To the North \n"
                   "is the shrine room.")
