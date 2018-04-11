import random

# Classes


class Item(object):
    def __init__(self, name, description, durability, drop, amount):
        self.name = name
        self.description = description
        self.durability = durability
        self.drop = drop
        self.amount = amount

    def drop(self):
        self.drop = True
        print("You dropped %s." % self.name)

    def pick_up(self):
        self.drop = False
        print("You picked up %s" % self.name)


class Enchanted(Item):
    def __init__(self, name, description, durability, enchanted, drop, amount):
        super(Enchanted, self).__init__(name, description, durability, drop, amount)
        self.enchanted = enchanted

    def used(self):
        if self.name == "armor of undying":
            print("You have been revived. But your armor is now broken.")
            current_character.inventory.pop("ARMOR OF UNDYING")
        if self.name == "armor of strength":
            self.durability = self.durability - 5
            print("Your durability is now %s" % self.durability)


class Key(Item):
    def __init__(self, name, description, durability, door, drop, door_number, amount):
        super(Key, self).__init__(name, description, durability, drop, amount)
        self.door = door
        self.door_number = door_number

    def use(self):
        if self.door_number == 1:
            print("You used %s. The door that you opened was %s." % (self.name, self.door))


class Edible(Item):
    def __init__(self, name, description, durability, drop, amount):
        super(Edible, self).__init__(name, description, durability, drop, amount)

    def consume(self):
        print("You consumed %s" % self.name)


class Craftable(Item):
    def __init__(self, name, description, durability, drop, amount):
        super(Craftable, self).__init__(name, description, durability, drop, amount)

    def crafting(self):
        if command == "armor of undying":
            if "cosmonium ore" in current_character.inventory:
                current_character.inventory.append("ARMOR OF UNDYING")
                print("You have used your cosmonium ore.")
                print(
                    "You have created the ARMOR OF UNDYING. type in 'armor of undying description' in the command \n"
                    "to see what it does.")
        if command == "armor of strength":
            if "strength potion" in current_character.inventory:
                current_character.inventory.append("ARMOR OF STRENGTH")
                print("You have used one of your strength potion.")
                print("You have created the ARMOR OF STRENGTH. type in 'armor of strength' in the command to see \n"
                      "what it does.")


class Armor(Item):
    def __init__(self, name, description, durability, drop, armor, amount, craftable):
        super(Armor, self).__init__(name, description, durability, drop, amount)
        self.armor = armor
        self.craftable = craftable

    def use(self):
        print("You put on %s." % self.name)


class Weapons(Item):
    def __init__(self, name, description, durability, drop, damage, ability, amount):
        super(Weapons, self).__init__(name, description, durability, drop, amount)
        self.ability = ability
        self.broke = False
        self.damage = damage

    def broke(self):
        if self.durability == 0:
            self.broke = True
            print("Your %s broke because it had lost its durability." % self.name)
            current_character.inventory.pop(self.name)


class Potion(Edible):
    def __init__(self, name, description, durability, drop, duration, ability, amount):
        super(Potion, self).__init__(name, description, durability, drop, amount)
        self.duration = duration
        self.ability = ability

    def drink(self):
        if self.name in current_character.inventory:
            print("You drank %s." % self.name)
            current_character.inventory.pop(self.name)
            print("You know have %s affect." % self.ability)


class Food(Edible):
    def __init__(self, name, description, durability, heal, drop, amount):
        super(Food, self).__init__(name, description, durability, drop, amount)
        self.heal = heal

    def heal(self):
        if current_character.health == 100:
            print("Why you trying to heal yourself if you have all your health. Are you hungry?")
        else:
            if current_character.health >= 50:
                print("You used %s. You are now maxed out in health.")
                current_character.inventory.pop(self.name)
            else:
                print("You need to have less than 50 health in order to use this item.")


class Lowhealth(Food):
    def __init__(self, name, description, durability, heal, drop, amount):
        super(Lowhealth, self).__init__(name, description, durability, heal, drop, amount)


class Maxhealth(Food):
    def __init__(self, name, description, durability, heal, drop, amount):
        super(Maxhealth, self).__init__(name, description, durability, heal, drop, amount)


class Healthpot(Potion):
    def __init__(self, name, description, durability, drop, duration, ability, heal, amount):
        super(Healthpot, self).__init__(name, description, durability, drop, duration, ability, amount)
        self.heal = heal

    def healing(self):
        if current_character.health <= 90:
            if (self.heal + current_character) < 100:
                current_character.health = current_character.health + self.heal
            else:
                print("You dn't want to want to over heal do you.")


class Strengthpot(Potion):
    def __init__(self, name, description, durability, duration, drop, ability, strength, amount):
        super(Strengthpot, self).__init__(name, description, durability, duration, drop, ability, amount)
        self.strength = strength

    def strength(self):
        current_character.inventory.pop(self.name)
        print("You now have strength for %s seconds." % self.duration)
        current_character.damage = current_character.damage + self.strength


class Resistancepot(Potion):
    def __init__(self, name, description, durability, drop, duration, ability, armor, amount):
        super(Resistancepot, self).__init__(name, description, durability, drop, duration, ability, amount)
        self.armor = armor

    def armor_gain(self):
        current_character.inventory.pop(self.name)
        print("You now have resistance for %s seconds." % self.duration)
        current_character.armor = current_character.armor + self.armor


class Sword(Weapons):
    def __init__(self, name, description, durability, drop, damage, ability, amount):
        super(Sword, self).__init__(name, description, durability, drop, damage, ability, amount)


class Bow(Weapons):
    def __init__(self, name, description, durability, drop, damage, distance, ability, amount):
        super(Bow, self).__init__(name, description, durability, drop, damage, ability, amount)
        self.distance = distance


class Ammo(Item):
    def __init__(self, name, description, durability, drop, amount, weapon, ability):
        super(Ammo, self).__init__(name, description, durability, drop, amount)
        self.weapon = weapon
        self.ability = ability


class EnchantBook(Enchanted):
    def __init__(self, name, description, durability, enchanted, drop, amount):
        super(EnchantBook, self).__init__(name, description, durability, enchanted, drop, amount)


