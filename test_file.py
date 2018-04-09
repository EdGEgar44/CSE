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


class Edible(Item):
    def __init__(self, name, description, durability, drop, amount):
        super(Edible, self).__init__(name, description, durability, drop, amount)

    def consume(self):
        print("You consumed %s" % self.name)


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


current_character = Characters("John", ["beans \n"], 100, 0, 10, False,
                               "You are yourself. Don't let anyone change that.", None, False, True)

raw_potato = Food("raw potato \n",
                  "You can eat this raw potato. But it looks so weird.", 1, 5, True, 1)

test = True

while test:
    grab = input(">_").lower()
    if grab == "grab raw potato":
        current_character.inventory.append(raw_potato.name)
        raw_potato.drop = False
        print("".join(current_character.inventory))
