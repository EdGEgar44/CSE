import random

# Move

# Attack

# take damage

# Regeneration

# Dialogue


class Characters(object):
    def __init__(self, name, inventory, health, armor, description):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.armor = armor
        self.description = description

    def move(self, direction):
        current_location = FORGOTTEN_R
        location_1 = BO_BO
        location_2 = LIGHT_R
        if current_node == BO_BO:
            current_location = BO_BO
            print("You shall not pass. It is I, Gabe. ")



    def attack(self, damage, armor, attack_damage):
        if armor >= 1:
            attack_damage = health - armor
            if enemy.armor <= damage:
                attack_damage = armor - damage


    def damage(self,health, armor):


c_location = TELEPORTER_R

enemy = Characters("Gabe", ["pickaxe", "Torch", "Sword", "wallet"], 100, 10,
                   "The Enemies name is Gabe, he is one of the hardest people to fight. He have killed many people \n"
                   "for trying to solve the puzzle. They never got to the question so they weren't able to tell \n"
                   "people the question.")