class Characters(object):
    def __init__(self, name, inventory, health, armor, damage, weapon, description, diologue, hostile, alive):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.armor = armor
        self.damage = damage
        self.description = description
        self.diologue = diologue
        self.weapon = weapon
        self.hostile = hostile
        self.alive = alive

    def attacked(self):
        if self.armor >= 1:
            self.damage = self.damage - self.armor
            if self.armor <= self.hostile.damage:
                self.damage = self.armor - self.hostile.damage
                self.damage = self.damage
        if self.weapon:
            self.damage = self.damage * 2.5

    def attacking(self):
        if self.hostile:
            if self.armor >= 1:
                self.damage = self.damage - self.armor
                if self.armor <= self.hostile.damage:
                    self.damage = self.armor - self.hostile.damage
                    self.damage = self.damage
            if self.weapon:
                self.damage = self.damage * 2.5
            self.hostile.health = self.hostile.health - self.hostile.damage

    def diologue(self):
        if self.alive:
            length = len(self.diologue)
            diologue = random.randint(length)
            print(diologue)


class Room(object):
    def __init__(self, name, north, east, south, west, item, repeat, description, description_2, stayed, enemies=None):
        self.name = name
        self.description = description
        self.description_2 = description_2
        self.stayed = stayed
        self.item = item
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.again = repeat
        self.enemies = enemies

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


# Keys
tr_key = Key("TR Key",
             "The TR Key seems to open a door that is locked. Which door that can be is unknown.", None, 'teleporter_R',
             True, 0, 1)

p_key_1 = Key("P Key #1",
              "The first key seems to not be the only key.", None, 'puzzle_R', True, 1, 1)

p_key_2 = Key("P Key #2",
              "The second key seems to not be the only key.", None, 'puzzle_R', True, 1, 1)

p_key_3 = Key("P Key #3",
              "The third key seems o not be the only key.", None, 'puzzle_R', True, 1, 1)

p_key_4 = Key("P Key #4",
              "The Last key seems to not be the only key. Their is a note in the back. It reads 'You must have all \n"
              "of the keys in order to be in the puzzle room.'", None, 'puzzle_R', True, 1, 1)

# Armor
leather_armor = Armor("leather armor",
                      "This armor type is the weakest armor possible.", 20, True, 30, 1, False)

wood_armor = Armor("wooden armor",
                   "This armor is made complete made of flexible wood.", 30, True, 35, 1, True)

iron_armor = Armor("iron armor",
                   "This armor is made of iron bars.", 45, True, 50, 1, True)

gold_armor = Armor("gold armor",
                   "This armor is made of gold bars. It is extremely heavy and it doesn't block a lot of hits.", 35,
                   True, 15, 1, True)

diamond_armor = Armor("diamond armor",
                      "This armor is made from diamonds.", 150, True, 85, 1, True)

armor_of_undying = Armor("ARMOR OF UNDYING",
                         "The armor of undying will revive you when you die. But when the armor revives you, it will \n"
                         "break and you will not have the armor anymore.", 1, True, 20, 1, True)

armor_of_strength = Armor("ARMOR OF STRENGTH",
                          "The armor of strength will give you extra damage. But when you attack, you will lose 5% \n"
                          "of your base health(100).", 250, True, 35, 1, True)

# Extras
candle = Item("candle",
              "This candle can be use so that you can burn something. But what?", 1, True, 1)

torch = Item("torch",
             "This torch can be used to burn something. But what?", 1, True, 1)

pickaxe = Item("a diamond pickaxe",
               "This item seams to be used to mine hard to get materials. Which material it is unknown. Maybe you \n"
               "will find it somewhere.", 1, True, 1)

rainbow_in_a_bottle = Healthpot("rainbow in a bottle",
                                "The rainbow in the bottle fills you up with warmth. It is almost as if it can heal \n"
                                "you.", 5, True, 0, "heal", 20, 1)

paper_with_writing = Item("paper",
                          "The piece of paper that you found has writing in it. it reads 'You Must find the puzzle \n"
                          "room. if you don't we will never escApe. who ever you are, you Must find us. We are \n"
                          "Trapped. we Can't find tHe exit. you must pass the test in order to free us. hope you are \n"
                          "come quickly. we are running out of food.'", 1, True, 1)

camera = Item("camera",
              "You look at the camera. You wonder if they are any photos inside it.", 1, True, 1)

firework = Item("firework",
                "Its a firework. It goes BOOM.", 1, True, 1)

wallet = Item("wallet",
              "It is a wallet with some money in it. But you don't even need it.", 1, False, 1)

# Weapons
dull_sword = Sword("dull sword",
                   "This sword is dull.", 100, True, 8, None, 1)

sharp_sword = Sword("sharp sword",
                    "This sword is so sharp, it can cut stone.", 50, True, 73, None, 1)

magical_sword = Sword("MAGICAL SWORD",
                      "This sword seems magical. It is glowing with a purple glow.", 230, True, 99, 'Burn', 1)

broken_bow = Bow("broken bow",
                 "The bow is broken. you can use it but it might now do a lot of damage.", 14, True, 11, 13, None, 1)

x_bow = Bow("x-bow",
            "You have a cross bar.", 300, True, 46, 38, 'strength', 1)

metal_bow = Bow("metal bow",
                "The bow has been reinforced with iron.", 200, True, 73, 74, 'strength', 1)

legendary_bow = Bow("LEGENDARY BOW",
                    "This bow is a reinforced bow that has 3 enchantments with it.", 999, True, 300, 235,
                    ['strength', 'unbreakable', 'fire_frost'], 1)

# Enchanted Books
strength_book = EnchantBook("strength book",
                            "This book gives an item more damage.", 1, 'strength', True, 1)

unbreakable_book = EnchantBook("unbreakable book",
                               "This book gives an item more durability", 1, 'unbreakable', True, 1)

fire_frost_book = EnchantBook("FIRE FROST BOOK",
                              "This book gives an item more damage and makes half of the sword on fire and the other \n"
                              "frozen. When you hit an enemy, they will either burn or they would freeze. If the \n"
                              "enemy has burn, they would lose 10% of their health when it is their turn. If the \n"
                              "item also has strength, the burn will do 20% of their health. If the enemy has been \n"
                              "frozen. They will lose 2 turns.", 1, 'fire_frost', True, 1)

# Potions
weak_health_potion = Potion("weak health potion",
                            "This health potion gives you 20 health back.", 1, True, 1, 'health', 1)

strong_health_potion = Potion("strong health potion",
                              "This health potion gives you 50 health back.", 1, True, 1, 'health', 1)

strength_potion = Potion("strength potion",
                         "This strength potion gives you an attack boost for 30 moves.", 1, True, 30, 'strength', 1)

poison_potion = Potion("POISON IN A BOTTLE",
                       "This potion can be thrown and will poison the enemy. The poison will not kill the enemy. The \n"
                       "enemy will do less damage and will have less health", 1, True, 1, 'poison', 1)

