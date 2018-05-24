import random

# Classes


class Item(object):
    def __init__(self, name, description, durability, base_durability, drop_item, amount):
        self.name = name
        self.description = description
        self.durability = durability
        self.base_durability = base_durability
        self.drop_item = drop_item
        self.amount = amount


class Enchanted(Item):
    def __init__(self, name, description, durability, base_durability, enchanted, drop_item, amount):
        super(Enchanted, self).__init__(name, description, durability, base_durability, drop_item, amount)
        self.enchanted = enchanted


class Key(Item):
    def __init__(self, name, description, durability, base_durability, door, drop_item, door_number, amount):
        super(Key, self).__init__(name, description, durability, base_durability, drop_item, amount)
        self.door = door
        self.door_number = door_number


class Edible(Item):
    def __init__(self, name, description, durability, base_durability, drop_item, amount):
        super(Edible, self).__init__(name, description, durability, base_durability, drop_item, amount)


class Armor(Item):
    def __init__(self, name, description, durability, base_durability, drop_item, amount, creatable):
        super(Armor, self).__init__(name, description, durability, base_durability, drop_item, amount)
        self.creatable = creatable


class Weapons(Item):
    def __init__(self, name, description, durability, base_durability, drop_item, damage, crafted,
                 amount):
        super(Weapons, self).__init__(name, description, durability, base_durability, drop_item, amount)
        self.crafted = crafted
        self.damage = damage

    # def broke(self):


class Potion(Edible):
    def __init__(self, name, description, durability, base_durability, drop_item, heal, ability, amount):
        super(Potion, self).__init__(name, description, durability, base_durability, drop_item, amount)
        self.heal = heal
        self.ability = ability


class Food(Edible):
    def __init__(self, name, description, durability, base_durability, heal, drop_item, amount):
        super(Food, self).__init__(name, description, durability, base_durability, drop_item, amount)
        self.heal = heal


class Lowhealth(Food):
    def __init__(self, name, description, durability, base_durability, heal, drop_item, amount):
        super(Lowhealth, self).__init__(name, description, durability, base_durability, heal, drop_item, amount)


class Maxhealth(Food):
    def __init__(self, name, description, durability, base_durability, heal, drop_item, amount):
        super(Maxhealth, self).__init__(name, description, durability, base_durability, heal, drop_item, amount)


class Healthpot(Potion):
    def __init__(self, name, description, durability, base_durability, drop_item, duration, ability, heal, amount):
        super(Healthpot, self).__init__(name, description, durability, base_durability, drop_item, duration, ability,
                                        amount)
        self.heal = heal


class Strengthpot(Potion):
    def __init__(self, name, description, durability, base_durability, duration, drop_item, ability, strength, amount):
        super(Strengthpot, self).__init__(name, description, durability, base_durability, duration, drop_item, ability,
                                          amount)
        self.strength = strength


class Resistancepot(Potion):
    def __init__(self, name, description, durability, base_durability, drop_item, duration, ability, armor, amount):
        super(Resistancepot, self).__init__(name, description, durability, base_durability, drop_item, duration,
                                            ability, amount)
        self.armor = armor


class Sword(Weapons):
    def __init__(self, name, description, durability, base_durability, drop_item, damage, crafted, amount):
        super(Sword, self).__init__(name, description, durability, base_durability, drop_item, damage, crafted, amount)


class Bow(Weapons):
    def __init__(self, name, description, durability, base_durability, drop_item, damage, distance, crafted,
                 amount):
        super(Bow, self).__init__(name, description, durability, base_durability, drop_item, damage, crafted, amount)
        self.distance = distance


class Staff(Weapons):
    def __init__(self, name, description, durability, base_durability, drop_item, damage, enchantment, armor,
                 crafted, amount, one_crafted):
        super(Staff, self).__init__(name, description, durability, base_durability, drop_item, damage, crafted,
                                    amount)
        self.enchantment = enchantment
        self.armor = armor
        self.one_crafted = one_crafted


class Characters(object):
    def __init__(self, name, inventory, health, damage, ranged_weapon, melee, mining_equipment,
                 description, diologue, hostile, alive, armor_type):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.damage = damage
        self.description = description
        self.diologue = diologue
        self.ranged_weapon = ranged_weapon
        self.melee = melee
        self.mining_equipment = mining_equipment
        self.hostile = hostile
        self.alive = alive
        self.armor_type = armor_type

    def attacking(self):
        escaped_d = False
        run_successful = False
        moved = False
        if current_node != FORGOTTEN_R:
            while current_node.enemies is not None or run_successful or not self.alive:
                self.damage = current_character.damage
                print("Your health is %s." % self.health)
                print()
                print("Your damage is %s." % self.damage)
                print("%s's health: %s " % (current_node.enemies.name, current_node.enemies.health))
                print()
                if current_node == FORGOTTEN_R:
                    print(Gabe.description)
                print()
                continue_1 = input("What would you like to do? \n1: Attack \n2: Escape \n3: Use item \n>_")
                if continue_1 == "1":
                    if current_node == FORGOTTEN_R:
                        print(len(Gabe.diologue(0)))
                    current_character.damage = current_character.melee.damage + current_character.ranged_weapon.damage
                    enemy_damage = random.randrange(current_node.enemies.damage, 0)
                    enemy_health = current_node.enemies.health
                    self.damage = random.randrange(self.damage, 0)
                    if self.damage == 0:
                        print("You missed.")
                        print("You didn't do any damage.")
                    else:
                        enemy_health -= self.damage
                        print("You did %s damage." % self.damage)
                        print()
                        print("%s's health is %s." % (current_node.enemies.name, enemy_health))
                    if enemy_damage == 0:
                        print("The %s missed." % current_node.enemies.name)
                        print("You didn't lose health.")
                    if enemy_health <= 0:
                        print("You killed %s.")
                        if current_node == FORGOTTEN_R:
                            print(len(Gabe.diologue(1)))
                    else:
                        self.health -= enemy_damage.damage
                        print("The enemy did %s damage." % enemy_damage)
                        if self.health == 0:
                            self.alive = False
                if continue_1 == "2":
                    if current_node == FORGOTTEN_R:
                        print("Sorry, but you cannot run when you are in combat with Gabe.")
                    else:
                        run_1 = random.randint(1, 6)
                        run_2 = random.randint(1, 6)
                        run = run_1 + run_2
                        if firework in current_character.inventory:
                            print("If you use the firework, you will have a 100 percent chance of escaping.")
                            use_firework = input("Would you like to use a firework? ").lower()
                            if use_firework == "yes":
                                print("You used the firework.")
                                print()
                                while not moved:
                                    try:
                                        moved = False
                                        escaped_d = random.randrange(directions)
                                        current_node.move(escaped_d)
                                    except KeyError:
                                        print("You can't go %s" % escaped_d)
                        else:
                            if run == 7:
                                print("You escaped successfully.")
                                run_successful = True
                                while not moved:
                                    try:
                                        moved = False
                                        escaped_d = random.randrange(directions)
                                        current_node.move(escaped_d)
                                    except KeyError:
                                        print("You can't go %s" % escaped_d)
                            else:
                                print("You didn't run successfully.")
                        current_character.damage += current_character.ranged_weapon.damage
                        current_character.damage += current_character.melee.damage
                        enemy_damage = random.randrange(current_node.enemies.damage, 0)
                        enemy_health = current_node.enemies.health
                        self.damage = random.randrange(self.damage, 0)
                        if self.damage == 0:
                            print("You missed.")
                            print("You didn't do any damage.")
                        else:
                            enemy_health -= self.damage
                            print("You did %s damage." % self.damage)
                            print()
                            print("%s's health is %s." % (current_node.enemies.name, enemy_health))
                        if enemy_damage == 0:
                            print("The %s missed." % current_node.enemies.name)
                            print("You didn't lose health.")
                        if enemy_health <= 0:
                            print("You killed %s.")
                        self.health -= enemy_damage.damage
                        print("The enemy did %s damage." % enemy_damage)
                        if self.health == 0:
                            self.alive = False
                if continue_1 == "3":
                    for uses in current_character.inventory:
                        if uses in usable:
                            print(uses.name)
                    consumable = input("What item would you like to use? ")
                    if consumable in current_character.inventory:
                        self.health += consumable.heal  # Help
                else:
                    print("There aren't any enemies here.")


class Room(object):
    def __init__(self, name, north, east, south, west, item_i, repeat, description, description_2, stayed,
                 enemies=None):
        self.name = name
        self.description = description
        self.description_2 = description_2
        self.stayed = stayed
        self.item_i = item_i
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
             "The TR Key seems to open a door that is locked. Which door that can be is unknown.", None, None,
             'teleporter_R', True, 0, 1)

p_key_1 = Key("P Key #1",
              "The first key seems to not be the only key.", None, None, 'puzzle_R', True, 1, 1)

p_key_2 = Key("P Key #2",
              "The second key seems to not be the only key.", None, None, 'puzzle_R', True, 1, 1)

p_key_3 = Key("P Key #3",
              "The third key seems o not be the only key.", None, None, 'puzzle_R', True, 1, 1)

p_key_4 = Key("P Key #4",
              "The Last key seems to not be the only key. Their is a note in the back. It reads 'You must have all \n"
              "of the keys in order to be in the puzzle room.'", None, None, 'puzzle_R', True, 1, 1)

# Armor
beginner_armor = Armor("beginner armor",
                       "This armor is what you start of with at the beginning of the ga- I mean you start of with.",
                       2000, 2000, False, 1, False)

leather_armor = Armor("leather armor",
                      "This armor type is the weakest armor possible.", 20, 20, True, 0, False)

wood_armor = Armor("wooden armor",
                   "This armor is made complete made of flexible wood.", 30, 30, True, 0, True)

iron_armor = Armor("iron armor",
                   "This armor is made of iron bars.", 45, 45, True, 0, True)

gold_armor = Armor("gold armor",
                   "This armor is made of gold bars. It is extremely heavy and it doesn't block a lot of hits.", 35, 35,
                   True, 0, True)

diamond_armor = Armor("diamond armor",
                      "This armor is made from diamonds.", 150, 150, True, 0, True)

armor_of_undying = Armor("ARMOR OF UNDYING",
                         "The armor of undying will revive you when you die. But when the armor revives you, it will \n"
                         "break and you will not have the armor anymore.", 1, 1, True, 0, True)

armor_of_strength = Armor("ARMOR OF STRENGTH",
                          "The armor of strength will give you extra damage. But when you attack, you will lose 5% \n"
                          "of your base health(100).", 250, 250, True, 0, True)

armor_shell = Armor("armor shell",
                    "This armor shell is used so that you can make armor.", 1, 1, True, 0, True)

# Extras
candle = Item("candle",
              "This candle can be use so that you can burn something. But what?", 1, 1, True, 1)

torch = Item("torch",
             "This torch can be used to burn something. But what?", 1, 1, True, 1)

pickaxe = Item("a diamond pickaxe",
               "This item seams to be used to mine hard to get materials. Which material it is unknown. Maybe you \n"
               "will find it somewhere.", 1, 1, True, 1)

rainbow_in_a_bottle = Healthpot("rainbow in a bottle",
                                "The rainbow in the bottle fills you up with warmth. It is almost as if it can heal \n"
                                "you.", 5, 5, True, 0, "heal", 20, 1)

paper_with_writing = Item("blueprint: paper with writing",
                          "The piece of paper that you found has writing in it. it reads 'You Must find the puzzle \n"
                          "room. if you don't we will never escApe. who ever you are, you Must find us. we are \n"
                          "Trapped. we Can't find tHe exit. you must pass the test in order to free us. hope you are \n"
                          "come quickly. we care running out of food. You must also craft the legendary armor of \n"
                          "undying. That is if you are worth it. You can craft it using cosmonium ingots.'", 1, 1, True,
                          1)

