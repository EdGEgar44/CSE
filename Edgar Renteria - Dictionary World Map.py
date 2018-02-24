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
            'NORTHE': 'CORRUPTED_S',
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
                       "their is a Oreo cookie factory, to the East is the front of the store, to the South is the \n"
                       "kitchen and to the West is the hallway.",
        'PATHS': {
            'NORTH': 'OREO_FACTORY',
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
            'NORTH': 'BOOK_SECTION',
            'EAST': 'SCHOOL_HOUSE'
        }
    },
    'SCHOOL_HOUSE': {
        'NAME': "School House",
        'DESCRIPTION': "You reached the front of a small school house that looks like it was from the 1800's. You \n"
                       "try to open the door but it is locked. You try to find another way in but their isn't. \n"
                       "inside seems to be some desk that has a computer that is unreachable. On the screen it \n"
                       "says 'THE MAP' in big letters. But because it was so far away that you couldn't read what \n"
                       "was below it. So you leave it light that. To the West is the back of the store.",
        'PATHS': {
            'WEST': 'BACK_STORE'
        }
    },
    'OREO_FACTORY': {
        'NAME': "The Oreo Cookie Factory",
        'DESCRIPTION': "You reached the ever so popular Oreo cookie factory. You go inside and you find packs among \n"
                       "packs of double stuffed Oreo's. You grab two packs of double stuffed Oreo's (not that it \n"
                       "matters) so that you have some on the road. You leave the Oreo factory and you walk out \n"
                       "the door. Then you notice a pack of mega stuffed oreo's. You take it and you walk back \n"
                       "outside. To the East is the back of the mall and to the South is the side entrance to a \n"
                       "scary looking house.",
        'PATHS': {
            'EAST': 'BACK_MALL',
            'SOUTH': 'SIDE_ENTRANCE'
        }
    },
    'FRONT_HOUSE': {
        'NAME': "The Front of the House",
        'DESCRIPTION': "You are at the front of the house. You knock on the door to see if anyone is their. No one \n"
                       "answers so you just open the door. You see that the door isn't unlocked. You open the door, \n"
                       "enter the house and closed the door. To the North is the parking lot and to the South is the \n"
                       "hallway.",
        'PATHS': {
            'NORTH': 'HALL',
            'WEST': 'PARKING_LOT'
        }
    },
    'LEFT_MALL': {
        'NAME': "Left of Mall",
        'DESCRIPTION': "You reach the left side of the mall. You see trash cans that don't have anything. You look \n"
                       "inside and their seems to be a graffiti that says 'He is near'. You get out of the garbage \n"
                       "bin and you think for a bit. You wonder why they put that their. To the South is an alley \n"
                       "and to the West is Walmart.",
        'PATHS': {
            'SOUTH': 'ALLEYWAY',
            'WEST': 'WALMART'
        }
    },
    'ALLEYWAY': {
        'NAME': "The Alleyway",
        'DESCRIPTION': "You reach an alleyway. Their isn't much that is here other than a piece of paper with a \n"
                       "clown, a bear, a ballerina, and a puppet. You see that it familiar in a way but you couldn't \n"
                       "place it. To the North is the left of the mall, to the East is a Casino and to the South \n"
                       "seems to have a garbage truck parked outside.",
        'PATHS': {
            'NORTH': 'LEFT_MALL',
            'EAST': 'CASINO',
            'SOUTH': 'GARBAGE TRUCK'
        }
    },
    'CASINO': {
        'NAME': "The Casino",
        'DESCRIPTION': "You reach the Casino's entrance. You can't enter the casino because you are not 18 years or \n"
                       "older. So you just wait outside as you hear slot machines ringing to announce the winner and \n"
                       "hear people talking. To the East is a door that is floating. You don't know how but it is.\n"
                       "In front of the door has a sign that reads 'you need a key. You that walks and can talk.' \n"
                       "Have you seen a key that can do that? To the South is a restaurant and to the West is the \n"
                       "alleyway.",
        'PATHS': {
            'EASTtr': 'TELEPORTER_R',
            'SOUTH': '5_STAR_RESTAURANT',
            'WEST': 'ALLEYWAY'
        }
    },
    'GARBAGE_TRUCK': {
        'NAME': "The Garbage Truck",
        'DESCRIPTION': "You reached the Garbage truck. When you reach their, you see that the passenger seat s open. \n"
                       "You enter the garbage truck and their seems to be a key of some sort. Their is also a piece \n"
                       "of paper that has some writing on it. To the North is the alleyway and to the East is a \n"
                       "restaurant.",
        'PATHS': {
            'NORTH': 'ALLEYWAY',
            'EAST': '5_STAR_RESTAURANT'
        }
    },
    '5_STAR_RESTAURANT': {
        'NAME': "The 5 star Restaurant",
        'DESCRIPTION': "You reached the 5 star restaurant. You feel hungry but you put that feeling away since you \n"
                       "you don't have any money. To the North is a Casino, to the South seems to be a corner and \n"
                       "to the west is a garbage truck.",
        'PATHS': {
            'NORTH': 'CASINO',
            'SOUTH': 'CORNER',
            'WEST': 'GARBAGE_TRUCK'
        }
    },
    'CORNER': {
        'NAME': "The Corner",
        'DESCRIPTION': "You reached the corner of the 5 star restaurant and you turn. You see a chinese restaurant \n"
                       "that seems to be abandoned because of its location. You see that the walls are being torn \n"
                       "by the weather and the windows are broken. To the North is the 5 star restaurant and to the \n"
                       "West is the chinese restaurant.",
        'PATHS': {
            'NORTH': '5_STAR_RESTAURANT',
            'EAST': 'CHINESE_RESTAURANT'
        }
    },
    'CHINESE_RESTAURANT': {
        'NAME': "The Abandoned Chinese Restaurant",
        'DESCRIPTION': "You reached the abandoned chinese restaurant and you go inside. You see that the their was a \n"
                       "a lot of people that use to go here because of so any tables and chairs. You see burn marks \n"
                       "on the wall and you wonder if their was a fire. To the West is the corner of the 5 star \n"
                       "restaurant",
        'PATHS': {
            'WEST': 'CORNER'
        }
    },
    'TELEPORTER_R': {
        'NAME': "The Teleporter Room",
        'DESCRIPTION': "You enter the door that was floating bit because you hold the key near it stopped floating \n"
                       "and reached the floor. You put the key in the key hole and the door opens. You take the key \n"
                       "and you go inside. Inside seems to have a bunch of wire and a pod in the middle. The pod had \n"
                       "a name. The name was 'The Teleporter 9000'. Their was also a command center but you didn't \n"
                       "touch it. To the West is the casino.",
        'PATHS': {
            'WEST': 'CASINO'
        }
    },
    'SERVER': {
        'NAME': "The Server",
        'DESCRIPTION': "You feel dazed because of 'The Teleporter 9000'. You try to walk but you can't. Then you see \n"
                       "a door to the west that is slightly open. You see blue light flickering true the bottom of \n"
                       "the door. But then you see that their is a sight that dose not very much glows. It reads \n"
                       "'YOU SHOULD NOT ENTER. IF YOU ENTER. YOU WILL CRASH THE WORLD AND He WILL COME. IF YOU ENTER \n"
                       "WITHOUT THE PROPER MATERIALS. YOU WILL DIE. DON'T SAY YOU WEREN'T WORDED'. You wonder if you \n"
                       "have the pieces.",
        'PATHS': {
            'WEST': 'CORRUPTED_S'
        }
    },
    'CORRUPTED_R': {
        'NAME': "The Corrupted Server",
        'DESCRIPTION': "When you reach the door you felt a weired feeling when you entered the room. Their was light \n"
                       "on the walls that wre in a patter like a circuit board. They slowly started to glow red. To \n"
                       "the North wall is a door that has a sign that reads 'To the Server'. To the East is to the \n"
                       "server room.",
        'PATHS': {
            'EAST': 'SERVER'
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
