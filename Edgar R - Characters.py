import random

# Move

# Attack

# take damage

# Regeneration

# Dialogue


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
