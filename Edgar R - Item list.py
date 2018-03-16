class Items(object):
    def __init__(self, name, description, durability, drop):
        self.name = name
        self.description = description
        self.durability = durability
        self.drop = drop

    def drop(self):
        self.drop = True
        print("You dropped %s." % self.name)


class Enchanted(Items):
    def __init__(self, name, description, durability, enchanted, drop):
        super(Enchanted, self).__init__(name, description, durability, drop)
        self.enchanted = enchanted

    def usage(self):
        if self.name == "armor of undying":
            print("You have been revived. But your armor is now broken.")
        if self.name == "armor of strength":
            print("Your durability is now %s" % self.durability)


class Keys(Items):
    def __init__(self, name, description, durability, door, drop, door_number):
        super(Keys, self).__init__(name, description, durability, drop)
        self.door = door
        self.door_number = door_number

    def use(self):
        if self.door_number == 1:
            print("You used %s. The door that you opened was %s." % (self.name, self.door))


class Edibles(Items):
    def __init__(self, name, description, durability, drop):
        super(Edibles, self).__init__(name, description, durability, drop)

    def consume(self):
        print("You consumed %s" % self.name)


class Material(Items):
    def __init__(self, name, description, durability, drop):
        super(Material, self).__init__(name, description, durability, drop)

    def crafting(self):
        if command == "armor of undying":
            if "cosmonium" in current_character.inventory:


class Armor(Items):
    def __init__(self, name, description, durability, drop):
        super(Armor, self).__init__(name, description, durability, drop)


class Weapons(Items):
    def __init__(self, name, description, durability, drop):
        super(Weapons, self).__init__(name, description, durability, drop)


class Characters(object):
    def __init__(self, name, inventory, health, armor, damage, weapon, description, diologue):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.armor = armor
        self.damage = damage
        self.description = description
        self.diologue = diologue
        self.weapon = weapon

    def attacked(self):
        if self.armor >= 1:
            self.damage = self.damage - self.armor
            if self.armor <= enemy.damage:
                self.damage = self.armor - enemy.damage
                self.damage = self.damage
        if self.weapon:
            self.damage = self.damage * 2.5

    def attacking(self):
        if self.armor >= 1:
            self.damage = self.damage - self.armor
            if self.armor <= enemy.damage:
                self.damage = self.armor - enemy.damage
                self.damage = self.damage
        if self.weapon:
            self.damage = self.damage * 2.5
        enemy.health = enemy.health - enemy.damage


enemy = Characters("Gabe", ["pickaxe", "Torch", "Sword", "wallet"], 100, 10, 20, False,
                   "The Enemies name is Gabe, he is one of the hardest people to fight. He have killed many people \n"
                   "for trying to solve the puzzle. They never got to the question so they weren't able to tell \n"
                   "people the question.",
                   ["It is I, Gabe, the one that changed the world. If you want to get your family and friends and \n"
                    "everyone in your world back, you have to get past me.", "In order to solve you family, you need \n"
                    "to solve the puzzle.", "You have defeated me. You may solve the riddle. But be worn. If you \n"
                    "don't solve it within your third try, you will die. So be worn."])

current_character = Characters("John", ["5 Bags of Beans"], 100, 0, 10, False, "You are yourself. Don't let "
                               "anyone change that.", None)

current_node = BACK_MALL
directions = ['north', 'east', 'south', 'west']
short_directions = ['n', 'e', 's', 'w']

moves = 0

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
        print("health: %s" % current_character.health)
        print(current_node.name)
        print()
        if current_node.again:
            print(current_node.description_2)
        else:
            print(current_node.description)
            current_node.again = True
        command = input('>_').lower()
        if command == 'quit':
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
            else:
                if command == 'my description':
                    print(current_character.description)
                else:
                    print("Command not recognize")
