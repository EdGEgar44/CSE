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

dark_R = Room("The Dark Room", 'SCARY_R', 'CORRIDOR', None, 'WEST_HOUSE', None,
              "You reached a dark room. You can't see anything in the room. Yo felt something in the back \n"
              "of your leg. It feels like a camera. You hear scary sounds in the room to the North, to the \n"
              "East is the corridor and to the West you hear birds chirping.")

scary_R = Room("Scary Room", None, None, 'DARK_R', None, None,
               "You enter the scary room  to find that the monitor of a computer was on. It was playing \n"
               "scary music from Youtube. You wonder why you they will leave it running. Then you see a key \n"
               "that came shooting out of the wall behind a painting. It is a key. A shiny blue key that \n"
               "says 'P key 2 KEEP HIDDEN'. You wonder why they didn't take it. To the South is the scary \n"
               "room.")

west_house = Room("West of House", None, 'DARK_R', None, None, None,
                  "You leave the house and reached the west side of the house. You can't go anywhere because \n"
                  "it is surrounded by bushed and thick trees. The only way you can go is to the dark room to \n"
                  "the East.")

woodwork_section = Room("Woodwork section", None, None, 'WALKWAY', 'FRONT_STORE', None,
                        "You go to the woodwork section. Their is a lot of wood that has been cut down and but into \n"
                        "To the South is a Walkway and to the West is the front of the store.")

walkway = Room("Walkway", 'WOODWORK_SECTION', 'BOX_R', 'BOOK_SECTION', None, None,
               "You find yourself in the walkway of the store. You find yourself in a three-section. To the \n"
               "North is the woodwork section, to the East is the box room and to the South is the book \n"
               "section.")

box_R = Room("The Box Room", None, 'WALKWAY', None, 'MEAT_SECTION', None,
             "You enter the box room that seems to be for employee only. The only thing that is in the \n"
             "room are boxes. Boxes. And more boxes. boxes with wood and books. To the East is the Meet \n"
             "section and to the West is the walkway.")

meat_section = Room("Meat Section", None, None, 'MIRROR_R', 'BOX_R', None,
                    "You reach the meat section of the store. It was all empty but the cow meat section. You \n"
                    "want to take the meat but you don't because it is stealing. To the South is a room full \n"
                    "of mirrors and to the West is the box room.")

mirror_R = Room("Mirror Room", 'MEAT_SECTION', 'THE_ROOM', None, None, None,
                "You have reached the mirror room and all you see is yourself. ou seemed like you have seen \n"
                "better days. You have baggy clothes and you have shorts. To the North is the meat section \n"
                "and to the East in a door with a caption 'The Room'")

the_room = Room("The Room", None, None, 'MIRROR_R', None, None,
                "You enter the mysterious room called the room. You can't see a lot of things since the room \n"
                "is dimly lit. All you can really see is that people have been here. It is all messy as if \n"
                "they were looking for something. They probably found it or game up since they was a corner \n"
                "of the room that was neat and clean. To the West is the Mirror room.")

book_section = Room("Book Section", 'WALKWAY', None, 'BACK_STORE', 'CLOTHING_SECTION', None,
                    "You reach the book section of the store. You see famous books in the 'Famous book section'. \n"
                    "Their were books from the 'Harry Potter' series and the books series of 'Percy Jackson and \n"
                    "the Olympians'. To the North is the Walkway, to the South is a door that is leading outside \n"
                    "and to the West is the clothing section.")

clothing_section = Room("Clothing Section", None, 'BOOK_SECTION', None, None, None,
                        "You reach the clothing section. You see lines of clothes missing. The only thing you see \n"
                        "is armor that seems to fit you. It seems to be made out of chain mail armor. To the East \n"
                        "is the book section of the store.")

back_store = Room("Back of Store", 'BOOK_SECTION', 'SCHOOL_HOUSE', None, None, None,
                  "You reached the back of the store. You see a garbage can that is full of trash. You see a \n"
                  "graffiti that says 'HE CAME'. What that meant was a mystery. To the North is the book \n"
                  "section and to the East is a school House.")

