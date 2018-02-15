world_map = {
    'BACK_MALL': {
        'NAME': "Back Of Mall",
        'DESCRIPTION': "You are in the back of the mall. You see Target in the North and the front of a store to the \n"
                       "south.",
        'PATHS': {
            'NORTH': 'TARGET',
            'SOUTH': 'FRONT_STORE'
        }
    },
    'FRONT_STORE': {
        'NAME': "The Front of a store",
        'DESCRIPTION': "The store is a convenient store that has been here for a while. To the North is the back of \n"
                       "a mall, to the East is the Woodwork section, and to the West is an entrance to an abandoned \n"
                       "house.",
        'PATHS': {
            'NORTH': 'BACK_MALL',
            'EAST': 'WOODWORK_SECTION',
            'WEST': 'SIDE_ENTRANCE'
        }
    },
    'TARGET': {
        'NAME': "Target",
        'DESCRIPTION': "You have entered Target and walked through. You have triggered the metal detector and was \n"
                       "kicked out of the store. Walmart is in the North, Home Depot is in the East, Office Depot \n"
                       "is in the West, and to the South is the back of the mall.",
        'PATHS': {
            'NORTH': 'WALMART',
            'EAST': 'HOME_D',
            'SOUTH': 'BACK_MALL',
            'WEST': 'OFFICE_D'
        }
    },
    'OFFICE_D': {
        'NAME': "Office Depot",
        'DESCRIPTION': "You have entered Office Depot and didn't want to go thought because of what happened with \n"
                       "Target. To the West is Target and to the East is the left of the mall.",
        'PATHS': {
            'NORTH': 'APPLE',
            'EAST': 'HOME_D',
            'WEST': 'CAR'
        }
    },
    'CAR': {
        'NAME': "The Car",
        'DESCRIPTION': "You found your car. But you left your keys in an unknown area, so you can't get in. To the \n"
                       "East is Office Depot and to the West in the Parking lot.",
        'PATHS': {
            'EAST': 'OFFICE_D',
            'WEST': 'PARKING'
        }
    },
    'PARKING': {
        'NAME': "Parking Lot",
        'DESCRIPTION': "You have reached the parking lot. Their are a lot of cars in the parking lot to visit the \n"
                       "bat cave. To the North is the bat cave, to the East is were your car is at, to the South is \n"
                       "the front of a house and to the west is a taco truck.",
        'PATHS': {
            'NORTH': 'CAVE',
            'EAST': 'CAR',
            'SOUTH': 'FRONT_HOUSE',
            'WEST': 'TRUCK'
        },
    },
    'TRUCK': {
        'NAME': "Taco Truck",
        'DESCRIPTION': "You smell a the tacos that are in the truck. You want to buy a taco because you are hungry \n"
                       "but you don't have any money. To the East is the parking lot.",
        'PATHS': {
            'EAST': 'PARKING'
        }
    },
    'APPLE': {
        'NAME': "The Apple Store",
        'DESCRIPTION': "You have reached the famous store from the Apple company. You want to go in but you don't \n"
                       "have any intentions their. To the North is a fence that is locked with unbreakable chains \n"
                       "with a lock on a door that doesn't look like a normal key. To the South is Office Depot.",
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'OFFICE_D'
        }
    },
    'HOME_D': {
        'NAME': "Home Depot",
        'DESCRIPTION': "You have reached Home Depot. You go inside. But nothing in the store that you want. So you \n"
                       "go outside. To the West is Target.",
        'PATHS': {
            'WEST': 'TARGET'
        }
    },
    'WALMART': {
        'NAME': "Walmart",
        'DESCRIPTION': "You have reached Walmart. You don't want to go inside because it you have nothing to do in \n"
                       "their. To the East is the left of mall and to the West is Target.",
        'PATHS': {
            'EAST': 'NORTHHOUSE',
            'WEST': 'Target'
        }
    },
    'Cave': {
        'NAME': "The Bat Cave",
        'DESCRIPTION': "You have reached the bat cave but no one is here. It is strange that no one whn their is a \n"
                       "full parking lot. To the South is the parking lot.",
        'PATHS': {
            'SOUTH': 'PARKING'
        }
    },
    'SIDE_ENTRANCE': {
        'NAME': "Side Entrance of the House",
        'DESCRIPTION': "You have reached the side entrance of the house. You enter the creepy house. To the North \n"
                       "their is a cupcake factory, to the East is the front of the store, to the South is the \n"
                       "kitchen and to the West is the hallway.",
        'PATHS': {
            'NORTH': 'FACTORY',
            'EAST': 'FRONT_STORE',
            'SOUTH': 'KITCHEN',
            'WEST': 'HALL'
        }
    },
    'KITCHEN': {
        'NAME': "Kitchen",
        'DESCRIPTION': "You have reached the kitchen. You don't see anything but a bunch of cabinets. To the North \n"
                       "is the side entrance of the house and to the West is the living room.",
        'PATHS': {
            'NORTH': 'SIDE_ENTRANCE',
            'WEST': 'LIVING_R'
        }
    },
    'LIVING_R': {
        'NAME': "Living Room",
        'DESCRIPTION': "You reached the living room. There seem to be a maze with the couches. You pass the maze. To\n"
                       "the North is the hallway, to the East is the kitchen and to the West is a corridor.",
        'PATHS': {
            'NORTH': 'HALL',
            'EAST': 'KITCHEN',
            'WEST': 'CORRIDOR'
        }
    },
    'CORRIDOR': {
        'NAME': "Left Corridor",
        'DESCRIPTION': "You find yourself in a cross way inside the house. There is a door that is slightly open \n"
                       "that seems to have something bright coming from the room, to the East is the living room, \n"
                       "to the South is a bookshelf with books about God and to the West is a room that is dark inside"
                       ".",
        'PATHS': {
            'NORTH': 'TROPHY_R',
            'EAST': 'LIVING_R',
            'SOUTH': 'SHRINE_R',
            'WEST': 'DARK_R'
        }
    },
    'TROPHY_R': {
        'NAME': "Trophy Room",
        'DESCRIPTION': " You find yourself in a room filled with trophy's. You see trophy's of Swimming, Cross \n"
                       "Country, Football and Soccer. There are also some posters that are all around the room \n"
                       "that are athletes. All you can go is South to the corridor.",
        'PATHS': {
            'SOUTH': 'CORRIDOR'
        }
    },
    'SHRINE_R': {
        'NAME': "Shrine Room",
        'DESCRIPTION': "You found a room that seems to be a shrine. You see a picture of a boy that seems to be \n"
                       "around 20 years old. You see food, drinks, and candles that have cobwebs around them. To \n"
                       "the North is the secret bookshelf door that leads to the corridor and to the South it seems \n"
                       "to lead outside.",
        'PATHS': {
            'NORTH': 'CORRIDOR',
            'SOUTH': 'SOUTH_HOUSE'
        }
    },
    'SOUTH_HOUSE': {
        'NAME': "South of House",
        'DESCRIPTION': "You open the door to the outside and you you see a torch that is just sitting their. It \n"
                       "fills you up with hope just to remember that you are all alone in this town. To the North \n"
                       "is the shrine room.",
        'PATHS': {
            'NORTH': 'SHRINE_R'
        }
    },
    'DARK_R': {
        'NAME': "The Dark Room",
        'DESCRIPTION': "You reached a dark room. You can't see anything in the room. You hear scary sounds in the \n"
                       "room to the North, to the East is the corridor and to the West you hear birds chirping.",
        'PATHS': {
            'NORTH': 'SCARY_R',
            'EAST': 'CORRIDOR',
            'WEST': 'WEST_HOUSE'
        }
    },
    '': {
        'NAME': "",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': 'TROPHY_R',
            'EAST': 'LIVING_R',
            'SOUTH': 'SHRINE_R',
            'WEST': 'DARK_R'
        }
    },

}

current_node = world_map['BACK_MALL']
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

while True:
    print(current_node['NAME'])
    print()
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("Command not recognize")
            print()
    else:
        print("Command not recognize")