staff_of_emerged_power_blueprint = Item("blueprint: staff of emerged power",
                                        "This is a piece of paper has a blueprint for the staff of emerged power. \n"
                                        "You need 10 sticks, 5 diamonds, and a cosmonium ingot.", 1, 1, True, 1)

staff_of_healing_blueprint = Item("Blueprint: staff of healing",
                                  "This is a piece of paper has a blueprint for the staff of healing. You need \n"
                                  "10 sticks, 2 diamonds, and 4 cosmonium ingots.", 1, 1, True, 1)

camera = Item("camera",
              "You look at the camera. You wonder if they are any photos inside it.", 1, 1, True, 1)

firework = Item("firework",
                "Its a firework. It goes BOOM.", 1, 1, True, 0)

wallet = Item("wallet",
              "It is a wallet with some money in it. But you don't even need it.", 1, 1, True, 1)

armor_glue = Item("bottle of armor glue",
                  "This item can help make better armor.", 100, 100, True, 200)

gunpowder = Item("gunpowder",
                 "This item will help make crossbow bolts.", 1, 1, True, 300)

battery = Item("battery",
               "This item is used to make items or weapons have an electric conduct.", 100, 100, True, 0)

charger = Item("charger",
               "This item is to charge up the durability of the battery.", 200, 200, True, 0)

wire = Item("wire",
            "This item is used to craft batteries.", 1, 1, True, 10)

# Materials
iron_ore = Item("iron ore",
                "This material is used to make iron bars.", 1, 1, True, 0)

iron_bar = Item("iron bar",
                "This material is used to craft armor and weapons.", 1, 1, True, 1)

gold_ore = Item("gold ore",
                "This material is used to make gold bars.", 1, 1, True, 0)

gold_bar = Item("gold bar",
                "This material is used to craft armor and weapons.", 1, 1, True, 0)

uncut_diamond = Item("uncut diamond",
                     "This material is used to make diamonds.", 1, 1, True, 0)

diamond = Item("diamond",
               "This material is used to craft very strong armor and complex electronics.", 1, 1, True, 0)

cosmonium_ore = Item("COSMONIUM ORE",
                     "This material is very hard to find. It is harder than diamond and has the power to revive you. \n"
                     "You need to craft the cosmonium ingot.", 9, 9, True, 50)

cosmonium_ingot = Item("COSMONIUM INGOT",
                       "This material is hard to craft. It can be used to craft legendary or to craft unstable items.",
                       2, 2, True, 0)

wood = Item("wood",
            "This material is the weakest material. it can be used to make sticks. One wood makes 4 sticks", 1, 1, True,
            39)

sticks = Item("sticks",
              "This material is used to make items that need a wooden handle.", 1, 1, True, 0)

stone = Item("stone",
             "This material is used to make stone parts.", 1, 1, True, 15)

sharpening_stone = Item("sharpening stone",
                        "This stone is used so that you can sharpen tools. Has a small chance of giving durability \n"
                        "to the tool", 40, 40, True, 0)

sand = Item("sand",
            "This is sand.", 1, 1, True, 0)

magical_stone = Item("magical stone",
                     "This material is used to make magical items.", 1, 1, True, 5)

# Weapons
dull_sword = Sword("dull sword",
                   "This sword is dull.", 100, 100, True, 8, False, 1)

sharp_sword = Sword("sharp sword",
                    "This sword is so sharp, it can cut stone.", 50, 50, True, 73, True, 0)

magical_sword = Sword("MAGICAL SWORD",
                      "This sword seems magical. It is glowing with a purple glow.", 230, 230, True, 99, True, 0)

broken_bow = Bow("broken bow",
                 "The bow is broken. you can use it but it might now do a lot of damage.", 14, 14, True, 11, 13, False,
                 1)

x_bow = Bow("x-bow",
            "You have a cross bar.", 300, 300, True, 46, 38, False, 1)

metal_bow = Bow("metal bow",
                "The bow has been reinforced with iron.", 200, 200, True, 73, 74, True, 0)

legendary_bow = Bow("LEGENDARY BOW",
                    "This bow is a reinforced bow that has 3 enchantments with it.", 999, 999, True, 300, 235, True, 1)

staff_of_healing = Staff("staff of healing",
                         "This staff is used to heal yourself.", 50, 50, True, 0, 'heal', 0, True, 1,
                         False)

staff_of_emerged_power = Staff("STAFF OF EMERGED POWER",
                               "This staff can one shot anything in the game. You can only make it once in the game. \n"
                               "But it only has one durability. So use it wisely.", 1, 1, True,
                               999999999999999999999999999999999999999999999999999999, 0, True, 0, False, False)

# Potions
weak_health_potion = Potion("weak health potion",
                            "This health potion gives you 20 health back.", 1, 1, True, 1, 20, 0)

strong_health_potion = Potion("strong health potion",
                              "This health potion gives you 50 health back.", 1, 1, True, 1, 40, 0)

strength_potion = Potion("strength potion",
                         "This strength potion gives you an attack boost for 30 moves.", 1, 1, True, 1, 10, 0)

poison_potion = Potion("POISON IN A BOTTLE",
                       "This potion can be thrown and will poison the enemy. The poison will not kill the enemy. The \n"
                       "enemy will do less damage and will have less health", 1, 1, True, 1, 50, 0)

# Food
raw_potato = Food("raw potato",
                  "You can eat this raw potato. But it looks so weird.", 1, 1, 5, True, 0)

cooked_potato = Food("cooked potato",
                     "This potato is cooked.", 1, 1, 15, True, 0)

potato_chip = Food("potato chips",
                   "Its a bag of chips.", 1, 1, 20, True, 20)

raw_meat = Food("raw meat",
                "This is a piece of raw meat from an unknown creature.", 1, 1, 30, True, 40)

cooked_meat = Food("cooked meat",
                   "This is a piece of cooked meat from the oven.", 1, 1, 50, True, 0)

unicorn_meat = Food("UNICORN MEAT",
                    "Despite its name, it is not from a unicorn. It is just called that because it is extremely rare. "
                    "Tho it is does \n have a little bit of a rainbow color. But it is just food dye.", 1, 1, 80, True,
                    20)

# Brewing items
glass = Item("glass",
             "This is sand that has been heated up to see thorough.", 1, 1, True, 0)

glass_bottle = Item("empty glass bottle",
                    "This is a bottle made of glass.", 1, 1, True, 0)

sham_pow = Item("sham-Pow",
                "This is a good cleaning rag.", 90, 90, True, 1)

dirty_glass_bottle = Item("dirty glass bottle",
                          "This is a used glass bottle.", 1, 1, True, 0)

heal_flower = Item("heal flower",
                   "This flower has the power to heal.", 1, 1, True, 1)

power_stone = Item("power stone",
                   "This stone has the power to give someone strength.", 1, 1, True, 0)

elf_leaf = Item("elf leaf",
                "this leaf has the power to give someone poison.", 1, 1, True, 0)

broken_bottle = Item("broken bottle",
                     "This is a broken bottle that has broken when you tried to make a potion.", 1, 1, True, 0)

# Characters
Gabe = Characters("Gabe", [pickaxe, torch, wallet], 100, 20, "sword", "pickaxe", None,
                  "The Enemies name is Gabe, he is one of the hardest people to fight. He have killed many people for "
                  "trying to \nsolve the puzzle. They never got to the question so they weren't able to tell people "
                  "the question.",
                  ["It is I, Gabe, the one that changed the world. If you want to get your family and friends and "
                   "everyone in your \nworld back, you have to get past me.", "In order to solve you family, you need "
                   "to solve the puzzle.",
                   "You have defeated me. You may solve the riddle. But be worn. If you don't solve it within your "
                   "third try, you \nwill die. So be worn."], False, True, "golden armor")

current_character = Characters("John", [], 100, 10, "broken bow", None, None,
                               "You are yourself. Don't let anyone change that.", None, False, True, "beginner armor")

# Enemies

stickboss = ("THE STICK BOSS", None, 999999, 99, 30, None, None, None,
             "This boss is the stick boss. It is supper hard. It only has one weakness. You can only attack it if you "
             "make it \nmad.", None, False, True, None)

Dogboss = ("THE DOG BOSS", None, 200, 40, 10, None, None, None,
           "This boss is some-what hard. It has one weakness.", None, True, True, None)

witchboss = ("WITCH BOSS", None, 400, 45, 20, None, None, None,
             "This boss is harder than the Dog boss. But easier than the boss boss. It doesn't have a weakness. You "
             "just got \nto fight it.", None, True, True, None)

guarddog = ("guard dogs", None, 20, 10, 30, None, None, None,
            "This is a guard dog. They spawn near the dog boss.", None, True, True, None)

wasp = ("wasp", None, 5, 10, 20, None, None, None,
        "This enemies comes in herds. They may be weak, but they do a ton of damage if they work together.", None, True,
        True, None)

treearmy = ("tree army", None, 100, 30, 50, None, None, None,
            "These trees seem normal at first, but they have a magical property to move and attack. They would not "
            "attack, \nas long as you don't do anything to them.", None, False, True, None)

wonbers = ("wonbers", None, 100, 50, 70, None, None, None,
           "This is a wonbers. They do a lot of damage.", None, True, True, None)

# Initialize Rooms
BACK_MALL = Room("Back of the Mall", 'TARGET', None, 'FRONT_STORE', 'OREO_FACTORY', [], False,
                 "You are in the back of the mall. You wonder were you are and how you got here. You see Target to "
                 "North and the \nfront of a store to the south.",
                 "You are in the back of the mall. You see Target in the North and the front of a store to the south.",
                 False, None)

FRONT_STORE = Room("Front of Store", 'BACK_MALL', 'WOODWORK_SECTION', None, 'SIDE_ENTRANCE', [], False,
                   "The store is a convenient store that has been here for a while. To the North is the back of a \n"
                   "mall, to the East \nis the Woodwork section, and to the West is an entrance to an abandoned house.",
                   "You reached the cashier of the convenient store. To the East is the Woodwork section, and to the "
                   "West is an \nentrance to an abandoned house", False, None)

TARGET = Room("Target", 'WALMART', 'HOME_D', 'BACK_MALL', 'OFFICE_D', [], False,
              "You have entered Target and walked through. You have triggered the metal detector and was kicked out of "
              "the \nstore. Walmart is to the North, Home Depot is in the East, Office Depot is in the West, and to "
              "the South is the \nback of the mall.",
              "You are now in front of Target. Walmart is to the North, Home Depot is in the East, Office Depot is to "
              "the \nWest, and to the South is the back of the mall.", False, None)

OFFICE_D = Room("Office Depot", 'BANANA', 'HOME_D', None, 'CAR', [wire], False,
                "You have entered Office Depot and didn't want to go thought because of what happened with Target. To "
                "the West \nis Target and to the East is the left of the mall.",
                "You are outside of Office Depot. To the West is Target and to the East is the left of the mall.",
                False, None)

CAR = Room("The Car", None, 'OFFICE_D', None, 'PARKING', [], False,
           "You found your car. But you left your keys in an unknown area, so you can't get in. To the East is Office "
           "Depot \nand to the West in the Parking lot.",
           "You are now near you car. To the East is Office Depot and to the West in the Parking lot.", False, None)

PARKING = Room("Parking Lot", 'CAVE', 'CAR', 'FRONT_HOUSE', 'TRUCK', [], False,
               "You have reached the parking lot. Their are a lot of cars in the parking lot to visit the bat cave. To "
               "the \nNorth is the bat cave, to the East is were your car is at, to the South is the front of a house "
               "and to the west \nis a taco truck.",
               "You reached the parking lot fulled with car but with no one around. To the North is the bat cave, to "
               "the East \nis were your car is at, to the South is the front of a house and to the west is a taco "
               "truck.", False, None)