# Ammo
wooden_arrow = Ammo("wooden arrow",
                    "This ammo is used for bows. The arrow isn't the strongest but it is the easiest to craft. Can \n"
                    "be used for the broken bow and the metal bow.", 1, True, 1, ['broken_bow', 'metal_bow'], None)
metal_arrow = Ammo("metal arrow",
                   "This ammo is used for bows. The arrow is the strongest that you can craft. Can be used for metal \n"
                   "bows only", 1, True, 1, 'metal_bow', None)

normal_crossbow_bolt = Ammo("normal crossbow bolt",
                            "This ammo is used for an x-bow. It isn't the only ammo for the x-bow.", 1, True, 1,
                            'x_bow', None)

explosive_crossbow_bolt = Ammo("EXPLOSIVE X-BOW BOLT ",
                               "This ammo is used only for an x-bow. This bolt explodes on impact and does more \n"
                               "damage on impact.", 1, True, 1, 'x-bow', None)

electric_crossbow_bolt = Ammo("ELECTRIC X-BOW BOLT",
                              "This ammo is used only for an x-bow. This bolt will electrocute the enemy.", 1, True,
                              1, 'x-bow', None)

# Food
raw_potato = Food("raw potato",
                  "You can eat this raw potato. But it looks so weird.", 1, 5, True, 1)

cooked_potato = Food("cooked potato",
                     "This potato is cooked.", 1, 15, True, 1)

potato_chip = Food("potato chips",
                   "Its a bag of chips.", 1, 20, True, 1)

raw_meat = Food("raw meat",
                "This is a piece of raw meat from an unknown creature.", 1, 30, True, 1)

unicorn_meat = Food("UNICORN MEAT",
                    "Despite its name, it is not from a unicorn. It is just called that because it is extremely rare.\n"
                    "Tho it is does have a little bit of a rainbow color. But it is just food dye.",
                    1, 80, True, 1)

# Characters
gabe = Characters("Gabe", [pickaxe, torch, Sword, wallet], 100, 10, 20, False,
                  "The Enemies name is Gabe, he is one of the hardest people to fight. He have killed many people \n"
                  "for trying to solve the puzzle. They never got to the question so they weren't able to tell \n"
                  "people the question.",
                  ["It is I, Gabe, the one that changed the world. If you want to get your family and friends and \n"
                   "everyone in your world back, you have to get past me.", "In order to solve you family, you need \n"
                   "to solve the puzzle.", "You have defeated me. You may solve the riddle. But be worn. If you \n"
                   "don't solve it within your third try, you will die. So be worn."], False, True)

current_character = Characters("John", [raw_potato], 100, 0, 10, False,
                               "You are yourself. Don't let anyone change that.", None, False, True)

# Initialize Rooms
BACK_MALL = Room("Back of the Mall", 'TARGET', None, 'FRONT_STORE', None, ['raw_potato'], False,
                 "You are in the back of the mall. You wonder were you are and how you got here. You see Target to \n"
                 "North and the front of a store to the south.",
                 "You are in the back of the mall. You see Target in the North and the front of a store to the \n "
                 "south.", False, None)

FRONT_STORE = Room("Front of Store", 'BACK_MALL', 'WOODWORK_SECTION', None, 'SIDE_ENTRANCE', None, False,
                   "The store is a convenient store that has been here for a while. To the North is the back of \n "
                   "a mall, to the East is the Woodwork section, and to the West is an entrance to an abandoned \n "
                   "house.",
                   "You reached the cashier of the convenient store. To the East is the Woodwork section, and to the \n"
                   "West is an entrance to an abandoned house", False, None)

TARGET = Room("Target", 'WALMART', 'HOME_D', 'BACK_MALL', 'OFFICE_D', None, False,
              "You have entered Target and walked through. You have triggered the metal detector and was \n kicked out"
              "of the store. Walmart is to the North, Home Depot is in the East, Office Depot \n is in the West, and"
              "to the South is the back of the mall.",
              "You are now in front of Target. Walmart is to the North, Home Depot is in the East, Office Depot is \n"
              "to the West, and to the South is the back of the mall.", False, None)

OFFICE_D = Room("Office Depot", 'APPLE', 'HOME_D', None, 'CAR', None, False,
                "You have entered Office Depot and didn't want to go thought because of what happened with Target. \n"
                "To the West is Target and to the East is the left of the mall.",
                "You are outside of Office Depot. To the West is Target and to the East is the left of the mall.",
                False, None)

CAR = Room("The Car", None, 'OFFICE_D', None, 'PARKING', None, False,
           "You found your car. But you left your keys in an unknown area, so you can't get in. To the East is \n"
           "Office Depot and to the West in the Parking lot.",
           "You are now near you car. To the East is Office Depot and to the West in the Parking lot.", False, None)

PARKING = Room("Parking Lot", 'CAVE', 'CAR', 'FRONT_HOUSE', 'TRUCK', None, False,
               "You have reached the parking lot. Their are a lot of cars in the parking lot to visit the \n bat cave."
               "To the North is the bat cave, to the East is were your car is at, to the South is \n the front of a"
               "house and to the west is a taco truck.",
               "You reached the parking lot fulled with car but with no one around. To the North is the bat cave, to \n"
               "the East is were your car is at, to the South is the front of a house and to the west is a taco truck.",
               False, None)

TRUCK = Room("Taco Truck", None, 'PARKING', None, None, None, False,
             "You smell a the tacos that are in the truck. You want to buy a taco because you are hungry \n but you"
             "don't have any money. To the East is the parking lot.",
             "You are now near the taco truck. To the East is the parking lot.", False, None)

APPLE = Room("The Apple Store", 'SERVER_R', None, 'OFFICE_D', None, None, False,
             "You have reached the famous store from the Apple company. You want to go in but you don't \n have any"
             "intentions their. To the North is a fence that is locked with unbreakable chains \n with a lock on a door"
             "that doesn't look like a normal key. To the South is Office Depot.",
             "You are now outside of the ever so famous Apple store from Apple.inc. To the North is a fence that is \n"
             "locked with unbreakable chains with a lock on a door that doesn't look like a normal key. To the South \n"
             "is Office Depot.", False, None)

HOME_D = Room("Home Depot", None, None, None, 'TARGET', None, False,
              "You have reached Home Depot. You don't want to go inside because it you have nothing to do in \n"
              "their. You wonder if you could steal something since their is no one around. They wont notice it \n"
              "gone. To the East is the left of mall and to the West is Target.",
              "You reached outside of Home Depot. To the East is the left of mall and to the West is Target.", False,
              None)

