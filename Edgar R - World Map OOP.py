class Room(object):
    def __init__(self, name, north, east, south, west, item, description, description_2):
        self.name = name
        self.description = description
        self.description_2 = description_2
        self.item = item
        self.north = north
        self.east = east
        self.south = south
        self.west = west

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Initialize Rooms
BACK_MALL = Room("Back of the Mall", 'TARGET', None, 'FRONT_STORE', None, None,
                 "You are in the back of the mall. You wonder were you are and how you got here. You see Target to \n"
                 "North and the front of a store to the south.",
                 "You are in the back of the mall. You see Target in the North and the front of a store to the \n "
                 "south.")

FRONT_STORE = Room("Front of Store", 'BACK_MALL', 'WOODWORK_SECTION', None, 'SIDE_ENTRANCE', None,
                   "The store is a convenient store that has been here for a while. To the North is the back of \n a "
                   "mall, to the East is the Woodwork section, and to the West is an entrance to an abandoned \n "
                   "house.",
                   "You reached the cashier of the convenient store. To the East is the Woodwork section, and to the \n"
                   "West is an entrance to an abandoned house")

TARGET = Room("Target", 'WALMART', 'HOME_D', 'BACK_MALL', 'OFFICE_D', None,
              "You have entered Target and walked through. You have triggered the metal detector and was \n kicked out"
              "of the store. Walmart is to the North, Home Depot is in the East, Office Depot \n is in the West, and"
              "to the South is the back of the mall.",
              "You are now in front of Target. Walmart is to the North, Home Depot is in the East, Office Depot is \n"
              "to the West, and to the South is the back of the mall.")

OFFICE_D = Room("Office Depot", 'APPLE', 'HOME_D', None, 'CAR', None,
                "You have entered Office Depot and didn't want to go thought because of what happened with Target. \n"
                "To the West is Target and to the East is the left of the mall.",
                "You are outside of Office Depot. To the West is Target and to the East is the left of the mall.")

CAR = Room("The Car", None, 'OFFICE_D', None, 'PARKING', None,
           "You found your car. But you left your keys in an unknown area, so you can't get in. To the East is \n"
           "Office Depot and to the West in the Parking lot.",
           "You are now near you car. To the East is Office Depot and to the West in the Parking lot.")

PARKING = Room("Parking Lot", 'CAVE', 'CAR', 'FRONT_HOUSE', 'TRUCK', None,
               "You have reached the parking lot. Their are a lot of cars in the parking lot to visit the \n bat cave."
               "To the North is the bat cave, to the East is were your car is at, to the South is \n the front of a"
               "house and to the west is a taco truck.",
               "You reached the parking lot fulled with car but with no one around. To the North is the bat cave, to \n"
               "the East is were your car is at, to the South is the front of a house and to the west is a taco truck.")

TRUCK = Room("Taco Truck", None, 'PARKING', None, None, None,
             "You smell a the tacos that are in the truck. You want to buy a taco because you are hungry \n but you"
             "don't have any money. To the East is the parking lot.",
             "You are now near the taco truck. To the East is the parking lot.")

APPLE = Room("The Apple Store", 'SERVER_R', None, 'OFFICE_D', None, None,
             "You have reached the famous store from the Apple company. You want to go in but you don't \n have any"
             "intentions their. To the North is a fence that is locked with unbreakable chains \n with a lock on a door"
             "that doesn't look like a normal key. To the South is Office Depot.",
             "You are now outside of the ever so famous Apple store from Apple.inc. To the North is a fence that is \n"
             "locked with unbreakable chains with a lock on a door that doesn't look like a normal key. To the South \n"
             "is Office Depot.")

HOME_D = Room("Home Depot", None, None, None, 'TARGET', None,
              "You have reached Home Depot. You don't want to go inside because it you have nothing to do in \n"
              "their. You wonder if you could steal something since their is no one around. They wont notice it \n"
              "gone. To the East is the left of mall and to the West is Target.",
              "You reached outside of Home Depot. To the East is the left of mall and to the West is Target.")

WALMART = Room("Walmart", None, 'LEFT_MALL', None, 'Target', None,
               "You have reached Walmart. You don't want to go inside because it you have nothing to do in \n"
               "their. To the East is the left of mall and to the West is Target.",
               "You are now outside of walmart. To the East is the left of mall and to the West is Target.")

