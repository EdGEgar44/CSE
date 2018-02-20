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
        'DESCRIPTION': "You push the bookshelf to find out that it is a hidden door. You found a room that seems to\n"
                       "be a shrine. You see a picture of a boy that seems to be around 20 years old. You see food, \n"
                       "drinks, and candles that have cobwebs around them. To the North is the secret bookshelf door \n"
                       "that leads to the corridor and to the South it seems to lead outside.",
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
        'DESCRIPTION': "You reached a dark room. You can't see anything in the room. Yo felt something in the back \n"
                       "of your leg. It feels like a camera. You hear scary sounds in the room to the North, to the \n"
                       "East is the corridor and to the West you hear birds chirping.",
        'PATHS': {
            'NORTH': 'SCARY_R',
            'EAST': 'CORRIDOR',
            'WEST': 'WEST_HOUSE'
        }
    },
    'SCARY_R': {
        'NAME': "Scary Room",
        'DESCRIPTION': "You enter the scary room  to find that the monitor of a computer was on. It was playing \n"
                       "scary music from Youtube. You wonder why you they will leave it running. Then you see a key \n"
                       "that came shooting out of the wall behind a painting. It is a key. A shiny blue key that \n"
                       "says 'P key 2 KEEP HIDDEN'. You wonder why they didn't take it. To the South is the scary \n"
                       "room.",
        'PATHS': {
            'SOUTH': 'DARK_R'
        }
    },
    'WEST_HOUSE': {
        'NAME': "West of House",
        'DESCRIPTION': "You leave the house and reached the west side of the house. You can't go anywhere because \n"
                       "it is surrounded by bushed and thick trees. The only way you can go is to the dark room to \n"
                       "the East.",
        'PATHS': {
            'EAST': 'DARK_R'
        }
    },
    'WOODWORK_SECTION': {
        'NAME': "Woodwork section",
        'DESCRIPTION': " You go to the woodwork section. Their is a lot of wood that has been cut down and but into \n"
                       "To the South is a Walkway and to the West is the front of the store.",
        'PATHS': {
            'SOUTH': 'WALKWAY',
            'WEST': 'FRONT_STORE'
        }
    },
    'WALKWAY': {
        'NAME': "Walkway",
        'DESCRIPTION': "You find yourself in the walkway of the store. You find yourself in a three-section. To the \n"
                       "North is the woodwork section, to the East is the box room and to the South is the book \n"
                       "section.",
        'PATHS': {
            'NORTH': 'WOODWORK_SECTION',
            'EAST': 'BOX_R',
            'SOUTH': 'BOOK_SECTION'
        }
    },
    'BOX_R': {
        'NAME': "The Box Room",
        'DESCRIPTION': "You enter the box room that seems to be for employee only. The only thing that is in the \n"
                       "room are boxes. Boxes. And more boxes. boxes with wood and books. To the East is the Meet \n"
                       "section and to the West is the walkway.",
        'PATHS': {
            'EAST': 'WALKWAY',
            'WEST': 'MEAT_SECTION'
        }
    },
    'MEAT_SECTION': {
        'NAME': "Meat Section",
        'DESCRIPTION': "You reach the meat section of the store. It was all empty but the cow meat section. You \n"
                       "want to take the meat but you don't because it is stealing. To the South is a room full \n"
                       "of mirrors and to the West is the box room.",
        'PATHS': {
            'SOUTH': 'MIRROR_R',
            'WEST': 'BOX_R'
        }
    },
    'MIRROR_R': {
        'NAME': "Mirror Room",
        'DESCRIPTION': "You have reached the mirror room and all you see is yourself. ou seemed like you have seen \n"
                       "better days. You have baggy clothes and you have shorts. To the North is the meat section \n"
                       "and to the East in a door with a caption 'The Room'",
        'PATHS': {
            'NORTH': 'MEAT_SECTION',
            'EAST': 'THE_ROOM'
        }
    },
    'THE_ROOM': {
        'NAME': "The Room",
        'DESCRIPTION': "You enter the mysterious room called the room. You can't see a lot of things since the room \n"
                       "is dimly lit. All you can really see is that people have been here. It is all messy as if \n"
                       "they were looking for something. They probably found it or game up since they was a corner \n"
                       "of the room that was neat and clean. To the West is the Mirror room.",
        'PATHS': {
            'WEST': 'MIRROR_R'
        }
    },
    'BOOK_SECTION': {
        'NAME': "Book Section",
        'DESCRIPTION': "You reach the book section of the store. You see famous books in the 'Famous book section'. \n"
                       "Their were books from the 'Harry Potter' series and the books series of 'Percy Jackson and \n"
                       "the Olympians'. To the North is the Walkway, to the South is a door that is leading outside \n"
                       "and to the West is the clothing section.",
        'PATHS': {
            'NORTH': 'WALKWAY',
            'SOUTH': 'BACK_STORE',
            'WEST': 'CLOTHING_SECTION'
        }
    },
    'CLOTHING_SECTION': {
        'NAME': "Clothing Section",
        'DESCRIPTION': "You reach the clothing section. You see lines of clothes missing. The only thing you see \n"
                       "is armor that seems to fit you. It seems to be made out of chain mail armor. To the East \n"
                       "is the book section of the store.",
        'PATHS': {
            'EAST': 'BOOK_SECTION'
        }
    },
    'BACK_STORE': {
        'NAME': "Back of Store",
        'DESCRIPTION': "You reached the back of the store. You see a garbage can that is full of trash. You see a \n"
                       "graffiti that says 'HE CAME'. What that meant was a mystery. To the North is the book \n"
                       "section and to the East is a school House.",
        'PATHS': {
            'NORTH': '',
            'EAST': ''
        }
    },
    'SCHOOL_HOUSE': {
        'NAME': "School House",
        'DESCRIPTION': "",
        'PATHS': {
            'WEST': ''
        }
    },
    '': {
        'NAME': " ",
        'DESCRIPTION': " ",
        'PATHS': {
            'NORTH': '',
            'EAST': '',
            'SOUTH': '',
            'WEST': ''
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