WALMART = Room("Walmart", None, 'LEFT_MALL', None, 'Target', None, False,
               "You have reached Walmart. You don't want to go inside because it you have nothing to do in \n"
               "their. To the East is the left of mall and to the West is Target.",
               "You are now outside of walmart. To the East is the left of mall and to the West is Target.", False,
               None)

CAVE = Room("The Bat Cave", None, None, 'PARKING', None, None, False,
            "You have reached the bat cave but no one is here. It is strange that no one whn their is a \n"
            "full parking lot. To the South is the parking lot.",
            "You are now outside of the cave. You still wonder why this is a wonderful cave to visit if they are so \n"
            "many cars in the parking lot. To the South is the parking lot.", False, None)

SIDE_ENTRANCE = Room("Side Entrance of the House", 'OREO_FACTORY', 'FRONT_STORE', 'KITCHEN', 'HALL', None, False,
                     "You have reached the side entrance of the house. You enter the creepy house. To the North \n"
                     "their is a Oreo cookie factory, to the East is the front of the store, to the South is the \n"
                     "kitchen and to the West is the hallway.",
                     "You are now inside of the creepy house. To the North  their is a Oreo cookie factory, to the \n"
                     "East is the front of the store, to the South is the kitchen and to the West is the hallway.",
                     False, None)

KITCHEN = Room("Kitchen", 'SIDE_ENTRANCE', None, None, 'LIVING_R', None, False,
               "You have reached the kitchen. You don't see anything but a bunch of cabinets. To the North \n"
               "is the side entrance of the house and to the West is the living room.",
               "You enter the kitchen of the creepy house. To the North is the side entrance of the house and to the \n"
               "West is the living room.", False, None)

HALL = Room("The Hall", 'FRONT_HOUSE', 'SIDE_ENTRANCE', 'LIVING_R', None, None, False,
            "You are in the hallway of the creepy house. In the hallway you can see that there is a book that seems \n"
            " to want you are trying to do. If you know what to do that is. To the North is a door leading \n"
            "to the outside, to the East is a door with a carpet that has an eye on it and to the South is what \n"
            "looks like the living room.",
            "You enter the hallway to the creepy house with the book that does nothing. To the North is a door \n"
            "leading to the outside, to the East is a door with a carpet that has an eye on it and to the South is \n"
            "what looks like the living room.", False, None)

LIVING_R = Room("Living Room", 'HALL', 'KITCHEN', None, 'CORRIDOR', None, False,
                "You reached the living room. There seem to be a maze with the couches. You pass the maze. To \n"
                "the North is the hallway, to the East is the kitchen and to the West is a corridor.",
                "You reached the living room. You don't want to do the maze again so you go over the couches. To the \n"
                "North is the hallway, to the East is the kitchen and to the West is a corridor.", False, None)

CORRIDOR = Room("Left Corridor", 'TROPHY_R', 'LIVING_R', 'SHRINE_R', 'DARK_R', None, False,
                "You find yourself in a cross way inside the house. There is a door to the North that is slightly \n"
                "open that seems to have something bright coming from the room, to the East is the living room, \n"
                "to the South is a bookshelf with books about God and to the West is a room that is dark inside.",
                "You find yourself in a hallway that leads you to four places. There is a door to the North that is \n"
                "slightly open that seems to have something bright coming from the room, to the East is the living \n"
                "room, to the South is a bookshelf with books about God and to the West is a room that is dark inside.",
                False, None)

TROPHY_R = Room("Trophy Room", None, None, 'CORRIDOR', None, None, False,
                "You find yourself in a room filled with trophy's. You see trophy's of Swimming, Cross \n"
                "Country, Football and Soccer. There are also some posters that are all around the room \n"
                "that are athletes. All you can go is to the South.",
                "You reached the room that is filled with the trophy's. All you can go is to the South.", False, None)

SHRINE_R = Room("Shrine Room", 'CORRIDOR', None, 'SOUTH_HOUSE', None, None, False,
                "You push the bookshelf to find out that it is a hidden door. You found a room that seems to\n"
                "be a shrine. You see a picture of a boy that seems to be around 20 years old. You see food, \n"
                "drinks, and candles that have cobwebs around them. To the North is the secret bookshelf door \n"
                "that leads to the corridor and to the South it seems to lead outside.",
                "You enter the somewhat creepy shrine room. To the North is the secret bookshelf door that leads to \n"
                "the corridor and to the South it seems to lead outside.", False, None)

SOUTH_HOUSE = Room("South of House", 'SHRINE_R', None, None, None, None, False,
                   "You open the door to the outside and you you see a torch that is just sitting their. It \n"
                   "fills you up with hope just to remember that you are all alone in this town. To the North \n"
                   "is the shrine room.",
                   "You reached the south part of the house. To the North is the shrine room.", False, None)

DARK_R = Room("The Dark Room", 'SCARY_R', 'CORRIDOR', None, 'WEST_HOUSE', None, False,
              "You reached a dark room. You can't see anything in the room. Yo felt something in the back \n"
              "of your leg. It feels like a camera. You hear scary sounds in the room to the North, to the \n"
              "East is the corridor and to the West you hear birds chirping.",
              "You entered the dark room. You wonder why they didn't have some kind of light source in the room. You \n"
              "hear scary sounds in the room to the North, to the East is the corridor and to the West you hear \n"
              "birds chirping.", False, None)

SCARY_R = Room("Scary Room", None, None, 'DARK_R', None, None, False,
               "You enter the scary room  to find that the monitor of a computer was on. It was playing \n"
               "scary music from Youtube. You wonder why you they will leave it running. Then you see a key \n"
               "that came shooting out of the wall behind a painting. It is a key. A shiny blue key that \n"
               "says 'P key 2 KEEP HIDDEN'. You wonder why they didn't take it. To the South is the scary \n"
               "room.",
               "You enter the scary room. To the South is the scary room.", False, None)

WEST_HOUSE = Room("West of House", None, 'DARK_R', None, None, None, False,
                  "You leave the house and reached the west side of the house. You can't go anywhere because \n"
                  "it is surrounded by bushed and thick trees. The only way you can go is to the dark room to \n"
                  "the East.",
                  "You are now in the west of the house. You can only go to the East.", False, None)

WOODWORK_SECTION = Room("Woodwork section", None, None, 'WALKWAY', 'FRONT_STORE', None, False,
                        "You go to the woodwork section. Their is a lot of wood that has been cut down and but into \n"
                        "To the South is a Walkway and to the West is the front of the store.",
                        "You are now in the woodwork section. To the South is a Walkway and to the West is the front \n"
                        "of the store.", None)