CAVE = Room("The Bat Cave", None, None, 'PARKING', None, None,
            "You have reached the bat cave but no one is here. It is strange that no one whn their is a \n"
            "full parking lot. To the South is the parking lot.",
            "You are now outside of the cave. You still wonder why this is a wonderful cave to visit if they are so \n"
            "many cars in the parking lot. To the South is the parking lot.")

SIDE_ENTRANCE = Room("Side Entrance of the House", 'OREO_FACTORY', 'FRONT_STORE', 'KITCHEN', 'HALL', None,
                     "You have reached the side entrance of the house. You enter the creepy house. To the North \n"
                     "their is a Oreo cookie factory, to the East is the front of the store, to the South is the \n"
                     "kitchen and to the West is the hallway.",
                     "You are now inside of the creepy house. To the North  their is a Oreo cookie factory, to the \n"
                     "East is the front of the store, to the South is the kitchen and to the West is the hallway.")

KITCHEN = Room("Kitchen", 'SIDE_ENTRANCE', None, None, 'LIVING_R', None,
               "You have reached the kitchen. You don't see anything but a bunch of cabinets. To the North \n"
               "is the side entrance of the house and to the West is the living room.",
               "You enter the kitchen of the creepy house. To the North is the side entrance of the house and to the \n"
               "West is the living room.")

HALL = Room("The Hall", 'FRONT_HOUSE', 'SIDE_ENTRANCE', 'LIVING_R', None, None,
            "You are in the hallway of the creepy house. In the hallway you can see that there is a book that seems \n"
            " to want you are trying to do. If you know what to do that is. To the North is a door leading \n"
            "to the outside, to the East is a door with a carpet that has an eye on it and to the South is what \n"
            "looks like the living room.",
            "You enter the hallway to the creepy house with the book that does nothing. To the North is a door \n"
            "leading to the outside, to the East is a door with a carpet that has an eye on it and to the South is \n"
            "what looks like the living room.")

LIVING_R = Room("Living Room", 'HALL', 'KITCHEN', None, 'CORRIDOR', None,
                "You reached the living room. There seem to be a maze with the couches. You pass the maze. To \n"
                "the North is the hallway, to the East is the kitchen and to the West is a corridor.",
                "You reached the living room. You don't want to do the maze again so you go over the couches. To the \n"
                "North is the hallway, to the East is the kitchen and to the West is a corridor.")

CORRIDOR = Room("Left Corridor", 'TROPHY_R', 'LIVING_R', 'SHRINE_R', 'DARK_R', None,
                "You find yourself in a cross way inside the house. There is a door to the North that is slightly \n"
                "open that seems to have something bright coming from the room, to the East is the living room, \n"
                "to the South is a bookshelf with books about God and to the West is a room that is dark inside.",
                "You find yourself in a hallway that leads you to four places. There is a door to the North that is \n"
                "slightly open that seems to have something bright coming from the room, to the East is the living \n"
                "room, to the South is a bookshelf with books about God and to the West is a room that is dark inside.")

TROPHY_R = Room("Trophy Room", None, None, 'CORRIDOR', None, None,
                "You find yourself in a room filled with trophy's. You see trophy's of Swimming, Cross \n"
                "Country, Football and Soccer. There are also some posters that are all around the room \n"
                "that are athletes. All you can go is to the South.",
                "You reached the room that is filled with the trophy's. All you can go is to the South.")

SHRINE_R = Room("Shrine Room", 'CORRIDOR', None, 'SOUTH_HOUSE', None, None,
                "You push the bookshelf to find out that it is a hidden door. You found a room that seems to\n"
                "be a shrine. You see a picture of a boy that seems to be around 20 years old. You see food, \n"
                "drinks, and candles that have cobwebs around them. To the North is the secret bookshelf door \n"
                "that leads to the corridor and to the South it seems to lead outside.",
                "You enter the somewhat creepy shrine room. To the North is the secret bookshelf door that leads to \n"
                "the corridor and to the South it seems to lead outside.")

SOUTH_HOUSE = Room("South of House", 'SHRINE_R', None, None, None, None,
                   "You open the door to the outside and you you see a torch that is just sitting their. It \n"
                   "fills you up with hope just to remember that you are all alone in this town. To the North \n"
                   "is the shrine room.",
                   "You reached the south part of the house. To the North is the shrine room.")