TRUCK = Room("Taco Truck", None, 'PARKING', None, None, [], False,
             "You smell a the tacos that are in the truck. You want to buy a taco because you are hungry but you don't "
             "have \nany money. To the East is the parking lot.",
             "You are now near the taco truck. To the East is the parking lot.", False, None)

BANANA = Room("The Banana Store", 'SERVER_R', None, 'OFFICE_D', None, [], False,
              "You have reached the famous store from the Banana company. You want to go in but you don't have any "
              "intentions \ntheir. To the North is a fence that is locked with unbreakable chains with a lock on a "
              "door that doesn't look \nlike a normal key. To the South is Office Depot.",
              "You are now outside of the ever so famous banana store from Banana.inc. To the North is a fence that is "
              "locked \nwith unbreakable chains with a lock on a door that doesn't look like a normal key. To the "
              "South is Office Depot.", False, None)

HOME_D = Room("Home Depot", None, None, None, 'TARGET', [], False,
              "You have reached Home Depot. You don't want to go inside because it you have nothing to do in their. "
              "You wonder \nif you could steal something since their is no one around. They wont notice it gone. To "
              "the East is the left of \nmall and to the West is Target.",
              "You reached outside of Home Depot. To the East is the left of mall and to the West is Target.", False,
              None)

WALMART = Room("Walmart", None, 'LEFT_MALL', None, 'Target', [], False,
               "You have reached Walmart. You don't want to go inside because it you have nothing to do in their. To "
               "the East \nis the left of mall and to the West is Target.",
               "You are now outside of walmart. To the East is the left of mall and to the West is Target.", False,
               None)

CAVE = Room("The Bat Cave", None, None, 'PARKING', None, [staff_of_emerged_power_blueprint, tr_key], False,
            "You have reached the bat cave but no one is here. It is strange that no one whn their is a full parking "
            "lot. To \nthe South is the parking lot.",
            "You are now outside of the cave. You still wonder why this is a wonderful cave to visit if they are so "
            "many \ncars in the parking lot. To the South is the parking lot.", False, None)

SIDE_ENTRANCE = Room("Side Entrance of the House", 'OREO_FACTORY', 'FRONT_STORE', 'KITCHEN', 'HALL', [], False,
                     "You have reached the side entrance of the house. You enter the creepy house. To the North their "
                     "is a Oreo \ncookie factory, to the East is the front of the store, to the South is the kitchen "
                     "and to the West is the \nhallway.",
                     "You are now inside of the creepy house. To the North  their is a Oreo cookie factory, to the "
                     "East is the front \n"
                     "of the store, to the South is the kitchen and to the West is the hallway.", False, None)

KITCHEN = Room("Kitchen", 'SIDE ENTRANCE', None, None, 'LIVING_R', [potato_chip], False,
               "You have reached the kitchen. You don't see anything but a bunch of cabinets. To the North is the side "
               "entrance \nof the house and to the West is the living room.",
               "You enter the kitchen of the creepy house. To the North is the side entrance of the house and to the "
               "West is \nthe living room.", False, None)

HALL = Room("The Hall", 'FRONT_HOUSE', 'SIDE _ENTRANCE', 'LIVING_R', None, [], False,
            "You are in the hallway of the creepy house. In the hallway you can see that there is a book that seems to "
            "want \nyou are trying to do. If you know what to do that is. To the North is a door leading to the "
            "outside, to the \nEast is a door with a carpet that has an eye on it and to the South is what looks like "
            "the living room.",
            "You enter the hallway to the creepy house with the book that does nothing. To the North is a door leading "
            "to \nthe outside, to the East is a door with a carpet that has an eye on it and to the South is what "
            "looks like the \nliving room.", False, None)

LIVING_R = Room("Living Room", 'HALL', 'KITCHEN', None, 'CORRIDOR', [], False,
                "You reached the living room. There seem to be a maze with the couches. You pass the maze. To the "
                "North is the \nhallway, to the East is the kitchen and to the West is a corridor.",
                "You reached the living room. You don't want to do the maze again so you go over the couches. To the "
                "North is \nthe hallway, to the East is the kitchen and to the West is a corridor.", False, None)

CORRIDOR = Room("Left Corridor", 'TROPHY_R', 'LIVING_R', 'SHRINE_R', 'DARK_R', [], False,
                "You find yourself in a cross way inside the house. There is a door to the North that is slightly open "
                "that \nseems to have something bright coming from the room, to the East is the living room, to the "
                "South is a \nbookshelf with books about God and to the West is a room that is dark inside.",
                "You find yourself in a hallway that leads you to four places. There is a door to the North that is "
                "slightly \nopen that seems to have something bright coming from the room, to the East is the living "
                "room, to the South is \na bookshelf with books about God and to the West is a room that is dark "
                "inside.", False, None)

TROPHY_R = Room("Trophy Room", None, None, 'CORRIDOR', None, [], False,
                "You find yourself in a room filled with trophy's. You see trophy's of Swimming, Cross Country, "
                "Football and \nSoccer. There are also some posters that are all around the room that are athletes. "
                "All you can go is to the \nSouth.",
                "You reached the room that is filled with the trophy's. All you can go is to the South.", False, None)

SHRINE_R = Room("Shrine Room", 'CORRIDOR', None, 'SOUTH_HOUSE', None, [candle], False,
                "You push the bookshelf to find out that it is a hidden door. You found a room that seems to be a "
                "shrine. You \nsee a picture of a boy that seems to be around 20 years old. You see food, drinks, and "
                "candles that have \ncobwebs around them. To the North is the secret bookshelf door that leads to the "
                "corridor and to the South it \nseems to lead outside.",
                "You enter the somewhat creepy shrine room. To the North is the secret bookshelf door that leads to "
                "the corridor \nand to the South it seems to lead outside.", False, None)

SOUTH_HOUSE = Room("South of House", 'SHRINE_R', None, None, None, [torch], False,
                   "You open the door to the outside and you you see a torch that is just sitting their. It fills you "
                   "up with hope \njust to remember that you are all alone in this town. To the North is the shrine "
                   "room.",
                   "You reached the south part of the house. To the North is the shrine room.", False, None)

DARK_R = Room("The Dark Room", 'SCARY_R', 'CORRIDOR', None, 'WEST_HOUSE', [camera], False,
              "You reached a dark room. You can't see anything in the room. Yo felt something in the back of your leg. "
              "It \nfeels like a camera. You hear scary sounds in the room to the North, to the East is the corridor "
              "and to the \nWest you hear birds chirping.",
              "You entered the dark room. You wonder why they didn't have some kind of light source in the room. You "
              "hear \nscary sounds in the room to the North, to the East is the corridor and to the West you hear "
              "birds chirping.", False, None)

SCARY_R = Room("Scary Room", None, None, 'DARK_R', None, [p_key_2], False,
               "You enter the scary room  to find that the monitor of a computer was on. It was playing scary music "
               "from \nYoutube. You wonder why you they will leave it running. Then you see a key that came shooting "
               "out of the wall \nbehind a painting. It is a key. A shiny blue key that says 'P key 2 KEEP HIDDEN'. "
               "You wonder why they didn't \ntake it. To the South is the scary room.",
               "You enter the scary room. To the South is the scary room.", False, None)

WEST_HOUSE = Room("West of House", None, 'DARK_R', None, None, [], False,
                  "You leave the house and reached the west side of the house. You can't go anywhere because it is "
                  "surrounded by \nbushed and thick trees. The only way you can go is to the dark room to the East.",
                  "You are now in the west of the house. You can only go to the East.", False, None)

WOODWORK_SECTION = Room("Woodwork section", None, None, 'WALKWAY', 'FRONT_STORE', [], False,
                        "You go to the woodwork section. Their is a lot of wood that has been cut down and but into To "
                        "the South is a \nWalkway and to the West is the front of the store.",
                        "You are now in the woodwork section. To the South is a Walkway and to the West is the front "
                        "of the store.", None)

WALKWAY = Room("Walkway", 'WOODWORK_SECTION', 'BOX_R', 'BOOK_SECTION', None, [], False,
               "You find yourself in the walkway of the store. You find yourself in a three-section. To the North is "
               "the \nwoodwork section, to the East is the box room and to the South is the book section.",
               "You are in the wall way of the store. You wonder why this is the only one you can go. That is because "
               "the \nothers are blocked. To the North is the woodwork section, to the East is the box room and to the "
               "South is the \nbook section.", False, None)

BOX_R = Room("The Box Room", None, 'MEAT_SECTION', None, 'WALKWAY', [], False,
             "You enter the box room that seems to be for employee only. The only thing that is in the room are boxes. "
             "Boxes. \nAnd more boxes. boxes with wood and books. To the East is the Meet section and to the West is "
             "the walkway.",
             "You enter the room filled with boxes. To the East is the Meet section and to the West is the walkway.",
             False, None)

MEAT_SECTION = Room("Meat Section", None, None, 'MIRROR_R', 'BOX_R', [gunpowder, raw_meat], False,
                    "You reach the meat section of the store. It was all empty but the cow meat section. You want to "
                    "take the meat \nbut you don't because it is stealing. To the South is a room full of mirrors and "
                    "to the West is the box room.",
                    "You reached the meat section of the store. To the South is a room full of mirrors and to the West "
                    "is the box \nroom.", False, None)

MIRROR_R = Room("Mirror Room", 'MEAT_SECTION', 'THE_ROOM', None, None, [], False,
                "You have reached the mirror room and all you see is yourself. ou seemed like you have seen better "
                "days. You \nhave baggy clothes and you have shorts. To the North is the meat section and to the East "
                "in a door with a \ncaption 'The Room'.",
                "You enter the room that is filled with mirrors. To the North is the meat section and to the East in a "
                "door with \na caption 'The Room'.", False, None)

THE_ROOM = Room("The Room", None, None, None, 'MIRROR_R', [], False,
                "You enter the mysterious room called the room. You can't see a lot of things since the room is dimly "
                "lit. All \nyou can really see is that people have been here. It is all messy as if they were looking "
                "for something. They \nprobably found it or game up since they was a corner of the room that was neat "
                "and clean. To the West is the \nMirror room.",
                "You entered the not so mysterious room. To the West is the Mirror room.", False, None)

BOOK_SECTION = Room("Book Section", 'WALKWAY', None, 'BACK_STORE', 'CLOTHING_SECTION', [], False,
                    "You reach the book section of the store. You see famous books in the 'Famous book section'. Their "
                    "were books \nfrom the 'Harry Potter' series and the books series of 'Percy Jackson and the "
                    "Olympians'. To the North is the \nWalkway, to the South is a door that is leading outside and to "
                    "the West is the clothing section.",
                    "You entered the book section of the store. To the North is the Walkway, to the South is a door "
                    "that is leading \noutside and to the West is the clothing section.", False, None)

CLOTHING_SECTION = Room("Clothing Section", None, 'BOOK_SECTION', None, None, [leather_armor], False,
                        "You reach the clothing section. You see lines of clothes missing. The only thing you see is "
                        "armor that seems to \nfit you. It seems to be made out of chain mail armor. To the East is "
                        "the book section of the store.",
                        "You entered the clothing section of the store. To the East is the book section.", False, None)

BACK_STORE = Room("Back of Store", 'BOOK_SECTION', 'SCHOOL_HOUSE', None, None, [], False,
                  "You reached the back of the store. You see a garbage can that is full of trash. You see a graffiti "
                  "that says \n'HE CAME'. What that meant was a mystery. To the North is the book section and to the "
                  "East is a school House.",
                  "You are now at the back of the school. To the North is the book section and to the East is the "
                  "school house.", False, None)