school_house = Room("School House", None, None, 'BACK_STORE', None, None,
                    "You reached the front of a small school house that looks like it was from the 1800's. You \n"
                    "try to open the door but it is locked. You try to find another way in but their isn't. \n"
                    "inside seems to be some desk that has a computer that is unreachable. On the screen it \n"
                    "says 'THE MAP' in big letters. But because it was so far away that you couldn't read what \n"
                    "was below it. So you leave it light that. To the West is the back of the store.")

oreo_factory = Room("The Oreo Cookie Factory", None, 'BACK_MALL', 'SIDE_ENTRANCE', None, None,
                    "You reached the ever so popular Oreo cookie factory. You go inside and you find packs among \n"
                    "packs of double stuffed Oreo's. You grab two packs of double stuffed Oreo's (not that it \n"
                    "matters) so that you have some on the road. You leave the Oreo factory and you walk out \n"
                    "the door. Then you notice a pack of mega stuffed oreo's. You take it and you walk back \n"
                    "outside. To the East is the back of the mall and to the South is the side entrance to a \n"
                    "scary looking house.")

front_house = Room("The Front of the House", 'HALL', None, None, 'PARKING_LOT', None,
                   "You are at the front of the house. You knock on the door to see if anyone is their. No one \n"
                   "answers so you just open the door. You see that the door isn't unlocked. You open the door, \n"
                   "enter the house and closed the door. To the North is the parking lot and to the South is the \n"
                   "hallway.")

left_mall = Room("Left of Mall", None, None, 'ALLEYWAY', 'WALMART', None,
                 "You reach the left side of the mall. You see trash cans that don't have anything. You look \n"
                 "inside and their seems to be a graffiti that says 'He is near'. You get out of the garbage \n"
                 "bin and you think for a bit. You wonder why they put that their. To the South is an alley \n"
                 "and to the West is Walmart.")

alleyway = Room("The Alleyway", 'LEFT_MALL', 'CASINO', 'GARBAGE TRUCK', None, None,
                "You reach an alleyway. Their isn't much that is here other than a piece of paper with a \n"
                "clown, a bear, a ballerina, and a puppet. You see that it familiar in a way but you couldn't \n"
                "place it. To the North is the left of the mall, to the East is a Casino and to the South \n"
                "seems to have a garbage truck parked outside.")

casino = Room("The Casino", None, None, 'RESTAURANT', 'ALLEYWAY', None,
              "You reach the Casino's entrance. You can't enter the casino because you are not 18 years or \n"
              "older. So you just wait outside as you hear slot machines ringing to announce the winner and \n"
              "hear people talking. To the East is a door that is floating. You don't know how but it is.\n"
              "In front of the door has a sign that reads 'you need a key. You that walks and can talk.' \n"
              "Have you seen a key that can do that? To the South is a restaurant and to the West is the \n"
              "alleyway.")

garbage_truck = Room("The Garbage Truck", 'ALLEYWAY', 'STAR_RESTAURANT', None, None, None,
                     "You reached the Garbage truck. When you reach their, you see that the passenger seat s open. \n"
                     "You enter the garbage truck and their seems to be a key of some sort. Their is also a piece \n"
                     "of paper that has some writing on it. To the North is the alleyway and to the East is a \n"
                     "restaurant.")

restaurant = Room("The 5 star Restaurant", 'CASINO', None, 'CORNER', 'GARBAGE_TRUCK', None,
                  "You reached the 5 star restaurant. You feel hungry but you put that feeling away since you \n"
                  "you don't have any money. To the North is a Casino, to the South seems to be a corner and \n"
                  "to the west is a garbage truck.")

corner = Room("The Corner", 'RESTAURANT', 'CHINESE_RESTAURANT', None, None, None,
              "You reached the corner of the 5 star restaurant and you turn. You see a chinese restaurant \n"
              "that seems to be abandoned because of its location. You see that the walls are being torn \n"
              "by the weather and the windows are broken. To the North is the 5 star restaurant and to the \n"
              "West is the chinese restaurant.")