DARK_R = Room("The Dark Room", 'SCARY_R', 'CORRIDOR', None, 'WEST_HOUSE', None,
              "You reached a dark room. You can't see anything in the room. Yo felt something in the back \n"
              "of your leg. It feels like a camera. You hear scary sounds in the room to the North, to the \n"
              "East is the corridor and to the West you hear birds chirping.",
              "You entered the dark room. You wonder why they didn't have some kind of light source in the room. You \n"
              "hear scary sounds in the room to the North, to the East is the corridor and to the West you hear \n"
              "birds chirping.")

SCARY_R = Room("Scary Room", None, None, 'DARK_R', None, None,
               "You enter the scary room  to find that the monitor of a computer was on. It was playing \n"
               "scary music from Youtube. You wonder why you they will leave it running. Then you see a key \n"
               "that came shooting out of the wall behind a painting. It is a key. A shiny blue key that \n"
               "says 'P key 2 KEEP HIDDEN'. You wonder why they didn't take it. To the South is the scary \n"
               "room.",
               "You enter the scary room. To the South is the scary room.")

WEST_HOUSE = Room("West of House", None, 'DARK_R', None, None, None,
                  "You leave the house and reached the west side of the house. You can't go anywhere because \n"
                  "it is surrounded by bushed and thick trees. The only way you can go is to the dark room to \n"
                  "the East.",
                  "You are now in the west of the house. You can only go to the East.")

WOODWORK_SECTION = Room("Woodwork section", None, None, 'WALKWAY', 'FRONT_STORE', None,
                        "You go to the woodwork section. Their is a lot of wood that has been cut down and but into \n"
                        "To the South is a Walkway and to the West is the front of the store.",
                        "You are now in the woodwork section. To the South is a Walkway and to the West is the front \n"
                        "of the store.")

WALKWAY = Room("Walkway", 'WOODWORK_SECTION', 'BOX_R', 'BOOK_SECTION', None, None,
               "You find yourself in the walkway of the store. You find yourself in a three-section. To the \n"
               "North is the woodwork section, to the East is the box room and to the South is the book \n"
               "section.",
               "You are in the wall way of the store. You wonder why this is the only one you can go. That is \n"
               "because the others are blocked. To the North is the woodwork section, to the East is the box room \n"
               "and to the South is the book section.")

BOX_R = Room("The Box Room", None, 'MEAT_SECTION', None, 'WALKWAY', None,
             "You enter the box room that seems to be for employee only. The only thing that is in the \n"
             "room are boxes. Boxes. And more boxes. boxes with wood and books. To the East is the Meet \n"
             "section and to the West is the walkway.",
             "You enter the room filled with boxes. To the East is the Meet section and to the West is the walkway.")

MEAT_SECTION = Room("Meat Section", None, None, 'MIRROR_R', 'BOX_R', None,
                    "You reach the meat section of the store. It was all empty but the cow meat section. You \n"
                    "want to take the meat but you don't because it is stealing. To the South is a room full \n"
                    "of mirrors and to the West is the box room.",
                    "You reached the meat section of the store. To the South is a room full of mirrors and to the \n"
                    "West is the box room.")

MIRROR_R = Room("Mirror Room", 'MEAT_SECTION', 'THE_ROOM', None, None, None,
                "You have reached the mirror room and all you see is yourself. ou seemed like you have seen \n"
                "better days. You have baggy clothes and you have shorts. To the North is the meat section \n"
                "and to the East in a door with a caption 'The Room'.",
                "You enter the room that is filled with mirrors. To the North is the meat section and to the East \n"
                "in a door with a caption 'The Room'.")

THE_ROOM = Room("The Room", None, None, None, 'MIRROR_R', None,
                "You enter the mysterious room called the room. You can't see a lot of things since the room \n"
                "is dimly lit. All you can really see is that people have been here. It is all messy as if \n"
                "they were looking for something. They probably found it or game up since they was a corner \n"
                "of the room that was neat and clean. To the West is the Mirror room.",
                "You entered the not so mysterious room. To the West is the Mirror room.")

BOOK_SECTION = Room("Book Section", 'WALKWAY', None, 'BACK_STORE', 'CLOTHING_SECTION', None,
                    "You reach the book section of the store. You see famous books in the 'Famous book section'. \n"
                    "Their were books from the 'Harry Potter' series and the books series of 'Percy Jackson and \n"
                    "the Olympians'. To the North is the Walkway, to the South is a door that is leading outside \n"
                    "and to the West is the clothing section.",
                    "You entered the book section of the store. To the North is the Walkway, to the South is a door \n"
                    "that is leading outside and to the West is the clothing section.")