WALKWAY = Room("Walkway", 'WOODWORK_SECTION', 'BOX_R', 'BOOK_SECTION', None, None, False,
               "You find yourself in the walkway of the store. You find yourself in a three-section. To the \n"
               "North is the woodwork section, to the East is the box room and to the South is the book \n"
               "section.",
               "You are in the wall way of the store. You wonder why this is the only one you can go. That is \n"
               "because the others are blocked. To the North is the woodwork section, to the East is the box room \n"
               "and to the South is the book section.", False, None)

BOX_R = Room("The Box Room", None, 'MEAT_SECTION', None, 'WALKWAY', None, False,
             "You enter the box room that seems to be for employee only. The only thing that is in the \n"
             "room are boxes. Boxes. And more boxes. boxes with wood and books. To the East is the Meet \n"
             "section and to the West is the walkway.",
             "You enter the room filled with boxes. To the East is the Meet section and to the West is the walkway.",
             False, None)

MEAT_SECTION = Room("Meat Section", None, None, 'MIRROR_R', 'BOX_R', None, False,
                    "You reach the meat section of the store. It was all empty but the cow meat section. You \n"
                    "want to take the meat but you don't because it is stealing. To the South is a room full \n"
                    "of mirrors and to the West is the box room.",
                    "You reached the meat section of the store. To the South is a room full of mirrors and to the \n"
                    "West is the box room.", False, None)

MIRROR_R = Room("Mirror Room", 'MEAT_SECTION', 'THE_ROOM', None, None, None, False,
                "You have reached the mirror room and all you see is yourself. ou seemed like you have seen \n"
                "better days. You have baggy clothes and you have shorts. To the North is the meat section \n"
                "and to the East in a door with a caption 'The Room'.",
                "You enter the room that is filled with mirrors. To the North is the meat section and to the East \n"
                "in a door with a caption 'The Room'.", False, None)

THE_ROOM = Room("The Room", None, None, None, 'MIRROR_R', None, False,
                "You enter the mysterious room called the room. You can't see a lot of things since the room \n"
                "is dimly lit. All you can really see is that people have been here. It is all messy as if \n"
                "they were looking for something. They probably found it or game up since they was a corner \n"
                "of the room that was neat and clean. To the West is the Mirror room.",
                "You entered the not so mysterious room. To the West is the Mirror room.", False, None)

BOOK_SECTION = Room("Book Section", 'WALKWAY', None, 'BACK_STORE', 'CLOTHING_SECTION', None, False,
                    "You reach the book section of the store. You see famous books in the 'Famous book section'. \n"
                    "Their were books from the 'Harry Potter' series and the books series of 'Percy Jackson and \n"
                    "the Olympians'. To the North is the Walkway, to the South is a door that is leading outside \n"
                    "and to the West is the clothing section.",
                    "You entered the book section of the store. To the North is the Walkway, to the South is a door \n"
                    "that is leading outside and to the West is the clothing section.", False, None)

CLOTHING_SECTION = Room("Clothing Section", None, 'BOOK_SECTION', None, None, None, False,
                        "You reach the clothing section. You see lines of clothes missing. The only thing you see \n"
                        "is armor that seems to fit you. It seems to be made out of chain mail armor. To the East \n"
                        "is the book section of the store.",
                        "You entered the clothing section of the store. To the East is the book section.", False, None)

BACK_STORE = Room("Back of Store", 'BOOK_SECTION', 'SCHOOL_HOUSE', None, None, None, False,
                  "You reached the back of the store. You see a garbage can that is full of trash. You see a \n"
                  "graffiti that says 'HE CAME'. What that meant was a mystery. To the North is the book \n"
                  "section and to the East is a school House.",
                  "You are now at the back of the school. To the North is the book section and to the East is the \n"
                  "school house.", False, None)

SCHOOL_HOUSE = Room("School House", None, None, None, 'BACK_STORE', None, False,
                    "You reached the front of a small school house that looks like it was from the 1800's. You \n"
                    "try to open the door but it is locked. You try to find another way in but their isn't. \n"
                    "inside seems to be some desk that has a computer that is unreachable. On the screen it \n"
                    "says 'THE MAP' in big letters. But because it was so far away that you couldn't read what \n"
                    "was below it. So you leave it light that. To the West is the back of the store.",
                    "You reached the school house. To the West is the entrance back to the store.", False, None)

OREO_FACTORY = Room("The Oreo Cookie Factory", None, 'BACK_MALL', 'SIDE_ENTRANCE', None, None, False,
                    "You reached the ever so popular Oreo cookie factory. You go inside and you find packs among \n"
                    "packs of double stuffed Oreo's. You grab two packs of double stuffed Oreo's (not that it \n"
                    "matters) so that you have some on the road. You leave the Oreo factory and you walk out \n"
                    "the door. Then you notice a pack of mega stuffed oreo's. You take it and you walk back \n"
                    "outside. To the East is the back of the mall and to the South is the side entrance to a \n"
                    "scary looking house.",
                    "You came back to the Oreo Factory. To the East is the back of the mall and to the South is the \n"
                    "side entrance to a scary looking house.", False, None)

FRONT_HOUSE = Room("The Front of the House", 'HALL', None, None, 'PARKING_LOT', None, False,
                   "You are at the front of the house. You knock on the door to see if anyone is their. No one \n"
                   "answers so you just open the door. You see that the door isn't unlocked. You open the door, \n"
                   "enter the house and closed the door. To the North is the parking lot and to the South is the \n"
                   "hallway.",
                   "You are now in front of the scary house. To the North is what looks like a parking lot and to \n"
                   "the south is a hallway.", False, None)

LEFT_MALL = Room("Left of Mall", None, None, 'ALLEYWAY', 'WALMART', None, False,
                 "You reach the left side of the mall. You see trash cans that don't have anything. You look \n"
                 "inside and their seems to be a graffiti that says 'He is near'. You get out of the garbage \n"
                 "bin and you think for a bit. You wonder why they put that their. To the South is an alley \n"
                 "and to the West is Walmart.",
                 "You are now in the left side of the mall. To the South is the alley way and to the West is Walmart",
                 False, None)

ALLEYWAY = Room("The Alleyway", 'LEFT_MALL', 'CASINO', 'GARBAGE TRUCK', None, None, False,
                "You reach an alleyway. Their isn't much that is here other than a piece of paper with a \n"
                "clown, a bear, a ballerina, and a puppet. You see that it familiar in a way but you couldn't \n"
                "place it. To the North is the left of the mall, to the East is a Casino and to the South \n"
                "seems to have a garbage truck parked outside.",
                "You reached the alleyway of the mall. To the North is the left of the mall, to the East is a Casino \n"
                "and to the South seems to have a garbage truck parked outside.", False, None)