SCHOOL_HOUSE = Room("School House", None, None, None, 'BACK_STORE', [], False,
                    "You reached the front of a small school house that looks like it was from the 1800's. You try to "
                    "open the door \nbut it is locked. You try to find another way in but their isn't. inside seems to "
                    "be some desk that has a \ncomputer that is unreachable. On the screen it says 'THE MAP' in big "
                    "letters. But because it was so far away \nthat you couldn't read what was below it. So you leave "
                    "it light that. To the West is the back of the store.",
                    "You reached the school house. To the West is the entrance back to the store.", False, None)

OREO_FACTORY = Room("The Oreo Cookie Factory", None, 'BACK_MALL', 'SIDE_ENTRANCE', None, [], False,
                    "You reached the ever so popular Oreo cookie factory. You go inside and you find packs among packs "
                    "of double \nstuffed Oreo's. You leave the Oreo factory and you walk out the door. Then you notice "
                    "a pack of mega stuffed \noreo's. To the East is the back of the mall and to the South is the side "
                    "entrance to a scary looking house.",
                    "You came back to the Oreo Factory. To the East is the back of the mall and to the South is the "
                    "side entrance to \na scary looking house.", False, None)

FRONT_HOUSE = Room("The Front of the House", 'HALL', None, None, 'PARKING_LOT', [], False,
                   "You are at the front of the house. You knock on the door to see if anyone is their. No one answers "
                   "so you just \nopen the door. You see that the door isn't unlocked. You open the door, enter the "
                   "house and closed the door. To \nthe North is the parking lot and to the South is the hallway.",
                   "You are now in front of the scary house. To the North is what looks like a parking lot and to the "
                   "south is a \nhallway.", False, None)

LEFT_MALL = Room("Left of Mall", None, None, 'ALLEYWAY', 'WALMART', [p_key_3], False,
                 "You reach the left side of the mall. You see trash cans that don't have anything. You look inside "
                 "and their \nseems to be a graffiti that says 'He is near'. You get out of the garbage bin and you "
                 "think for a bit. You \nwonder why they put that their. To the South is an alley and to the West is "
                 "Walmart.",
                 "You are now in the left side of the mall. To the South is the alley way and to the West is "
                 "Walmart", False, None)

ALLEYWAY = Room("The Alleyway", 'LEFT_MALL', 'CASINO', 'GARBAGE_TRUCK', None, [], False,
                "You reach an alleyway. Their isn't much that is here other than a piece of paper with a clown, a "
                "bear, a \nballerina, and a puppet. You see that it familiar in a way but you couldn't place it. To "
                "the North is the left \nof the mall, to the East is a Casino and to the South seems to have a garbage "
                "truck parked outside.",
                "You reached the alleyway of the mall. To the North is the left of the mall, to the East is a Casino "
                "and to the \nSouth seems to have a garbage truck parked outside.", False, None)

CASINO = Room("The Casino", None, None, 'RESTAURANT', 'ALLEYWAY', [], False,
              "You reach the Casino's entrance. You can't enter the casino because you are not 18 years or older. So "
              "you just \nwait outside as you hear slot machines ringing to announce the winner and hear people "
              "talking. To the East is a \ndoor that is floating. You don't know how but it is. In front of the door "
              "has a sign that reads 'you need a \nkey. You that walks and can talk.' Have you seen a key that can do "
              "that? To the South is a restaurant and to \nthe West is the alleyway.",
              "You are outside of the casino. To the South is a restaurant and to the West is the alleyway.", False,
              None)

GARBAGE_TRUCK = Room("The Garbage Truck", 'ALLEYWAY', 'STAR_RESTAURANT', None, None, [paper_with_writing, armor_glue],
                     False,
                     "You reached the Garbage truck. When you reach their, you see that the passenger seat s open. "
                     "You enter the \ngarbage truck and their seems to be a key of some sort. Their is also a piece of "
                     "paper that has some writing \non it. To the North is the alleyway and to the East is a "
                     "restaurant.",
                     "You are next to the garbage truck. To the North is the alleyway and to the East is a "
                     "restaurant.", False, None)

RESTAURANT = Room("The 5 star Restaurant", 'CASINO', None, 'CORNER', 'GARBAGE_TRUCK', [], False,
                  "You reached the 5 star restaurant. You feel hungry but you put that feeling away since you you "
                  "don't have any \nmoney. To the North is a Casino, to the South seems to be a corner and to the west "
                  "is a garbage truck.",
                  "You are now in front of the 5-star restaurant. To the North is a Casino, to the South seems to be "
                  "a corner and \nto the west is a garbage truck.", False, None)

CORNER = Room("The Corner", 'RESTAURANT', 'CHINESE_RESTAURANT', None, None, [], False,
              "You reached the corner of the 5 star restaurant and you turn. You see a chinese restaurant that seems "
              "to be \nabandoned because of its location. You see that the walls are being torn by the weather and the "
              "windows are \nbroken. To the North is the 5 star restaurant and to the West is the chinese restaurant.",
              "You reached the corner of the of the alleyway. To the North is the 5 star restaurant and to the West is "
              "the \nchinese restaurant.", False, None)

CHINESE_RESTAURANT = Room("The Abandoned Chinese Restaurant", None, None, 'CORNER', None, [], False,
                          "You reached the abandoned chinese restaurant and you go inside. You see that the their was "
                          "a lot of people that \nuse to go here because of so any tables and chairs. You see burn "
                          "marks on the wall and you wonder if their was \na fire. To the West is the corner of the 5 "
                          "star \n restaurant.",
                          "You are now in the parking lot of the abandoned restaurant. To the West is the corner of "
                          "the 5 star restaurant.", False, None)

TELEPORTER_R = Room("The Teleporter Room", None, None, None, 'CASINO', [], False,
                    "You enter the door that was floating bit because you hold the key near it stopped floating and "
                    "reached the \nfloor. You put the key in the key hole and the door opens. You take the key and you "
                    "go inside. Inside seems to \nhave a bunch of wire and a pod in the middle. The pod had a name. "
                    "The name was 'The Teleporter 9000'. Their was \nalso a command center but you didn't touch it. To "
                    "the West is the casino.",
                    "You are in the teleporter room. To the West is the casino.", False, None)

SERVER = Room("The Server", None, None, None, 'CORRUPTED_R', [], False,
              "You feel dazed because of 'The Teleporter 9000'. You try to walk but you can't. Then you see a door to "
              "the west \nthat is slightly open. You see blue light flickering true the bottom of the door. But then "
              "you see that their \nis a sight that dose not very much glows. It reads: \n'YOU SHOULD NOT ENTER. IF "
              "YOU ENTER. YOU WILL CRASH THE WORLD AND He WILL COME. IF YOU ENTER WITHOUT THE PROPER \nMATERIALS. YOU "
              "WILL DIE. DON'T SAY YOU WEREN'T WORDED'. You wonder if you have the pieces.",
              "You are now in the server room.", False, None)

CORRUPTED_R = Room("The Corrupted Room", 'CORRUPTED_SERVER', 'SERVER', None, None, [], False,
                   "When you entered the room you felt a weired feeling in your stomach. Their was light on the walls "
                   "that wre in \na patter like a circuit board. They slowly started to glow red. To the North wall is "
                   "a door that has a sign \nthat reads 'To the Server'. To the East is to the server room.",
                   "You entered the red room. To the East is the server room and to the North ", False, None)

CORRUPTED_SERVER = Room("Corrupted Server", 'REFLECTIVE_R', None, 'CORRUPTED_R', None, [], False,
                        "You entered the door to the server room. Then you hear alarm bearing. The room turned red. "
                        "Then a speaker \nspoke, 'The World has been corrupted'.The speaker spoke that over and "
                        "over. Your ears. You try to find the \npanel for the speaker but it is not here. You must "
                        "find it in order to stop the speaker. To the North is a room \nfilled with mirrors. You don't "
                        "know why their filled with mirrors, but they are. To the South is the corrupted \nroom.",
                        "You entered the annoying room with the load speaker. To the North is a room filled with "
                        "mirrors. You don't know \nwhy their filled with mirrors, but they are. To the South is the "
                        "corrupted room.", False, None)

REFLECTIVE_R = Room("The Reflective Room", None, None, 'CORRUPTED_SERVER', 'COMPUTER_R', [], False,
                    "You enter the reflective room. Since you haven't found the panel to the speaker, you haven't "
                    "turned off the \nspeaker or the blaring red light. So the mirrors is mostly reflecting red "
                    "light. To the South is the corrupted \nserver and to the West is a room filled with complicated "
                    "electronics.",
                    "You have reached the reflected room with a bunch of mirrors. Why does it always have to be "
                    "mirrors. To the \nSouth is the corrupted server and to the West is a room filled with complicated "
                    "electronics.", False, None)

COMPUTER_R = Room("Computer Room", 'STONE_LIBRARY', 'REFLECTIVE_R', None, None, [], False,
                  "You reach the room filled with computers. You look at one of the computer screens and you see that "
                  "it is a blue \nscreen. The blue screen had text on it. The text says 'The Server is corrupted. "
                  "Restarting in an hour'. To the \nNorth is door that is made out of stone. it appears to be open. "
                  "To the East is the room filled with mirrors.",
                  "You entered the room filled with computers. To the North is door that is made out of stone. It "
                  "appears to be \nopen. To the East is the room filled with mirrors.", False, None)

STONE_LIBRARY = Room("STONE_LIBRARY", None, None, 'COMPUTER_R', 'GARDEN', [], False,
                     "You open the stone door. When you open the door, you see a huge library made up of stones. You "
                     "wonder why the \nstone door wasn't even locked. You go down the aile and you see that the books "
                     "are very old yet new. To the \nSouth is the computer room and to the West is a garden.",
                     "You entered the stone library. To the South is the computer room and to the West is a garden.",
                     False, None)

GARDEN = Room("Garden", None, 'STONE_LIBRARY', None, 'CASTLE_KITCHEN', [], False,
              "You reached the garden.The garden is filled with fruit and vegetables.You wonder why they will leave "
              "this \nbeautiful garden with the fruit and vegetables ready to rip. Then you see their is an automated "
              "system at play \nbut it had stopped. It had stopped because the server is corrupted. To the East is the "
              "stone library and to the \nwest is a door with a picture of a slice of cake on it.",
              "You entered the amazing and beautiful garden. To the East is the stone library and to the west is a "
              "door with a \npicture of a slice of cake on it.", False, None)

CASTLE_KITCHEN = Room("Castle Kitchen", 'CASTLE_ENTRANCE', 'GARDEN', 'MAGIC_LIBRARY', 'THRONE_R', [], False,
                      "You open the door to the door with the slice of cake on it. You see that it is the kitchen for "
                      "the castle. You \nsee that their is no food or any ingredients anywhere to be seen. You feel "
                      "hungry so you look for the \nrefrigerator. But their isn't any. So you just feel empty inside. "
                      "To the North is the castle entrance, to the \nEast is the garden, to the South is a bookshelf "
                      "that has the work 'magic' on it and to the West are big doors.",
                      "You entered the castles kitchen. To the North is the castle entrance, to the East is the "
                      "garden, to the South \nis a bookshelf that has the work 'magic' on it and to the West are big "
                      "doors.", False, None)

MAGIC_LIBRARY = Room("Magic Library", 'KITCHEN', None, 'WATERFALL_R', None, [], False,
                     "You found the hidden library. All around you, you feel like something very dark and mysterious "
                     "things are \naround. Then you see a book started to drift away with a magenta aura. Then use see "
                     "another book but with a \nyellow aura around it. You don't want to fallow it since it can be "
                     "dangerous. To the North is the kitchen and \nto the South is a blue door.",
                     "You are now in the library with the books that can fly. To the North is the kitchen and to the "
                     "South is a blue \ndoor.", False, None)