CLOTHING_SECTION = Room("Clothing Section", None, 'BOOK_SECTION', None, None, None,
                        "You reach the clothing section. You see lines of clothes missing. The only thing you see \n"
                        "is armor that seems to fit you. It seems to be made out of chain mail armor. To the East \n"
                        "is the book section of the store.",
                        "You entered the clothing section of the store. To the East is the book section.")

BACK_STORE = Room("Back of Store", 'BOOK_SECTION', 'SCHOOL_HOUSE', None, None, None,
                  "You reached the back of the store. You see a garbage can that is full of trash. You see a \n"
                  "graffiti that says 'HE CAME'. What that meant was a mystery. To the North is the book \n"
                  "section and to the East is a school House.",
                  "You are now at the back of the school. To the North is the book section and to the East is the \n"
                  "school house.")

SCHOOL_HOUSE = Room("School House", None, None, None, 'BACK_STORE', None,
                    "You reached the front of a small school house that looks like it was from the 1800's. You \n"
                    "try to open the door but it is locked. You try to find another way in but their isn't. \n"
                    "inside seems to be some desk that has a computer that is unreachable. On the screen it \n"
                    "says 'THE MAP' in big letters. But because it was so far away that you couldn't read what \n"
                    "was below it. So you leave it light that. To the West is the back of the store.",
                    "You reached the school house. To the West is the entrance back to the store.")

OREO_FACTORY = Room("The Oreo Cookie Factory", None, 'BACK_MALL', 'SIDE_ENTRANCE', None, None,
                    "You reached the ever so popular Oreo cookie factory. You go inside and you find packs among \n"
                    "packs of double stuffed Oreo's. You grab two packs of double stuffed Oreo's (not that it \n"
                    "matters) so that you have some on the road. You leave the Oreo factory and you walk out \n"
                    "the door. Then you notice a pack of mega stuffed oreo's. You take it and you walk back \n"
                    "outside. To the East is the back of the mall and to the South is the side entrance to a \n"
                    "scary looking house.",
                    "You came back to the Oreo Factory. To the East is the back of the mall and to the South is the \n"
                    "side entrance to a scary looking house.")

FRONT_HOUSE = Room("The Front of the House", 'HALL', None, None, 'PARKING_LOT', None,
                   "You are at the front of the house. You knock on the door to see if anyone is their. No one \n"
                   "answers so you just open the door. You see that the door isn't unlocked. You open the door, \n"
                   "enter the house and closed the door. To the North is the parking lot and to the South is the \n"
                   "hallway.",
                   "You are now in front of the scary house. To the North is what looks like a parking lot and to \n"
                   "the south is a hallway.")

LEFT_MALL = Room("Left of Mall", None, None, 'ALLEYWAY', 'WALMART', None,
                 "You reach the left side of the mall. You see trash cans that don't have anything. You look \n"
                 "inside and their seems to be a graffiti that says 'He is near'. You get out of the garbage \n"
                 "bin and you think for a bit. You wonder why they put that their. To the South is an alley \n"
                 "and to the West is Walmart.",
                 "You are now in the left side of the mall. To the South is the alley way and to the West is Walmart")

ALLEYWAY = Room("The Alleyway", 'LEFT_MALL', 'CASINO', 'GARBAGE TRUCK', None, None,
                "You reach an alleyway. Their isn't much that is here other than a piece of paper with a \n"
                "clown, a bear, a ballerina, and a puppet. You see that it familiar in a way but you couldn't \n"
                "place it. To the North is the left of the mall, to the East is a Casino and to the South \n"
                "seems to have a garbage truck parked outside.",
                "You reached the allyway of the mall. To the North is the left of the mall, to the East is a Casino \n"
                "and to the South seems to have a garbage truck parked outside.")

CASINO = Room("The Casino", None, None, 'RESTAURANT', 'ALLEYWAY', None,
              "You reach the Casino's entrance. You can't enter the casino because you are not 18 years or \n"
              "older. So you just wait outside as you hear slot machines ringing to announce the winner and \n"
              "hear people talking. To the East is a door that is floating. You don't know how but it is.\n"
              "In front of the door has a sign that reads 'you need a key. You that walks and can talk.' \n"
              "Have you seen a key that can do that? To the South is a restaurant and to the West is the \n"
              "alleyway.",
              "You are outside of the casino. To the South is a restaurant and to the West is the alleyway.")