CASINO = Room("The Casino", None, None, 'RESTAURANT', 'ALLEYWAY', None, False,
              "You reach the Casino's entrance. You can't enter the casino because you are not 18 years or \n"
              "older. So you just wait outside as you hear slot machines ringing to announce the winner and \n"
              "hear people talking. To the East is a door that is floating. You don't know how but it is.\n"
              "In front of the door has a sign that reads 'you need a key. You that walks and can talk.' \n"
              "Have you seen a key that can do that? To the South is a restaurant and to the West is the \n"
              "alleyway.",
              "You are outside of the casino. To the South is a restaurant and to the West is the alleyway.", False,
              None)

GARBAGE_TRUCK = Room("The Garbage Truck", 'ALLEYWAY', 'STAR_RESTAURANT', None, None, None, False,
                     "You reached the Garbage truck. When you reach their, you see that the passenger seat s open. \n"
                     "You enter the garbage truck and their seems to be a key of some sort. Their is also a piece \n"
                     "of paper that has some writing on it. To the North is the alleyway and to the East is a \n"
                     "restaurant.",
                     "You are next to the garbage truck. To the North is the alleyway and to the East is a restaurant.",
                     False, None)

RESTAURANT = Room("The 5 star Restaurant", 'CASINO', None, 'CORNER', 'GARBAGE_TRUCK', None, False,
                  "You reached the 5 star restaurant. You feel hungry but you put that feeling away since you \n"
                  "you don't have any money. To the North is a Casino, to the South seems to be a corner and \n"
                  "to the west is a garbage truck.",
                  "You are now in front of the 5-star restaurant. To the North is a Casino, to the South seems to be \n"
                  "a corner and to the west is a garbage truck.", False, None)

CORNER = Room("The Corner", 'RESTAURANT', 'CHINESE_RESTAURANT', None, None, None, False,
              "You reached the corner of the 5 star restaurant and you turn. You see a chinese restaurant \n"
              "that seems to be abandoned because of its location. You see that the walls are being torn \n"
              "by the weather and the windows are broken. To the North is the 5 star restaurant and to the \n"
              "West is the chinese restaurant.",
              "You reached the corner of the of the alleyway. To the North is the 5 star restaurant and to the West \n"
              "is the chinese restaurant.", False, None)

CHINESE_RESTAURANT = Room("The Abandoned Chinese Restaurant", None, None, 'CORNER', None, None, False,
                          "You reached the abandoned chinese restaurant and you go inside. You see that the their was"
                          "\n a lot of people that use to go here because of so any tables and chairs. You see burn "
                          "marks \n on the wall and you wonder if their was a fire. To the West is the corner of "
                          "the 5 star \n restaurant.",
                          "You are now in the parking lot of the abandoned restaurant. To the West is the corner of "
                          "the 5 star \n restaurant.", False, None)

TELEPORTER_R = Room("The Teleporter Room", None, None, None, 'CASINO', None, False,
                    "You enter the door that was floating bit because you hold the key near it stopped floating \n"
                    "and reached the floor. You put the key in the key hole and the door opens. You take the key \n"
                    "and you go inside. Inside seems to have a bunch of wire and a pod in the middle. The pod had \n"
                    "a name. The name was 'The Teleporter 9000'. Their was also a command center but you didn't \n"
                    "touch it. To the West is the casino.",
                    "You are in the teleporter room. To the West is the casino.", False, None)

SERVER = Room("The Server", None, None, None, 'CORRUPTED_R', None, False,
              "You feel dazed because of 'The Teleporter 9000'. You try to walk but you can't. Then you see \n"
              "a door to the west that is slightly open. You see blue light flickering true the bottom of \n"
              "the door. But then you see that their is a sight that dose not very much glows. It reads \n"
              "'YOU SHOULD NOT ENTER. IF YOU ENTER. YOU WILL CRASH THE WORLD AND He WILL COME. IF YOU ENTER \n"
              "WITHOUT THE PROPER MATERIALS. YOU WILL DIE. DON'T SAY YOU WEREN'T WORDED'. You wonder if you \n"
              "have the pieces.",
              "You are now in the server room.", False, None)

CORRUPTED_SERVER = Room("The Corrupted Server", 'CORRUPTED_R', 'SERVER', None, None, None, False,
                        "When you entered the room you felt a weired feeling in your stomach. Their was light on the \n"
                        "walls that wre in a patter like a circuit board. They slowly started to glow red. To the \n"
                        "North wall is a door that has a sign that reads 'To the Server'. To the East is to the \n"
                        "server room.",
                        "You entered the red room. To the East is the server room.", False, None)

CORRUPTED_R = Room("Corrupted Server", 'REFLECTIVE_R', None, 'CORRUPTED_R', None, None, False,
                   "You entered the door to the server room. Then you hear alarm bearing. The room turned red. \n"
                   "Then a speaker spoke, 'The World has been corrupted'.The speaker spoke that over and over. \n"
                   "Your ears. You try to find the panel for the speaker but it is not here. You must find it in \n"
                   "order to stop the speaker. To the North is a room filled with mirrors. You don't know why \n"
                   "their filled with mirrors, but they are. To the South is the corrupted room.",
                   "You entered the annoying room with the load speaker. To the North is a room filled with mirrors. \n"
                   "You don't know why their filled with mirrors, but they are. To the South is the corrupted room.",
                   False, None)

REFLECTIVE_R = Room("The Reflective Room", None, None, 'CORRUPTED_SERVER', 'COMPUTER_R', None, False,
                    "You enter the reflective room. Since you haven't found the panel to the speaker, you haven't \n"
                    "turned off the speaker or the blaring red light. So the mirrors is mostly reflecting red \n"
                    "light. To the South is the corrupted server and to the West is a room filled with complicated \n"
                    "electronics.",
                    "You have reached the reflected room with a bunch of mirrors. Why does it always have to be \n"
                    "mirrors. To the South is the corrupted server and to the West is a room filled with complicated \n"
                    "electronics.", False, None)

COMPUTER_R = Room("Computer Room", 'STONE_LIBRARY', 'REFLECTIVE_R', None, None, None, False,
                  "You reach the room filled with computers. You look at one of the computer screens and you \n"
                  "see that it is a blue screen. The blue screen had text on it. The text says 'The Server is \n"
                  "corrupted. Restarting in an hour'. To the North is door that is made out of stone. it appears \n"
                  "to be open. To the East is the room filled with mirrors.",
                  "You entered the room filled with computers. To the North is door that is made out of stone. it \n"
                  "appears to be open. To the East is the room filled with mirrors.", False, None)