WATERFALL_R = Room("Waterfall Room", 'MAGIC_LIBRARY', None, 'MINE_SHAFT', None, [staff_of_emerged_power_blueprint],
                   False,
                   "You enter the peaceful room with a waterfall. You wonder how such beauty is in a place such like "
                   "this. In the \nRoom you see that a rainbow is trying to for but is sucked up from a tube in the "
                   "ceiling. It seems to be going \nto another place from the tube. To the North is the magic library "
                   "and to the South is the Mine shaft.",
                   "You entered the room with the beautiful water fall that seems to be out of place. To the North is "
                   "the magic \nlibrary and to the South is the Mine shaft.", False, None)

MINE_SHAFT = Room("The Mine Shaft", 'WATERFALL_R', None, None, 'CAVERN', [pickaxe], False,
                  "You have reached a mine shaft. You wonder why a place like this would even have a mine shaft since "
                  "it can \nrandomly generate whatever it wants. Wait, you didn't know that? Oh well. The only thing "
                  "some what ordinary is \nthat a pickaxe is here. To the North is the peaceful waterfall room and to "
                  "the West is a deeper part of the \nmine shaft.",
                  "Why did you come back to the mine if their really isn't anything here for you. To the North is the "
                  "peaceful \nwaterfall room and to the West is a deeper part of the mine shaft.", False, None)

CAVERN = Room("Cavern", 'LOOPER', 'MINE_SHAFT', None, None, [], False,
              "You are now in the deeper part of the mine shaft. All that is around you is rock and some minerals. To "
              "the \nNorth is what look like a way out of the mine shaft and to the East is the mine shaft that has "
              "the pickaxe.",
              "You are now in the cavern with rock all around you. To the North is what look like a way out of the "
              "mine shaft \nand to the East is the mine shaft that had the pickaxe.", False, None)

LOOPER = Room("The Looper", None, 'THRONE_R', 'CAVERN', 'RAINBOW_R', [dull_sword], False,
              "You are now in a room that is filled with side way eights. Then you remembered that side way eights is "
              "the \ninfinity sign. Then you see that their is a neon sign that says 'The lopper'. To the East is a "
              "throne room, to \nthe South is the cavern and to the West is a door that has rainbows all over the "
              "door.",
              "You are back to the Looper room. This sounds ironic. Does it to you? To the East is a throne room, to "
              "the South \nis the cavern and to the West is a door that has rainbows all over the door.", False, None)

THRONE_R = Room("Throne Room", None, 'CASTLE_KITCHEN', None, 'LOOPER', [magical_stone], False,
                "You entered the throne room that is in the castle. You see that their is someone on one of the "
                "thrones. He \nlooked like a king. But the way acted. he didn't seem like a king. To the East is the "
                "kitchen and to the West \nis the room that leads to somewhere else.",
                "You have came back to the impenetrable king. (For those who tried killing the king. You can't kill "
                "the king). \nTo the East is the kitchen and to the West is the room that leads to somewhere else.",
                False, Gabe)

RAINBOW_R = Room("Rainbow Room", None, 'BLOOD_MOON_R', 'LOOPER', None, [p_key_4, rainbow_in_a_bottle, unicorn_meat],
                 False,
                 "You have entered the room that has a bunch of rainbows. But they were in jars. They shouldn't be in "
                 "jars. Then \nyou see that their is a pipe on the ceiling that seems to be the one that transports "
                 "the rainbow into this \nroom. To the East is a door that you can't see into it and to the West is a "
                 "room that has an 8 on it.",
                 "You came back to the rainbow room. I guess you feel bad about the rainbows. No?. Then why did you "
                 "come back? To \nthe East is a door that you can't see into it and to the West is a room that has an "
                 "8 on it.", False, None)

BLOOD_MOON_R = Room("Blood Moon Room", None, 'SECTION_3', None, 'RAINBOW_R', [x_bow], False,
                    "You enter the room that was dark inside. But as soon as you came in. You were able to see that "
                    "their was a \nblood moon on the ceiling. 'How is this possible?' you asked yourself. To the East "
                    "is a hallway that you can go \nto in 3 directions and to the West is a room with a rainbow door.",
                    "You have came back to admire the blood moon, right? To the East is a hallway that can go 3 "
                    "directions and to \nthe West is a door with a rainbow door.", False, None)

SECTION_3 = Room("Section 3", None, 'LIGHT_R', 'CASTLE_ENTRANCE', 'BLOOD_MOON_R', [], False,
                 "You have made it to a 3-way section hallway. Their is nothing special in the hallway other than that "
                 "you can go \n3 ways. To the East is a room that has a blinding light, to the South is the entrance "
                 "of a castle and to the \nWest is a door that is red and inside is very dark.",
                 "You are now in the 3-way section. To the East is the room that has blinding light inside, to the "
                 "South is the \ncastle entrance and to the West is a door that is red that is dark inside.", False,
                 None)

CASTLE_ENTRANCE = Room("Castle Entrance", 'SECTION_3', None, 'CASTLE_KITCHEN', None, [], False,
                       "You are in the castle entrance. What are you going to do. You might find someone that can help "
                       "you understand \nwhat is going on. To the North is a 3-way section and to the West is the "
                       "castle's kitchen.",
                       "You are in the entrance of the castle's entrance. To the North is a 3-way section and to the "
                       "West is the \ncastle's kitchen.", False, None)

LIGHT_R = Room("Light Room", None, 'BO_BO', None, 'SECTION_3', [], False,
               "You have reached the room that you couldn't see the inside. You were blinded and you can't see "
               "anything. To \nwhat you think is East is a room that has something on the door and to what I think is "
               "West is a door that is \ngreen?",
               "You enter the room that is blinding. Then you feel that something is in your pants pocket and that is "
               "a pair of \nsunglasses. You put them on and you can actually see things inside. To the East is a door "
               "that leads to a place \ncalled Bo Bo's room and to the West is a green door that leads to a 3-way "
               "section. Then you put away the \nsunglasses. Forgetting about them. Even if you are blinded.", False,
               None)

BO_BO = Room("Bo Bo's room", 'PUZZLE_R', 'FORGOTTEN_R', None, 'LIGHT_R', [], False,
             "You finally reached the door to another room. This room was different. You have never been here before. "
             "Yet it \nis familiar. On the ceiling you see text that says 'Bo Bo's room'. You wonder who he is but you "
             "don't want to \nknow. To the North is a rope that doesn't look like you can just cut it and to the West "
             "is a the horrible room \nfiled with light.",
             "You entered Bo Bo's room. To the North is a room and to the West is a the horrible room filed with "
             "light.", False, None)

FORGOTTEN_R = Room("Forgotten Room", None, None, None, 'BO_BO', [p_key_1], False,
                   "You enter the room that was well hidden. You asked yourself how you knew about it. It doesn't "
                   "matter now. In \nthe room you see a bunch of bookshelves with books. In the room you see a paper "
                   "that someone has writen on it. \nYou don't understand it. But then you see a key. It has 'P KEY' "
                   "written on it. To the West is Bo BO's room.",
                   "You really like going to hidden rooms don't you know. Bet you feel nice to see this hard to find "
                   "key. To the \nWest is Bo Bo'd room", False, None)

PUZZLE_R = Room("Puzzle Room", None, None, 'BO_BO', None, [], False,
                "You enter the room that Gabe told you not to go their. 'The puzzle will be to hard' he said. You "
                "didn't care \nbecause you wanted everything to go back to normal. Then you saw a scroll and so you "
                "opened it. \nThe Puzzle: \nIf you had only one match, and entered a dark room containing an oil lamp, "
                "some newspaper, and some kindling \nwood, which would you light first?",
                "Are you going to solve the puzzle? if you are, here is the puzzle. \nThe Puzzle: \nIf you had only "
                "one match, and entered a dark room containing an oil lamp, some newspaper, and some kindling \nwood, "
                "which would you light first?", False, None)


end_game = "Once you have thought that the world was so easy, yet you didn't know how hard it was to survive all by \n"\
           "yourself. You saw yourself in a mirror as the wall changed around you. You couldn't do anything to change "\
           "that.\nYou saw all your friends go by. there were inside the room. Behind a hidden door that you didn't "\
           "see when you \nfirst entered. Thank you for playing my game. It was easy to make the game but I didn't "\
           "really know what to do \nwith ending. So I decided to do some improve and created this end game text. "\
           "Hope you enjoyed the game. :) \n"\
           "T-pose on them \n" \
           "___0___ \n" \
           "   |    \n" \
           "  / \     " \

print("You can end the game mid game by writing down 'quit' and entered it.")


current_node = BACK_MALL

directions = ['north', 'east', 'south', 'west']

short_directions = ['n', 'e', 's', 'w']

finished_the_game = False

pass_trough = False

moves = 0

current_armor_on = beginner_armor

commands_possible = ["jump", "H use", "armor info", "grab", "attack damage", "drop", "description", "commands possible",
                     "inventory", "how to play", "craft", "attack enemy", "H main weapon", "H put on armor",
                     "blueprints", "alchemist craft", "use firework", "farm", "mine"]

craftable = ["iron armor", "gold armor", "diamond armor", "armor of undying", "armor of strength", "metal bow",
             "legendary bow", "staff of healing", "staff of emerged power", "staff of power", "sticks",
             "cosmonium ingot", "magical sword", "armor shell", "battery", "firework", "cooked potato", "sharp sword",
             "sharpening stone", "glass", "glass bottle", "iron bar", "gold bar", "diamond", "cooked meat"]

alchemy = ["weak health potion", "strong health potion", "strength potion", "poison potion"]

farm = [sand, elf_leaf, wood, heal_flower]

mine = [uncut_diamond, cosmonium_ore, iron_ore, gold_ore, stone]

blueprints = [staff_of_emerged_power_blueprint, staff_of_healing_blueprint, paper_with_writing]

usable = [weak_health_potion, strong_health_potion, strength_potion, poison_potion, raw_potato, cooked_potato,
          potato_chip, raw_meat, cooked_meat, unicorn_meat]

armor_types = [armor_of_strength, armor_of_undying, beginner_armor, diamond_armor, gold_armor, iron_armor,
               leather_armor, wood_armor]

weapons_types = [dull_sword, sharp_sword, magical_sword, staff_of_healing, staff_of_emerged_power]

ranged_types = [broken_bow, x_bow, metal_bow, legendary_bow]