GARBAGE_TRUCK = Room("The Garbage Truck", 'ALLEYWAY', 'STAR_RESTAURANT', None, None, None,
                     "You reached the Garbage truck. When you reach their, you see that the passenger seat s open. \n"
                     "You enter the garbage truck and their seems to be a key of some sort. Their is also a piece \n"
                     "of paper that has some writing on it. To the North is the alleyway and to the East is a \n"
                     "restaurant.",
                     "You are next to the garbage truck. To the North is the alleyway and to the East is a restaurant.")

RESTAURANT = Room("The 5 star Restaurant", 'CASINO', None, 'CORNER', 'GARBAGE_TRUCK', None,
                  "You reached the 5 star restaurant. You feel hungry but you put that feeling away since you \n"
                  "you don't have any money. To the North is a Casino, to the South seems to be a corner and \n"
                  "to the west is a garbage truck.",
                  "You are now in front of the 5-star restaurant. To the North is a Casino, to the South seems to be \n"
                  "a corner and to the west is a garbage truck.")

CORNER = Room("The Corner", 'RESTAURANT', 'CHINESE_RESTAURANT', None, None, None,
              "You reached the corner of the 5 star restaurant and you turn. You see a chinese restaurant \n"
              "that seems to be abandoned because of its location. You see that the walls are being torn \n"
              "by the weather and the windows are broken. To the North is the 5 star restaurant and to the \n"
              "West is the chinese restaurant.",
              "You reached the corner of the of the alleyway. To the North is the 5 star restaurant and to the West \n"
              "is the chinese restaurant.")

CHINESE_RESTAURANT = Room("The Abandoned Chinese Restaurant", None, None, 'CORNER', None, None,
                          "You reached the abandoned chinese restaurant and you go inside. You see that the their was"
                          "\n a lot of people that use to go here because of so any tables and chairs. You see burn "
                          "marks \n on the wall and you wonder if their was a fire. To the West is the corner of "
                          "the 5 star \n restaurant.",
                          "You are now in the parking lot of the abandoned restaurant. To the West is the corner of "
                          "the 5 star \n restaurant.")

TELEPORTER_R = Room("The Teleporter Room", None, None, None, 'CASINO', None,
                    "You enter the door that was floating bit because you hold the key near it stopped floating \n"
                    "and reached the floor. You put the key in the key hole and the door opens. You take the key \n"
                    "and you go inside. Inside seems to have a bunch of wire and a pod in the middle. The pod had \n"
                    "a name. The name was 'The Teleporter 9000'. Their was also a command center but you didn't \n"
                    "touch it. To the West is the casino.",
                    "You are in the teleporter room. To the West is the casino.")

SERVER = Room("The Server", None, None, None, 'CORRUPTED_R', None,
              "You feel dazed because of 'The Teleporter 9000'. You try to walk but you can't. Then you see \n"
              "a door to the west that is slightly open. You see blue light flickering true the bottom of \n"
              "the door. But then you see that their is a sight that dose not very much glows. It reads \n"
              "'YOU SHOULD NOT ENTER. IF YOU ENTER. YOU WILL CRASH THE WORLD AND He WILL COME. IF YOU ENTER \n"
              "WITHOUT THE PROPER MATERIALS. YOU WILL DIE. DON'T SAY YOU WEREN'T WORDED'. You wonder if you \n"
              "have the pieces.",
              "You are now in the server room.")

CORRUPTED_SERVER = Room("The Corrupted Server", 'CORRUPTED_R', 'SERVER', None, None, None,
                        "When you entered the room you felt a weired feeling in your stomach. Their was light on the \n"
                        "walls that wre in a patter like a circuit board. They slowly started to glow red. To the \n"
                        "North wall is a door that has a sign that reads 'To the Server'. To the East is to the \n"
                        "server room.",
                        "You entered the red room. To the East is the server room.")

CORRUPTED_R = Room("Corrupted Server", 'REFLECTIVE_R', None, 'CORRUPTED_R', None, None,
                   "You entered the door to the server room. Then you hear alarm bearing. The room turned red. \n"
                   "Then a speaker spoke, 'The World has been corrupted'.The speaker spoke that over and over. \n"
                   "Your ears. You try to find the panel for the speaker but it is not here. You must find it in \n"
                   "order to stop the speaker. To the North is a room filled with mirrors. You don't know why \n"
                   "their filled with mirrors, but they are. To the South is the corrupted room.",
                   "You entered the anoying room with the load speaker. To the North is a room filled with mirrors. \n"
                   "You don't know why their filled with mirrors, but they are. To the South is the corrupted room.")