STONE_LIBRARY = Room("STONE_LIBRARY", None, None, 'COMPUTER_R', 'GARDEN', None, False,
                     "You open the stone door. When you open the door, you see a huge library made up of stones. \n"
                     "You wonder why the stone door wasn't even locked. You go down the aile and you see that the \n"
                     "books are very old yet new. To the South is the computer room and to the West is a garden.",
                     "You entered the stone library. To the South is the computer room and to the West is a garden.",
                     False, None)

GARDEN = Room("Garden", None, 'STONE_LIBRARY', None, 'CASTLE_KITCHEN', None, False,
              "You reached the garden.The garden is filled with fruit and vegetables.You wonder why they \n"
              "will leave this beautiful garden with the fruit and vegetables ready to rip. Then you see \n"
              "their is an automated system at play but it had stopped. It had stopped because the server \n"
              "is corrupted. To the East is the stone library and to the west is a door with a picture of \n"
              "a slice of cake on it.",
              "You entered the amazing and beautiful garden. To the East is the stone library and to the west is a \n"
              "door with a picture of a slice of cake on it.", False, None)

CASTLE_KITCHEN = Room("Castle Kitchen", 'CASTLE_ENTRANCE', 'GARDEN', 'MAGIC_LIBRARY', 'THRONE_ROOM', None, False,
                      "You open the door to the door with the slice of cake on it. You see that it is the kitchen \n"
                      "for the castle. You see that their is no food or any ingredients anywhere to be seen. You \n"
                      "feel hungry so you look for the refrigerator. But their isn't any. So you just feel empty \n"
                      "inside. To the North is the castle entrance, to the East is the garden, to the South is a \n"
                      "bookshelf that has the work 'magic' on it and to the West are big doors.",
                      "You entered the castles kitchen. To the North is the castle entrance, to the East is the \n"
                      "garden, to the South is a bookshelf that has the work 'magic' on it and to the West are \n"
                      "big doors.", False, None)

MAGIC_LIBRARY = Room("Magic Library", 'KITCHEN', None, 'WATERFALL_R', None, None, False,
                     "You found the hidden library. All around you, you feel like something very dark and \n"
                     "mysterious things are around. Then you see a book started to drift away with a magenta aura. \n"
                     "Then use see another book but with a yellow aura around it. You don't want to fallow it \n"
                     "since it can be dangerous. To the North is the kitchen and to the South is a blue door.",
                     "You are now in the library with the books that can fly. To the North is the kitchen and to \n"
                     "the South is a blue door.", False, None)

WATERFALL_R = Room("Waterfall Room", 'MAGIC_LIBRARY', None, 'MINE_SHAFT', None, None, False,
                   "You enter the peaceful room with a waterfall. You wonder how such beauty is in a place such \n"
                   "like this. In the Room you see that a rainbow is trying to for but is sucked up from a tube in \n"
                   "the ceiling. It seems to be going to another place from the tube. To the North is the magic \n"
                   "library and to the South is the Mine shaft.",
                   "You entered the room with the beautiful water fall that seems to be out of place. To the North \n"
                   "is the magic library and to the South is the Mine shaft.", False, None)

MINE_SHAFT = Room("The Mine Shaft", 'WATERFALL_R', None, None, 'CAVERN', "Pickaxe", False,
                  "You have reached a mine shaft. You wonder why a place like this would even have a mine shaft \n"
                  "since it can randomly generate whatever it wants. Wait, you didn't know that? Oh well. The only \n"
                  "thing some what ordinary is that a pickaxe is here. To the North is the peaceful waterfall room \n"
                  "and to the West is a deeper part of the mine shaft.",
                  "Why did you come back to the mine if their really isn't anything here for you. To the North is \n"
                  "the peaceful waterfall room and to the West is a deeper part of the mine shaft.", False, None)

CAVERN = Room("Cavern", 'LOOPER', 'MINE_SHAFT', None, None, None, False,
              "You are now in the deeper part of the mine shaft. All that is around you is rock and some minerals. \n"
              "To the North is what look like a way out of the mine shaft and to the East is the mine shaft that \n"
              "had the pickaxe.",
              "You are now in the cavern with rock all around you. To the North is what look like a way out of the \n"
              "mine shaft and to the East is the mine shaft that had the pickaxe.", False, None)

LOOPER = Room("The Looper", None, 'THRONE_R', 'CAVERN', 'RAINBOW_R', None, False,
              "You are now in a room that is filled with side way eights. Then you remembered that side way eights \n"
              "is the infinity sign. Then you see that their is a neon sign that says 'The lopper'. To the East is \n"
              "a throne room, to the South is the cavern and to the West is a door that has rainbows all over the \n"
              "door.",
              "You are back to the Looper room. This sounds ironic. Does it to you? To the East is a throne room, \n"
              "to the South is the cavern and to the West is a door that has rainbows all over the door.", False, None)

THRONE_R = Room("Throne Room", None, 'CASTLE_KITCHEN', None, 'LOOPER', None, False,
                "You entered the throne room that is in the castle. You see that their is someone on one of the \n"
                "thrones. He looked like a king. But the way acted. he didn't seem like a king. To the East is \n"
                "the kitchen and to the West is the room that leads to somewhere else.",
                "You have came back to the impenetrable king. (For those who tried killing the king. You can't \n"
                "kill the king.). To the East is the kitchen and to the West is the room that leads to somewhere else.",
                False, None)

RAINBOW_R = Room("Rainbow Room", None, 'BLOOD_MOON_R', 'LOOPER', None, None, False,
                 "You have entered the room that has a bunch of rainbows. But they were in jars. They shouldn't be \n"
                 "in jars. Then you see that their is a pipe on the ceiling that seems to be the one that transports \n"
                 "the rainbow into this room. To the East is a door that you can't see into it and to the West is \n"
                 "a room that has an 8 on it.",
                 "You came back to the rainbow room. I guess you feel bad about the rainbows. No?. Then why did you \n"
                 "come back? To the East is a door that you can't see into it and to the West is a room that has an \n"
                 "8 on it.", False, None)

BLOOD_MOON_R = Room("Blood Moon Room", None, 'SECTION_3', None, 'RAINBOW_R', None, False,
                    "You enter the room that was dark inside. But as soon as you came in. You were able to see that \n"
                    "their was a blood moon on the ceiling. 'How is this possible?' you asked yourself. To the East \n"
                    "is a hallway that you can go to in 3 directions and to the West is a room with a rainbow door.",
                    "You have came back to admire the blood moon, right? To the East is a hallway that can go 3 \n"
                    "directions and to the West is a door with a rainbow door.", False, None)