def crafting():
    item_crafting = False
    while item_crafting == "cancel":
        print("".join(craftable))
        item_crafting = input("What do you want to craft?(To exit crafting table, type cancel). ").lower()
        if item_crafting == "armor of undying":
            if paper_with_writing in current_character.inventory:
                if armor_of_undying not in current_character.inventory:
                    if cosmonium_ingot and armor_shell in current_character.inventory:
                        if cosmonium_ingot.amount >= str(10) and armor_shell.amount >= 15:
                            current_character.inventory.append(armor_of_undying)
                            armor_of_undying.amount += 1
                            cosmonium_ore.amount -= 10
                            if cosmonium_ore.amount == 0:
                                current_character.inventory.remove(cosmonium_ore)
                                print("You no longer have cosmonium ores in your inventory.")
                            armor_shell.amount -= 15
                            if armor_shell.amount == 0:
                                current_character.inventory.remove(armor_shell)
                                print("You no longer have armor shells in your inventory.")
                            print("You have used 10 cosmonium ore and 15 armor shell.")
                            print("You have created the ARMOR OF UNDYING. type in 'armor of undying' in the command.")
                        else:
                            print("You don't have enough materials for this item. You either don't have 10 cosmonium "
                                  "ore or 15 armor shells.")
                    else:
                        print("You don't have the materials for this item. You either don't have cosmonium ingots or "
                              "armor shells.")
                else:
                    print("You already have this item.")
            else:
                print("You don't have the paper with writing.")
        if item_crafting == "armor of strength":
            if strength_potion in current_character.inventory and iron_armor in current_character.inventory and \
                            armor_shell in current_character.inventory:
                if armor_shell.amount >= 5:
                    if armor_of_strength not in current_character.inventory:
                        current_character.inventory.append(armor_of_strength)
                    armor_of_strength.amount += 1
                    strength_potion.amount -= 1
                    if strength_potion.amount == 0:
                        current_character.inventory.remove(strength_potion)
                        print("You no longer have strength potions in your inventory.")
                    iron_armor.amount -= 1
                    if iron_armor.amount == 0:
                        current_character.inventory.remove(iron_armor)
                        print("You no longer have iron armor in your inventory.")
                    armor_shell.amount -= 5
                    if armor_shell.amount == 0:
                        current_character.inventory.remove(armor_shell)
                        print("You no longer have armor shells in your inventory.")
                    print("You have used one of your strength potion, iron armor, and 5 armor shell.")
                    print("You have created the ARMOR OF STRENGTH. For more info, type 'armor of strength' in the "
                          "command")
                else:
                    print("You don't have enough materials for this item. You don't have 5 armor shell.")
            else:
                print("You don't have the materials for this item. You either don't have a strength potion, iron armor "
                      "or armor \n"
                      "shells.")
        if item_crafting == "iron armor":
            if iron_bar in current_character.inventory and armor_shell in current_character.inventory:
                if iron_bar.amount >= str(5) and armor_shell.amount >= 10:
                    if iron_armor not in current_character.inventory:
                        current_character.inventory.append(iron_armor)
                    iron_armor.amount += 1
                    iron_bar.amount -= 5
                    if iron_bar.amount == 0:
                        current_character.inventory.remove(iron_bar)
                        print("You no longer have iron bars in your inventory.")
                    armor_shell.amount -= 10
                    if armor_shell.amount == 0:
                        current_character.inventory.remove(armor_shell)
                        print("You no longer have armor shells in your inventory.")
                    print("You no longer have 5 iron bars and 10 armor shells.")
                    print("You have crafted iron armor. For more info, type in 'iron armor'in the command.")
                else:
                    print("You don't have enough materials for this item. You either don't have 5 iron bars or 10 "
                          "shells.")
            else:
                print("You don't have the materials for this item. You either don't have iron bars or armor shells.")
        if item_crafting == "gold armor":
            if gold_bar in current_character.inventory and armor_shell in current_character.inventory \
                    in current_character.inventory:
                if gold_bar.amount >= str(5) and armor_shell.amount >= 10:
                    if gold_armor not in current_character.inventory:
                        current_character.inventory.append(gold_armor)
                    gold_armor.amount += 1
                    gold_bar.amount -= 5
                    if gold_bar.amount == 0:
                        current_character.inventory.remove(gold_bar)
                        print("You no longer have gold bars in your inventory.")
                    armor_shell.amount -= 10
                    if armor_shell.amount == 0:
                        current_character.inventory.remove(armor_shell)
                        print("You no longer have armor shells in your inventory.")
                    print("You no longer have 5 gold bars and 10 armor shells.")
                    print("You have crafted golden armor. For more info, type 'inventory' and then 'gold armor' in "
                          "the command.")
                else:
                    print("You don't have enough materials for this item. You either don't have 5 gold bars or 10 "
                          "armor shells.")
            else:
                print("You don't have the materials for this item. You either don't have gold bars or armor shells.")
        if item_crafting == "diamond armor":
            if diamond in current_character.inventory and armor_glue in current_character.inventory and armor_shell \
                    in current_character.inventory:
                if diamond.amount >= str(5) and armor_shell.amount >= 10:
                    if diamond_armor not in current_character.inventory:
                        current_character.inventory.append(diamond_armor)
                    diamond_armor.amount += 1
                    diamond.amount -= 5
                    if diamond.amount == 0:
                        current_character.inventory.remove(diamond)
                        print("You don't have diamonds in your inventory.")
                    armor_glue.amount -= 1
                    if armor_glue.amount == 0:
                        current_character.inventory.remove(armor_glue)
                        print("You don't have a bottle of armor glue.")
                    print("You no longer have 10 diamonds and the bottle of armor glue.")
                    print("You crafted diamond armor. But the glue still needs to dry. For more info, type 'inventory' "
                          "in the command.")
                else:
                    print("You don't have enough materials for this item. You either don't have 5 diamonds or 10 armor "
                          "shells.")
            else:
                print("You don't have the materials for this item. You either don't have diamonds, a bottle of armor "
                      "glue or \n"
                      "armor shells.")
        if item_crafting == "metal bow":
            if iron_bar in current_character.inventory and broken_bow in current_character.inventory:
                if iron_bar.amount >= str(5):
                    if metal_bow not in current_character.inventory:
                        current_character.inventory.append(metal_bow)
                    metal_bow.amount += 1
                    current_character.inventory.remove(broken_bow)
                    broken_bow.amount -= 1
                    iron_bar.amount -= 5
                    if iron_bar.amount == 0:
                        current_character.inventory.remove(iron_bar)
                        print("You no longer have iron bars in your inventory.")
                    print("You no longer have the broken bow and 5 iron bars.")
                    print("You crafted a metal bow. For more info, type 'inventory' in the command.")
                else:
                    print("You don't have enough material for this item.You either don't have 5 iron bars and a broken "
                          "bow.")
            else:
                print("You don't have the materials for this item. You either don't have iron bars or a broken bow.")
        if item_crafting == "legendary bow":
            if metal_bow in current_character.inventory and cosmonium_ingot in current_character.inventory and \
                            iron_bar in current_character.inventory:
                if cosmonium_ingot.amount >= str(6) and iron_bar.amount >= str(3):
                    if legendary_bow not in current_character.inventory:
                        current_character.inventory.append(legendary_bow)
                    legendary_bow.amount += 1
                    metal_bow.amount -= 1
                    current_character.inventory.remove(metal_bow)
                    cosmonium_ingot.amount -= 6
                    current_character.inventory.remove(cosmonium_ingot)
                    if cosmonium_ingot.amount == 0:
                        current_character.inventory.remove(cosmonium_ingot)
                        print("You no longer have cosmonium ingots in your inventory.")
                    iron_bar.amount -= 3
                    if iron_bar.amount == 0:
                        current_character.inventory.remove(iron_bar)
                        print("You no longer have iron bars in your inventory.")
                    print("You no longer have the iron bar and the 3 cosmonium ingots.")
                    print("You made a legendary item. You made the legendary bow. For more info, type 'inventory' in "
                          "the command.")
                else:
                    print("You don't have the materials for this item. You either don't have 6 cosmonium ingots or 3 "
                          "iron bars.")
            else:
                print("You don't have the materials for this item. You either don't have a metal bow, cosmonium ingots "
                      "or iron \n"
                      "bars.")
        if item_crafting == "staff of healing":
            if staff_of_healing_blueprint in current_character.inventory:
                if staff_of_healing not in current_character.inventory:
                    if sticks in current_character.inventory and cosmonium_ingot in current_character.inventory:
                        if not staff_of_healing.one_crafted:
                            if sticks.amount >= 10 and cosmonium_ingot.amount >= str(10):
                                current_character.inventory.append(staff_of_healing)
                                staff_of_healing.amount += 1
                                sticks.amount -= 10
                                if sticks.amount == 0:
                                    current_character.inventory.remove(sticks)
                                    print("You no longer have sticks in your inventory.")
                                cosmonium_ingot.amount -= 10
                                if cosmonium_ingot.amount == 0:
                                    current_character.inventory.remove(cosmonium_ingot)
                                    print("You no longer have cosmonium ingots in your inventory.")
                                print("You no longer have 10 sticks and 10 cosmonium ingots.")
                                print("You crafted a legendary item. You crafted the staff of healing. For more info, "
                                      "type in 'inventory' in the \n"
                                      "command.")
                            else:
                                print("You don't have enough materials for this item. You either don't have 10 sticks "
                                      "or 10 cosmonium ingots.")
                        else:
                            print("You can only craft this item once. Sorry :(")
                    else:
                        print("You don't have the materials for this item. You either don't have sticks or cosmonium "
                              "ore.")
                else:
                    print("You already have this item in your inventory. You can only craft it once. Sorry :(")
            else:
                print("You do not have the blueprint.")
        if item_crafting == "staff of emerged power":
            if staff_of_emerged_power_blueprint in current_character.inventory:
                if staff_of_emerged_power not in current_character.inventory:
                    if sticks in current_character.inventory and cosmonium_ingot in current_character.inventory:
                        if not staff_of_emerged_power.one_crafted:
                            if sticks.amount >= 10 and cosmonium_ingot.amount >= str(15):
                                current_character.inventory.append(staff_of_emerged_power)
                                staff_of_emerged_power.amount += 1
                                sticks.amount -= 10
                                if sticks.amount == 0:
                                    current_character.inventory.remove(sticks)
                                    print("You no longer have sticks in your inventory.")
                                cosmonium_ingot.amount -= 15
                                if cosmonium_ingot.amount == 0:
                                    current_character.inventory.remove(cosmonium_ingot)
                                    print("You no longer have cosmonium ingots in your inventory.")
                                print("You no longer have 10 sticks and 15 cosmonium ingots.")
                                print("You crafted a legendary item. You crafted the staff of emerged power. For more "
                                      "info, type in 'inventory' \n"
                                      "in the command.")
                            else:
                                print("You don't have enough materials for this item. You either don't have 10 sticks "
                                      "or \n"
                                      "15 cosmonium ingots.")
                        else:
                            print("You can only craft this item once. Sorry :(")
                    else:
                        print("You don't have the materials for this item. You either don't have sticks or cosmonium \n"
                              "ingots.")
                else:
                    print("You already have this item in your inventory. You can only have 1 in your inventory.")
            else:
                print("You do not have a blueprint.")
        if item_crafting == "sticks":
            if wood in current_character.inventory:
                sticks_amount = input("How many sticks do you want to craft? (Reminder: You must tell how many wood "
                                      "you want to use). ")
                wood_used = sticks_amount
                possible_s = wood.amount
                if possible_s <= sticks_amount:
                    if sticks not in current_character.inventory:
                        current_character.inventory.append(sticks)
                    sticks.amount = possible_s * 4
                    wood.amount -= sticks.amount
                    if wood.amount == 0:
                        current_character.inventory.remove(wood)
                        print("You no longer have wood in your inventory.")
                    print("You no longer have %s wood." % wood_used)
                    print("You crafted %s sticks. For more info, type in 'inventory' in the command." % possible_s)
                else:
                    print("You are asking for more than what you can craft.")
            else:
                print("You don't have the materials for this item. You don't have wood in your inventory.")
        if item_crafting == "cosmonium ingot":
            if cosmonium_ore in current_character.inventory:
                cosmonium_ingot_amount = input("How many cosmonium ingots do you want to craft? (Reminder: You must "
                                               "tell how many cosmonium ore you are going \n"
                                               "to use. Every cosmonium ore is 2 cosmonium ingots). ")
                cosmonium_ore_used = cosmonium_ingot_amount
                possible_ci = cosmonium_ore.amount
                if possible_ci <= cosmonium_ingot_amount:
                    if cosmonium_ingot not in current_character.inventory:
                        current_character.inventory.append(cosmonium_ingot)
                    cosmonium_ingot.amount = cosmonium_ingot_amount * 2
                    cosmonium_ore.amount -= cosmonium_ingot_amount
                    if cosmonium_ore.amount == 0:
                        current_character.inventory.remove(cosmonium_ore)
                        print("You no longer have cosmonium ore in your inventory.")
                    print("You no longer have %s cosmonium ore." % cosmonium_ore_used)
                    print("You crafted %s cosmonium ingots. For more info, type in 'inventory' in the "
                          "command." % possible_ci)
                else:
                    print("You are asking for more than what you can craft.")
            else:
                print("You don't have the material for this item.")
        if item_crafting == "magical sword":
            if magical_stone in current_character.inventory and sharp_sword in current_character.inventory:
                if magical_sword not in current_character.inventory:
                    current_character.inventory.append(magical_sword)
                    magical_sword.amount += 1
                    magical_stone.amount -= 1
                    if magical_stone.amount == 0:
                        current_character.inventory.remove(magical_stone)
                        print("You no longer have magical stones in your inventory.")
                    sharp_sword.amount -= 1
                    if sharp_sword.amount == 0:
                        current_character.inventory.remove(sharp_sword)
                        print("You no longer have stone swords in your inventory.")
                print("You no longer have a magical stone sword and a stone sword.")
                print("You crafted a magical sword. For more info, type 'inventory' in the command.")
            else:
                print("You don't have the materials for this item.")
        if item_crafting == "armor shell":
            if iron_bar in current_character.inventory:
                armor_shell_amount = input("How many armor shells do you want to craft? ")
                possible_as = iron_bar.amount
                if possible_as <= armor_shell_amount:
                    if "armor shell" not in current_character.inventory:
                        current_character.inventory.append(armor_shell)
                    armor_shell.amount += armor_shell_amount
                    iron_bar.amount -= armor_shell_amount
                    if iron_bar.amount == 0:
                        current_character.inventory.remove(iron_bar)
                        print("You no longer have iron bars in your inventory.")
                    print("You no longer have %s iron bars." % possible_as)
                    print("You crafted %s armor shells. For more info, type in 'inventory' in the command.")
                else:
                    print("You are asking for more than what you can craft.")
            else:
                print("You don't have the material for this item. You do not have iron bars.")
        if item_crafting == "battery":
            if wire in current_character.inventory and armor_shell in current_character.inventory:
                if battery not in current_character.inventory:
                    if wire.amount >= 10 and armor_shell.amount >= 5:
                        current_character.inventory.append(battery)
                        battery.amount += 1
                        wire.amount -= 10
                        if wire.amount == 0:
                            current_character.inventory.remove(wire)
                            print("You no longer have any wires in your inventory.")
                        armor_shell.amount -= 5
                        if armor_shell.amount == 0:
                            current_character.inventory.remove(armor_shell)
                            print("You no longer have any armor shells in your inventory.")
                        print("You no longer have 10 wires and 5 armor shell ")
                        print("You crafted a battery. For more info, type in 'inventory' in the command.")
                    else:
                        print("You don't have enough materials for this item. You either don't have 10 wires or 5 "
                              "armor shells.")
                else:
                    print("You already have a battery in your inventory.")
            else:
                print("You don't have the materials to craft this item. You either don't have wires or armor shells.")
        if item_crafting == "firework":
            if gunpowder in current_character.inventory and armor_shell in current_character.inventory:
                firework_amount = input("How many fireworks do you want to craft? ")
                amount_f_1 = gunpowder.amount - armor_shell.amount
                amount_f_2 = armor_shell.amount - gunpowder.amount
                possible_f = 0
                if amount_f_1 > 0:
                    possible_f = armor_shell.amount
                if amount_f_2 > 0:
                    possible_f = gunpowder.amount
                if possible_f <= firework_amount:
                    if firework not in current_character.inventory:
                        current_character.inventory.append(firework)
                    firework.amount += firework_amount
                    gunpowder.amount -= firework_amount
                    if gunpowder.amount == 0:
                        current_character.inventory.remove(gunpowder)
                        print("You no longer have gunpowder in your inventory.")
                    armor_shell.amount -= firework_amount
                    if armor_shell == 0:
                        current_character.inventory.remove(armor_shell)
                        print("You no longer have armor shells in your inventory.")
                    print("You no longer have %s gunpowder and armor shell." % possible_f)
                    print("You crafted %s fireworks. For more info, type 'inventory' in the command." % possible_f)
                else:
                    print("You are trying to craft more than you can craft.")
            else:
                print("You don't have the materials to craft this item. You either don't have gunpowder or armor "
                      "shells in your \n"
                      "inventory.")
        if item_crafting == "cooked potato":
            if raw_potato in current_character.inventory and torch in current_character.inventory:
                cooked_potato_amount = input("How much raw potato do you want to use to make cooked potato? ")
                possible_cp = raw_potato.amount
                if possible_cp <= cooked_potato_amount:
                    if cooked_potato not in current_character.inventory:
                        current_character.inventory.append(cooked_potato)
                    cooked_potato.amount += cooked_potato_amount
                    raw_potato.amount -= cooked_potato_amount
                    if raw_potato.amount == 0:
                        current_character.inventory.remove(raw_potato)
                        print("You no longer have raw potatoes.")
                    print("Yo no longer have %s raw potato" % cooked_potato_amount)
                    print("You crafted %s cooked potatoes. For more info, type 'inventory' in the "
                          "command." % cooked_potato_amount)
                else:
                    print("You are asking for more than what you can do.")
            else:
                print("You don't have the materials for this item. You don't have raw potatoes in your inventory.")
        if item_crafting == "sharp sword":
            if dull_sword in current_character.inventory and sharpening_stone in current_character.inventory:
                if sharp_sword not in current_character.inventory:
                    current_character.inventory.append(sharp_sword)
                    sharp_sword.amount += 1
                    dull_sword.amount -= 1
                    if dull_sword.amount == 0:
                        current_character.inventory.remove(dull_sword)
                        print("You no longer have a dull sword in your inventory.")
                    print("You no longer have a dull sword.")
                    print("You crafted a sharp sword. For more info, type 'inventory'in the command.")
                else:
                    print("You cannot craft something that is already in your inventory.")
        if item_crafting == "sharpening stone":
            if stone in current_character.inventory:
                if stone.amount >= 2:
                    if sharpening_stone not in current_character:
                        sharpening_stone.amount += 2
                        stone.amount -= 2
                        if stone.amount == 0:
                            current_character.inventory.remove(stone)
                            print("You no longer have stone in your inventory.")
                        print("You no longer have 2 normal stones.")
                        print("You crafted a sharpening stone. for more info, type 'inventory' in the command.")
                    else:
                        print("You cannot craft something that is already in your inventory.")
                else:
                    print("You don't have enough stones.")
            else:
                print("You don't have the materials for this item. You don't have stone.")
        if item_crafting == "glass":
            if sand in current_character.inventory:
                glass_amount = input("How much sand do you want to use to make glass? ")
                possible_s = sand.amount
                if possible_s >= glass_amount:
                    if glass not in current_character.inventory:
                        current_character.inventory.append(glass)
                    glass_made = glass_amount * 3
                    glass.amount = glass_amount * 3
                    sand.amount -= glass_amount
                    if sand.amount == 0:
                        current_character.inventory.remove(sand)
                        print("You no longer have sand in your inventory.")
                    print("You no longer have %s sand." % glass_amount)
                    print("You crafted %s glass. For more info, type 'inventory' in the command." % glass_made)
                else:
                    print("You are asking for more than what you can craft.")
            else:
                print("You don't have the materials for this item. You need sand.")
        if item_crafting == "glass bottle":
            if glass in current_character.inventory:
                glass_bottle_amount = input("How much glass do you want to craft to make glass bottle? ")
                possible_gb = glass.amount
                if possible_gb <= glass_bottle_amount:
                    if glass_bottle not in current_character.inventory:
                        current_character.inventory.append(glass_bottle)
                    glass_bottle.amount += glass_bottle_amount
                    glass.amount -= glass_bottle_amount
                    if glass.amount == 0:
                        current_character.inventory.remove(glass)
                        print("You no longer have glass in your inventory.")
                    print("You no longer have %s glass." % glass_bottle_amount)
                    print("You crafted %s glass bottle. For more info, type 'inventory' in the "
                          "command." % glass_bottle_amount)
                else:
                    print("You are trying to craft more than what you can do.")
            else:
                print("You do not have the materials for this item. You do not have glass.")
        if item_crafting == "iron bar":
            if iron_ore in current_character.inventory:
                iron_bar_amount = input("How many iron bars do you want to craft? ")
                possible_ib = iron_ore.amount
                if possible_ib <= iron_bar_amount:
                    if iron_bar not in current_character.inventory:
                        current_character.inventory.append(iron_bar)
                    iron_bar.amount = iron_bar_amount
                    iron_ore_used = iron_bar_amount * 2
                    iron_ore.amount -= iron_bar_amount * 2
                    if iron_ore.amount == 0:
                        current_character.inventory.remove(iron_ore)
                        print("You no longer have iron ores in your inventory.")
                    print("You no longer have %s iron ores." % iron_ore_used)
                    print("You crafted %s iron bars. For more info, type 'inventory' in the command." % iron_bar_amount)
                else:
                    print("You are asking for more than what you can do.")
            else:
                print("You don't have the materials for this item. You don't have iron ores.")
        if item_crafting == "gold bar":
            if gold_ore in current_character.inventory:
                gold_bar_amount = input("How many gold bars do you want to craft? ")
                possible_gb = gold_ore.amount
                if possible_gb <= gold_bar_amount:
                    if gold_bar not in current_character.inventory:
                        current_character.inventory.append(gold_bar)
                    gold_bar.amount = gold_bar_amount
                    gold_ore_used = gold_bar_amount * 2
                    gold_ore.amount -= gold_bar_amount * 2
                    if gold_ore.amount == 0:
                        current_character.inventory.remove(gold_ore)
                        print("You no longer have gold ores in your inventory.")
                    print("You no longer have %s gold ores." % gold_ore_used)
                    print("You crafted %s gold bars. For more info, type 'inventory' in the command." % gold_bar_amount)
                else:
                    print("You are asking for more than what you can craft.")
            else:
                print("You don't have materials for this item. You don't have gold ores.")
        if item_crafting == "diamond":
            if uncut_diamond in current_character.inventory:
                diamond_amount = input("How many diamonds do you want to craft? ")
                possible_d = uncut_diamond.amount
                if possible_d <= diamond_amount:
                    if diamond not in current_character.inventory:
                        current_character.inventory.append(diamond)
                    diamond.amount += diamond_amount
                    uncut_diamond.amount -= diamond_amount
                    if uncut_diamond.amount == 0:
                        current_character.inventory.remove(uncut_diamond)
                        print("You no longer have uncut diamonds in your inventory.")
                    print("You no longer have %s gold ores." % diamond_amount)
                    print("You crafted %s diamonds. For more info, type 'inventory' in the command." % diamond_amount)
                else:
                    print("You are asking for more than what you can craft.")
            else:
                print("You don't have materials for this item. You don't have diamonds.")
        if item_crafting == "cooked meat":
            if raw_meat in current_character.inventory:
                cooked_meat_amount = input("How much raw meat do you want to use to craft cooked meat? ")
                possible_cm = raw_meat.amount
                if possible_cm <= cooked_meat_amount:
                    if cooked_meat not in current_character.inventory:
                        current_character.inventory.append(cooked_meat)
                    cooked_meat.amount += cooked_meat_amount
                    raw_meat.amount -= cooked_meat_amount
                    if raw_meat.amount == 0:
                        current_character.inventory.remove(raw_meat)
                        print("You no longer have raw meat in your inventory.")
                    print("You no longer have %s raw meat." % cooked_meat_amount)
                    print("You crafted %s cooked meat. For more info, type 'inventory' in the "
                          "command." % cooked_meat_amount)
                else:
                    print("You are asking for more than you can cook.")
            else:
                print("You do not have the materials for this item. You need raw meat.")

        if item_crafting not in craftable:
            print("This item does not exist. Please try again.")