REFLECTIVE_R = Room("The Reflective Room", None, None, 'CORRUPTED_SERVER', 'COMPUTER_R', None,
                    "You enter the reflective room. Since you haven't found the panel to the speaker, you haven't \n"
                    "turned off the speaker or the blaring red light. So the mirrors is mostly reflecting red \n"
                    "light. To the South is the corrupted server and to the West is a room filled with complicated \n"
                    "electronics.",
                    "You have reached the reflected room with a bunch of mirrors. Why does it always have to be \n"
                    "mirrors. To the South is the corrupted server and to the West is a room filled with complicated \n"
                    "electronics.")

COMPUTER_R = Room("Computer Room", 'STONE_LIBRARY', 'REFLECTIVE_R', None, None, None,
                  "You reach the room filled with computers. You look at one of the computer screens and you \n"
                  "see that it is a blue screen. The blue screen had text on it. The text says 'The Server is \n"
                  "corrupted. Restarting in an hour'. To the North is door that is made out of stone. it appears \n"
                  "to be open. To the East is the room filled with mirrors.",
                  "You entered the room filled with computers. To the North is door that is made out of stone. it \n"
                  "appears to be open. To the East is the room filled with mirrors.")

STONE_LIBRARY = Room("STONE_LIBRARY", None, None, 'COMPUTER_R', 'GARDEN', None,
                     "You open the stone door. When you open the door, you see a huge library made up of stones. \n"
                     "You wonder why the stone door wasn't even locked. You go down the aile and you see that the \n"
                     "books are very old yet new. To the South is the computer room and to the West is a garden.",
                     "You entered the stone library. To the South is the computer room and to the West is a garden.")

GARDEN = Room("Garden", None, 'STONE_LIBRARY', None, 'CASTLE_KITCHEN', None,
              "You reached the garden.The garden is filled with fruit and vegetables.You wonder why they \n"
              "will leave this beautiful garden with the fruit and vegetables ready to rip. Then you see \n"
              "their is an automated system at play but it had stopped. It had stopped because the server \n"
              "is corrupted. To the East is the stone library and to the west is a door with a picture of \n"
              "a slice of cake on it.",
              "You entered the amazing and beautiful garden. To the East is the stone library and to the west is a \n"
              "door with a picture of a slice of cake on it.")

CASTLE_KITCHEN = Room("Castle Kitchen", 'CASTLE_ENTRANCE', 'GARDEN', 'MAGIC_LIBRARY', 'THRONE_ROOM', None,
                      "You open the door to the door with the slice of cake on it. You see that it is the kitchen \n"
                      "for the castle. You see that their is no food or any ingredients anywhere to be seen. You \n"
                      "feel hungry so you look for the refrigerator. But their isn't any. So you just feel empty \n"
                      "inside. To the North is the castle entrance, to the East is the garden, to the South is a \n"
                      "bookshelf that has the work 'magic' on it and to the West are big doors.",
                      "You entered the castles kitchen. To the North is the castle entrance, to the East is the \n"
                      "garden, to the South is a bookshelf that has the work 'magic' on it and to the West are \n"
                      "big doors.")

MAGIC_LIBRARY = Room("Magic Library", 'KITCHEN', None, 'WATERFALL_R', None, None,
                     "You found the hidden library. All around you, you feel like something very dark and \n"
                     "mysterious things are around. Then you see a book started to drift away with a magenta aura. \n"
                     "Then use see another book but with a yellow aura around it. You don't want to fallow it \n"
                     "since it can be dangerous. To the North is the kitchen and to the South is a blue door.",
                     "You are now in the library with the books that can fly. To the North is the kitchen and to \n"
                     "the South is a blue door.")

WATERFALL_R = Room("Waterfall Room", 'MAGIC_LIBRARY', None, 'MINE_SHAFT', None, None,
                   "You enter the peaceful room with a waterfall. You wonder how such beauty is in a place such \n"
                   "like this. In the Room you see that a rainbow is trying to for but is sucked up from a tube in \n"
                   "the ceiling. It seems to be going to another place from the tube. To the North is the magic \n"
                   "library and to the South is the Mine shaft.",
                   "You entered the room with the beautiful water fall that seems to be out of place. To the North \n"
                   "is the magic library and to the South is the Mine shaft.")