SECTION_3 = Room("Section 3", None, 'LIGHT_R', 'CASTLE_ENTRANCE', 'BLOOD_MOON_R', None, False,
                 "You have made it to a 3-way section hallway. Their is nothing special in the hallway other than \n"
                 "that you can go 3 ways. To the East is a room that has a blinding light, to the South is the \n"
                 "entrance of a castle and to the West is a door that is red and inside is very dark.",
                 "You are now in the 3-way section. To the East is the room that has blinding light inside, to the \n"
                 "South is the castle entrance and to the West is a door that is red that is dark inside.", False, None)

CASTLE_ENTRANCE = Room("Castle Entrance", 'SECTION_3', None, 'CASTLE_KITCHEN', None, None, False,
                       "You are in the castle entrance. What are you going to do. You might find someone that can \n"
                       "help you understand what is going on. To the North is a 3-way section and to the West is the \n"
                       "castle's kitchen.",
                       "You are in the entrance of the castle's entrance. To the North is a 3-way section and to the \n"
                       "West is the castle's kitchen.", False, None)

LIGHT_R = Room("Light Room", None, 'BO_BO', None, 'SECTION_3', None, False,
               "You have reached the room that you couldn't see the inside. You were blinded and you can't see \n"
               "anything. To what you think is East is a room that has something on the door and to what I think is \n"
               "West is a door that is green?",
               "You enter the room that is blinding. Then you feel that something is in your pants pocket and that \n"
               "is a pair of sunglasses. You put them on and you can actually see things inside. To the East is a \n"
               "door that leads to a place called Bo Bo's room and to the West is a green door that leads to a \n"
               "3-way section. Then you put away the sunglasses. Forgetting about them. Even if you are blinded.",
               False, None)

BO_BO = Room("Bo Bo's room", 'PUZZLE_R', 'FORGOTTEN_R', None, 'LIGHT_R', None, False,
             "You finally reached the door to another room. This room was different. You have never been here \n"
             "before. Yet it is familiar. On the ceiling you see text that says 'Bo Bo's room'. You wonder who he is \n"
             "but you don't want to know. To the North is a rope that doesn't look like you can just cut it and to \n"
             "the West is a the horrible room filed with light.",
             "You entered Bo Bo's room. To the North is a room and to the West is a the horrible room filed with \n"
             "light.", False, None)

FORGOTTEN_R = Room("Forgotten Room", None, None, None, 'BO_BO', None, False,
                   "You enter the room that was well hidden. You asked yourself how you knew about it. It doesn't \n"
                   "matter now. In the room you see a bunch of bookshelves with books. In the room you see a paper \n"
                   "that someone has writen on it. You don't understand it. But then you see a key. It has 'P KEY' \n"
                   "written on it. To the West is Bo BO's room.",
                   "You really like going to hidden rooms don't you know. Bet you feel nice to see this hard to \n"
                   "find key. To the West is Bo Bo'd room", False, None)

PUZZLE_R = Room("Puzzle Room", None, None, 'BO_BO', None, None, False,
                "You enter the room that Gabe told you not to go their. 'The puzzle will be to hard' he said. You \n"
                "didn't care because you wanted everything to go back to normal. Then you saw a scroll and so you \n"
                "opened it. \n"
                "The Puzzle: \n"
                "If you had only one match, and entered a dark room containing an oil lamp, some newspaper, \n"
                "and some kindling wood, which would you light first? \n",
                "Are you going to solve the puzzle? if you are, here is the puzzle. \n"
                "The Puzzle: \n"
                "If you had only one match, and entered a dark room containing an oil lamp, some newspaper, \n"
                "and some kindling wood, which would you light first?", False, None)


end_game = "Once you have thought that the world was so easy, yet you didn't know how hard it was to survive all by \n"\
           "yourself. You saw yourself in a mirror as the wall changed around you. You couldn't do anything to \n"\
           "change that. You saw all your friends go by. there were inside the room. Behind a hidden door that you \n"\
           "didn't see when you first entered.\n"\
           "Thank you for playing my game. It was easy to make the game but I didn't really know what to do with \n"\
           "ending. So I decided to do some improve and created this end game text. Hope you enjoyed the game. :)"

print("You can end the game mid game by writing down 'quit' and entered it.")


current_node = BACK_MALL
directions = ['north', 'east', 'south', 'west']
short_directions = ['n', 'e', 's', 'w']

moves = 0

commands_possible = ["jump", "use", "armor", "attack damage", "drop", "description", "commands possible", "inventory",
                     "how to play",| "ability", "craft", "attack enemy", "grab"]


def others():
    if command == "jump":
        print("Whoosh. You jumped.")
    if command == "use":
        if len(current_character.inventory) != 0:
            print("What")
    if command == "grab":
        grab = input("What item do you want to grab? ")
        if grab in current_node.item:
            print("You grabbed %s." % grab)
            current_character.inventory.append(grab)
            print()
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Your Inventory:")
            print("\n".join(current_character.inventory))
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("Command not recognized")
    if command == "armor":
        print(current_character.armor)
    if command == "attack damage":
        print(current_character.damage)
    if command == "drop":
        drop = input("What item do you want to drop? ")
        if drop in current_character.inventory:
            print("You dropped %s" % drop)
            current_node.item.append(drop)
            current_character.inventory.pop(drop)
    if command == "description":
        print(current_character.description)
    if command == "inventory":
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Your Inventory:")
        print("\n".join(current_character.inventory))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if command == "how to play":
        print("How to play: \n"
              "You move around using North(N), East(E), South(S), and West(W). You can use commands possible to see \n"
              "a list of possible commands. The end goal is to find out why you are the only one in the current world.")
    if command == "commands possible":
        print(", ".join(commands_possible))
    if command == "heal":
        print("\n".join(current_character.inventory))
        heal = input("What would you like to use to heal? ")


while current_character.alive:
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
            print("command not recognized")
    else:
        print("health: %s" % current_character.health)
        print(current_node.name)
        print()
        if current_node.again:
            print(current_node.description_2)
        else:
            print(current_node.description)
            current_node.again = True
        command = input('>_').lower()
        if command in ['quit', 'end']:
            quit(0)
        else:
            if command in short_directions:
                pos = short_directions.index(command)
                command = directions[pos]
            if command in directions:
                try:
                    current_node.move(command)
                except KeyError:
                    print("Command not recognize")
                    print()
            if command in commands_possible:
                others()
            else:
                print("command not recognized")
    moves += 1
print("You have died.")
print("You died on move %s" % moves)
print("good luck next time.")