chinese_restaurant = Room("The Abandoned Chinese Restaurant", None, None, 'CORNER', None, None,
                          "You reached the abandoned chinese restaurant and you go inside. You see that the their was"
                          "\n a lot of people that use to go here because of so any tables and chairs. You see burn "
                          "marks \n on the wall and you wonder if their was a fire. To the West is the corner of "
                          "the 5 star \n restaurant")

teleporter_R = Room("The Teleporter Room", None, None, None, 'CASINO', None,
                    "You enter the door that was floating bit because you hold the key near it stopped floating \n"
                    "and reached the floor. You put the key in the key hole and the door opens. You take the key \n"
                    "and you go inside. Inside seems to have a bunch of wire and a pod in the middle. The pod had \n"
                    "a name. The name was 'The Teleporter 9000'. Their was also a command center but you didn't \n"
                    "touch it. To the West is the casino.")

server = Room("The Server", None, None, None, 'CORRUPTED_R', None,
              "You feel dazed because of 'The Teleporter 9000'. You try to walk but you can't. Then you see \n"
              "a door to the west that is slightly open. You see blue light flickering true the bottom of \n"
              "the door. But then you see that their is a sight that dose not very much glows. It reads \n"
              "'YOU SHOULD NOT ENTER. IF YOU ENTER. YOU WILL CRASH THE WORLD AND He WILL COME. IF YOU ENTER \n"
              "WITHOUT THE PROPER MATERIALS. YOU WILL DIE. DON'T SAY YOU WEREN'T WORDED'. You wonder if you \n"
              "have the pieces.")

corrupted_server = Room("The Corrupted Server", 'CORRUPTED_R', 'SERVER', None, None, None,
                        "When you entered the room you felt a weired feeling in your stomach. Their was light on the \n"
                        "walls that wre in a patter like a circuit board. They slowly started to glow red. To the \n"
                        "North wall is a door that has a sign that reads 'To the Server'. To the East is to the \n"
                        "server room.")

corrupted_R = Room("Corrupted Server", 'REFLECTIVE_R', None, 'CORRUPTED_R', None, None,
                   "You entered the door to the server room. Then you hear alarm bearing. The room turned red. \n"
                   "Then a speaker spoke, 'The World has been corrupted'.The speaker spoke that over and over. \n"
                   "Your ears. You try to find the panel for the speaker but it is not here. You must find it in \n"
                   "order to stop the speaker. To the North is a room filled with mirrors. You don't know why \n"
                   "their filled with mirrors, but they are. To the South is the corrupted room.")

reflective_R = Room("The Reflective Room", None, None, 'CORRUPTED_SERVER', 'COMPUTER_R', None,
                    "You enter the reflective room. Since you haven't found the panel to the speaker, you haven't \n"
                    "turned off the speaker or the blaring red light. So the mirrors is mostly reflecting red \n"
                    "light. To the South is the corrupted server and to the West is a room filled with complicated \n"
                    "electronics.")

# computer_R = Room()

# stone_library = Room()

# garden = Room()

# castle_kitchen = Room()

# magic_library = Room()

# waterfall_R = Room()

# mine_shaft = Room()

# cavern = Room()

# looper = Room()

# throne_room = Room()

# rainbow_R = Room()

# blood_moon_R = Room()

# section_3 = Room()

# castle_entrance = Room()

# light_R = Room()

# bo_bo = Room()

# Forgotten_R = Room()

# puzzle_R = Room()

items = ["TR Key", "P Key 1", "P Key 2", "P Key 3", "P Key 4", "Camera", "Paper", "Armor", "Candle", "Torch",
         "Pickaxe", "Rainbow in a Bottle"]

current_node = back_mall
directions = ['north', 'east', 'south', 'west']
short_directions = ['n', 'e', 's', 'w']

while True:
    print(current_node.name)
    print()
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Looking for which command we typed in
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node = current_node.move(command)
        except KeyError:
            print("Command not recognize")
            print()
    else:
        print("Command not recognize")