MINE_SHAFT = Room("The Mine Shaft", 'WATERFALL_R', None, None, 'CAVERN', "Pickaxe",
                  "You have reached a mine shaft. You wonder why a place like this would even have a mine shaft \n"
                  "since it can randomly generate whatever it wants. Wait, you didn't know that? Oh well. The only \n"
                  "thing some what ordinary is that a pickaxe is here. To the North is the peaceful waterfall room \n"
                  "and to the West is a deeper part of the mine shaft.",
                  "Why did you come back to the mine if their really isn't anything here for you. To the North is \n"
                  "the peaceful waterfall room and to the West is a deeper part of the mine shaft.")

CAVERN = Room("Cavern", 'LOOPER', 'MINE_SHAFT', None, None, None,
              "You are now in the deeper part of the mine shaft. All that is around you is rock and some minerals. \n"
              "To the North is what look like a way out of the mine shaft and to the East is the mine shaft that \n"
              "had the pickaxe.",
              "You are now in the cavern with rock all around you. To the North is what look like a way out of the \n"
              "mine shaft and to the East is the mine shaft that had the pickaxe.")

LOOPER = Room("The Looper", None, 'THRONE_R', 'CAVERN', 'RAINBOW_R', None,
              "You are now in a room that is filled with side way eights. Then you remembered that side way eights \n"
              "is the infinity sign. Then you see that their is a neon sign that says 'The lopper'. To the East is \n"
              "a throne room, to the South is the cavern and to the West is a door that has rainbows all over the \n"
              "door.",
              "You are back to the Looper room. This sounds ironic. Does it to you? To the East is a throne room, \n"
              "to the South is the cavern and to the West is a door that has rainbows all over the door.")

THRONE_R = Room("Throne Room", None, 'CASTLE_KITCHEN', None, 'LOOPER', None,
                "You entered the throne room that is in the castle. You see that their is someone on one of the \n"
                "thrones. He looked like a king. But the way acted. he didn't seem like a king. To the East is \n"
                "the kitchen and to the West is the room that leads to somewhere else.",
                "You have came back to the impenetrable king. (For those who tried killing the king. You can't \n"
                "kill the king.). To the East is the kitchen and to the West is the room that leads to somewhere else.")

RAINBOW_R = Room("Rainbow Room", None, 'BLOOD_MOON_R', 'LOOPER', None, None,
                 "You have entered the room that has a bunch of rainbows. But they were in jars. They shouldn't be \n"
                 "in jars. Then you see that their is a pipe on the ceiling that seems to be the one that transports \n"
                 "the rainbow into this room. To the East is a door that you can't see into it and to the West is \n"
                 "a room that has an 8 on it.",
                 "You came back to the rainbow room. I guess you feel bad about the rainbows. No?. Then why did you \n"
                 "come back? To the East is a door that you can't see into it and to the West is a room that has an \n"
                 "8 on it.")

BLOOD_MOON_R = Room("Blood Moon Room", None, 'SECTION_3', None, 'RAINBOW_R', None,
                    "You enter the room that was dark inside. But as soon as you came in. You were able to see that \n"
                    "their was a blood moon on the ceiling. 'How is this possible?' you asked yourself. To the East \n"
                    "is a hallway that you can go to in 3 directions and to the West is a room with a rainbow door.",
                    "You have came back to admire the blood moon, right? To the East is a hallway that can go 3 \n"
                    "directions and to the West is a door with a rainbow door.")

SECTION_3 = Room("Section 3", None, 'LIGHT_R', 'CASTLE_ENTRANCE', 'BLOOD_MOON_R', None,
                 "You have made it to a 3-way section hallway. Their is nothing special in the hallway other than \n"
                 "that you can go 3 ways. To the East is a room that has a blinding light, to the South is the \n"
                 "entrance of a castle and to the West is a door that is red and inside is very dark.",
                 "You are now in the 3-way section. To the East is the room that has blinding light inside, to the \n"
                 "South is the castle entrance and to the West is a door that is red that is dark inside.")

CASTLE_ENTRANCE = Room("Castle Entrance", 'SECTION_3', None, 'CASTLE_KITCHEN', None, None,
                       "You are in the castle entrance. What are you going to do. You might find someone that can \n"
                       "help you understand what is going on. To the North is a 3-way section and to the West is the \n"
                       "castle's kitchen.",
                       "You are in the entrance of the castle's entrance. To the North is a 3-way section and to the \n"
                       "West is the castle's kitchen.")