def alchemist_crafting():
    potion_crafting = False
    while potion_crafting == "cancel":
        print("".join(alchemy))
        potion_crafting = input("What potion are you going to brew?(To exit, type cancel). ").lower()
        if potion_crafting == "weak health potion":
            if glass_bottle and heal_flower in current_character.inventory:
                if heal_flower.amount >= 2:
                    if "weak health potion" not in current_character.inventory:
                        current_character.inventory.append(weak_health_potion)
                    weak_health_potion.amount += 1
                    glass_bottle.amount -= 1
                    if glass_bottle.amount == 0:
                        current_character.inventory.remove(glass_bottle)
                        print("You no longer have glass bottles in your inventory.")
                    heal_flower.amount -= 2
                    if heal_flower.amount == 0:
                        current_character.inventory.remove(heal_flower)
                        print("You no longer have heal flowers in your inventory.")
                    print("You no longer have a glass bottle and 2 heal flowers.")
                    print("You crafted a weak health potion. For more info, type 'inventory' in the command.")
                else:
                    print("you don't have enough materials for this item. You do not have 2 heal flowers.")
            else:
                print("You do not have the items to craft this item. You either don't have a glass bottle or heal "
                      "flowers.")
        if potion_crafting == "strong health potion":
            if glass_bottle and heal_flower in current_character.inventory:
                if heal_flower.amount >= 5:
                    if strong_health_potion not in current_character.inventory:
                        current_character.inventory.append(strong_health_potion)
                    strong_health_potion.amount += 1
                    glass_bottle.amount -= 1
                    if glass_bottle.amount == 0:
                        current_character.inventory.remove(glass_bottle)
                        print("You no longer have glass bottles in your inventory.")
                    heal_flower.amount -= 5
                    if heal_flower.amount == 0:
                        current_character.inventory.remove(heal_flower)
                        print("You no longer have heal flowers in your inventory.")
                    print("you no longer have a glass bottle and 5 flowers.")
                    print("You crafted a strong health potion. For more info, type 'inventory' in the command.")
                else:
                    print("You don't have enough materials. You need 5 heal flowers.")
            else:
                print("You don't have the materials for this item. You either don't have glass bottles or heal "
                      "flowers.")
        if potion_crafting == "strength potion":
            if glass_bottle and power_stone in current_character.inventory:
                if strength_potion not in current_character.inventory:
                    current_character.inventory.append(strength_potion)
                strength_potion.amount += 1
                glass_bottle.amount -= 1
                if glass_bottle.amount == 0:
                    current_character.inventory.remove(glass_bottle)
                    print("You no longer have glass bottles in your inventory.")
                print("You no longer have a glass bottle and a power stone.")
                print("You crafted a strength potion. For more info, type 'inventory' in the command.")
            else:
                print("You don't have the materials for this item. You either don't have glass bottles or power "
                      "stones.")
        if potion_crafting == "poison potion":
            if glass_bottle and elf_leaf in current_character.inventory:
                if elf_leaf.amount >= 2:
                    if poison_potion not in current_character.inventory:
                        current_character.inventory.append(poison_potion)
                    poison_potion.amount += 1
                    glass_bottle.amount -= 1
                    if glass_bottle.amount == 0:
                        current_character.inventory.remove(glass_bottle)
                        print("You no longer have glass bottles in your inventory.")
                    elf_leaf.amount -= 1
                    if elf_leaf.amount == 0:
                        current_character.inventory.remove(elf_leaf)
                    print("You no longer have elf leafs in your inventory.")
                    print("You crafted a poison potion. For more info, type 'inventory' in the command.")
                else:
                    print("You don't have enough materials for this item. You don't have 2 elf leaves.")
            else:
                print("You don't have the materials for this item. You either don't have have glass bottles or elf "
                      "leaves.")