LIGHT_R = Room("Light Room", None, 'BO_BO', None, 'SECTION_3', None,
               "You have reached the room that you couldn't see the inside. You were blinded and you can't see \n"
               "anything. To what you think is East is a room that has something on the door and to what I think is \n"
               "West is a door that is green?",
               "You enter the room that is blinding. Then you feel that something is in your pants pocket and that \n"
               "is a pair of sunglasses. You put them on and you can actually see things inside. To the East is a \n"
               "door that leads to a place called Bo Bo's room and to the West is a green door that leads to a \n"
               "3-way section. Then you put away the sunglasses. Forgetting about them. Even if you are blinded.")

BO_BO = Room("Bo Bo's room", 'PUZZLE_R', 'FORGOTTEN_R', None, 'LIGHT_R', None,
             "You finally reached the door to another room. This room was different. You have never been here \n"
             "before. Yet it is familiar. On the ceiling you see text that says 'Bo Bo's room'. You wonder who he is \n"
             "but you don't want to know. To the North is a rope that doesn't look like you can just cut it and to \n"
             "the West is a the horrible room filed with light.",
             "You entered Bo Bo's room. To the North is a room and to the West is a the horrible room filed with \n"
             "light.")

FORGOTTEN_R = Room("Forgotten Room", None, None, None, 'BO_BO', None,
                   "You enter the room that was well hidden. You asked yourself how you knew about it. It doesn't \n"
                   "matter now. In the room you see a bunch of bookshelves with books. In the room you see a paper \n"
                   "that someone has writen on it. You don't understand it. But then you see a key. It has 'P KEY' \n"
                   "written on it. To the West is Bo BO's room.",
                   "You really like going to hidden rooms don't you know. Bet you feel nice to see this hard to \n"
                   "find key. To the West is Bo Bo'd room")

PUZZLE_R = Room("Puzzle Room", None, None, 'BO_BO', None, None,
                "You enter the room that Gabe told you not to go their. 'The puzzle will be to hard' he said. You \n"
                "didn't care because you wanted everything to go back to normal. Then you saw a scroll and so you \n"
                "opened it. \n"
                "The Puzzle: \n"
                "If you had only one match, and entered a dark room containing an oil lamp, some newspaper, \n"
                "and some kindling wood, which would you light first?",
                "Are you going to solve the puzzle? if you are, here is the puzzle. \n"
                "The Puzzle: \n"
                "If you had only one match, and entered a dark room containing an oil lamp, some newspaper, \n"
                "and some kindling wood, which would you light first?")

# items = ["TR Key", "P Key 1", "P Key 2", "P Key 3", "P Key 4", "Camera", "Paper", "Armor", "Candle", "Torch",
# "Pickaxe", "Rainbow in a Bottle"]

current_node = BACK_MALL
directions = ['north', 'east', 'south', 'west']
short_directions = ['n', 'e', 's', 'w']

moves = 0

end_game = "Once you have thought that the world was so easy, yet you didn't know how hard it was to survive all by \n"\
           "yourself. You saw yourself in a mirror as the wall changed around you. You couldn't do anything to \n"\
           "change that. You saw all your friends go by. there were inside the room. Behind a hidden door that you \n"\
           "didn't see when you first entered.\n"\
           "Thank you for playing my game. It was easy to make the game but I didn't really know what to do with \n"\
           "ending. So I decided to do some improve and created this end game text. Hope you enjoyed the game. :)"

print("You can end the game mid game by writing down 'quit' and entered it.")

while True:
    if current_node == PUZZLE_R:
        yes_no = input("Are you going to solve the question?(answer with a yes or no) ").lower()
        if yes_no == "yes":
            command_puzzle = input("The answer: ").lower()
            if command_puzzle == "the match" or "match":
                print("You got it right.")
                print("It is the match.")
                print("It took you %s moves" % moves)
                print(end_game)
                end_game_now = input("Do you want to end the game now? ").lower()
                if end_game_now == "Yes":
                    quit(0)
        if yes_no == "no":
            current_node = BO_BO
    else:
        print("Your health %s" % current_character.health)
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
                current_node.move(command)
            except KeyError:
                print("Command not recognize")
                print()
        else:
            if command == 'my description':
                print(current_character.description)
            else:
                print("Command not recognize")