while current_character.alive or finished_the_game is True:
    if current_node == PUZZLE_R:
        yes_no = input("Are you going to solve the question?(answer with a yes or no) ").lower()
        if yes_no == "yes":
            command_puzzle = input("The answer: ").lower()
            if command_puzzle == "the match" or "match":
                print("You got it right.")
                print("It is the match.")
                print("It took you %s moves" % moves)
                print(end_game)
                finished_the_game = True
            else:
                print("Command not recognized")
        if yes_no == "no":
            current_node = BO_BO
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("MOVES: %s" % moves)
        print("HEALTH: %s" % current_character.health)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
                    moves += 1
                except KeyError:
                    print("Command not recognize")
                    print()
            else:
                if command in commands_possible:
                    if command == "jump":
                        print("Whoosh.")
                    if command == "use":
                        if len(current_character.inventory) != 0:
                            for items in current_character.inventory:
                                print(items.name)
                            use_item = input("What do you want to use? ")
                            if use_item in current_character.inventory:
                                print()
                    if command == "armor info":
                        print("Your current armor: \n%s" % current_character.armor_type)
                        print()
                        print("To change the armor type, type in put on armor in the command.")
                    if command == "grab":
                        print("Type again the grab command but after that put th item you want to grab. ")
                        for items in current_node.item_i:
                            print(items.name)
                        command = input(">_")
                        if 'grab' in command:
                            print("Items in current location:")
                            item_request = command[5:]
                            for items in current_node.item_i:
                                if items in current_node.item_i:
                                    current_node.item_i.remove(items)
                                    current_character.inventory.append(items)
                                    print()
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Your Inventory:")
                                    for item in current_character.inventory:
                                        print(item.name)
                                        print()
                                        print(item.description)
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                else:
                                    print("This item is not in the room.")
                        else:
                            print("You forgot the grab in the beginning of the command. Try again.")
                            print("Remember, you need to first put grab and then grab(item name) for it to work.")
                    if command == "attack damage":
                        print()
                        print("Your Attack Damage:")
                        print(current_character.damage)
                    if command == "drop":
                        print("Type again the grab command but after that put th item you want to grab"
                              "(grab[item name]. ")
                        for items in current_character.inventory:
                            print(items.name)
                        command = input(">_")
                        if 'drop' in command:
                            item_request = command[5:]
                            for items in current_character.inventory:
                                if items in current_character.inventory:
                                    current_node.item_i.append(items)
                                    current_character.inventory.remove(items)
                                    print()
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                    print("Items in current node:")
                                    for item in current_node.item_i:
                                        print(item.name)
                                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                                else:
                                    print("This item is not in your inventory.")
                        else:
                            print("You forgot the grab in the beginning of the command. Try again.")
                            print("Remember, you need to first put grab and then grab(item name) for it to work.")
                    if command == "description":
                        print()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Your Description:")
                        print(current_character.description)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    if command == "commands possible":
                        print(", ".join(commands_possible))
                    if command == "inventory":
                        print()
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("Your Inventory:")
                        for items in current_character.inventory:
                            print("You have %s of %s" % (items.amount, items.name))
                            print()
                            print(items.description)
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    if command == "how to play":
                        print("How to play: \n"
                              "You move around using North(N), East(E), South(S), and West(W). You can use commands "
                              "possible to see a list of \n"
                              "possible commands. The end goal is to find out why you are the only one in the current "
                              "world.")
                    if command == "craft":
                        crafting()
                    if command == "attack enemy":
                        if len(current_node.enemies) >= 0:
                            current_character.attacking()
                        else:
                            print("There are no enemies here.")
                    if command == "main weapon":
                        new_ranged_weapon_q = None
                        for items in current_character.inventory:
                            print(items.name)
                        print("Please select a weapon.")
                        new_weapon = input("What weapon would you like to use? ").lower()
                        if new_weapon in weapons_types:
                            if new_weapon in current_character.inventory:
                                current_character.melee.remove(current_character.melee)
                                current_character.melee.append(new_weapon)
                                current_character.damage = current_character.melee.damage
                                print("Your new melee weapon is %s." % current_character.melee)
                                print("Your attack damage is now %s." % current_character.damage)
                            else:
                                print("You do not have this item in your inventory. pls select another item.")
                                print("You are going to need to do the whole process all over again.")
                        else:
                            print("This is not a weapon.")
                        print("This is your ranged weapon: \n%s" % current_character.ranged_weapon)
                        while new_ranged_weapon_q != "no":
                            new_ranged_weapon_q = input("Would you like to change your ranged weapon too? ").lower()
                            if new_ranged_weapon_q == "yes":
                                for items in current_character.inventory:
                                    print(items.names)
                                new_ranged_weapon = input("What would you like to change your for your ranged weapon? ")
                                if new_ranged_weapon in ranged_types:
                                    current_character.ranged_weapon.remove(current_character.ranged_weapon)
                                    current_character.ranged_weapon.append(new_ranged_weapon)
                                    current_character.damage += current_character.ranged_weapon.damage
                                    print("Your new ranged weapon is %s." % current_character.ranged_weapon)
                                    print("Your attack damage is now %s." % current_character.damage)
                                else:
                                    print("You do not have this item in your inventory. pls select another item.")
                                    print("You are going to need to do the whole process all over again.")
                            else:
                                current_character.damage += current_character.ranged_weapon.damage
                    if command == "put on armor":
                        for armor_types in current_character.inventory:
                            print(armor_types.names)
                        print("please select an armor piece.")
                        new_armor = input("What armor would you like to put on? ")
                        if new_armor in armor_types:
                            if new_armor in current_character.inventory:
                                current_character.armor_type.remove(current_character.armor_type)
                                current_character.armor_type.append(new_armor)
                                print("Your new armor is %s." % current_character.armor_type)
                            else:
                                print("You do not have this item in your inventory. pls select another item.")
                                print("You are going to need to do the whole process all over again.")
                        else:
                            print("This is not an armor piece.")
                    if command == "alchemist craft":
                        alchemist_crafting()
                    if command == "use fireworks":
                        if firework.amount > 0:
                            firework.amount -= 1
                            print("Boom!!")
                            print("You used one firework. Hopefully you didn't attract any enemies.")
                    if command == "farm":
                        if current_node == GARDEN:
                            farm_item = random.randint(farm)
                            farm_amount = random.randint(1, 10)
                            got_it_1 = random.randint(1, 6)
                            got_it_2 = random.randint(1, 6)
                            got_it = got_it_1 + got_it_2
                            if got_it == 7:
                                if farm_item not in current_character.inventory:
                                    current_character.inventory.append(farm_item)
                                farm_item.amount += farm_amount
                                if mine_amount == 1:
                                    print("You mined %s of %s." % (farm_amount, farm_item))
                                if mine_amount > 1:
                                    print("You mined %s of %ss." % (farm_amount, farm_item))
                                print("You got %s of %s." % (farm_amount, farm_item))
                            else:
                                print("You didn't get anything because you didn't farm correctly.")
                        else:
                            print("You can only use this command in the garden.")
                    if command == "mine":
                        if current_node == MINE_SHAFT:
                            if pickaxe in current_character.mining_equipment:
                                mine_item = random.randint(mine)
                                mine_amount = random.randint(1, 10)
                                got_it_1 = random.randint(1, 6)
                                got_it_2 = random.randint(1, 6)
                                got_it = got_it_1 + got_it_2
                                if got_it == 7:
                                    if mine_item not in current_character.inventory:
                                        current_character.inventory.append(mine_item)
                                    if mine_amount == 1:
                                        print("You mined %s of %s." % (mine_amount, mine_item))
                                    if mine_amount > 1:
                                        print("You mined %s of %ss." % (mine_amount, mine_item))
                                else:
                                    mine_item = stone
                                    if stone not in current_character.inventory:
                                        current_character.inventory.append(stone)
                                mine_item.amount += mine_amount
                            else:
                                print("You either don't have your pickaxe in mining equipment or you don't have a "
                                      "pickaxe at all.")
                        else:
                            print("You can only use this command in the mine shaft.")
                else:
                    print()
                    print("command not recognized")

if not current_character.alive:
    print("You have died.")
    print("You died on move %s" % moves)
    print("good luck next time.")
else:
    print("you have lived")
    print("You finished the game with %s moves." % moves)
