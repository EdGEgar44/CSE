import random

# Move

# Attack

# take damage

# Regeneration

# Dialogue


class Characters(object):
    def __init__(self, name, inventory, health, armor, damage, description):
        self.name = name
        self.inventory = inventory
        self.health = health
        self.armor = armor
        self.damage = damage
        self.description = description

    def diologue(self):
            print("You shall not pass. It is I, Gabe, the one that changed the world. If you want to get your family \n"
                  "and friends and everyone in your world back, you have to get past me.")

    def attacked(self, armor, attack_damage):
        if armor >= 1:
            attack_damage = enemy.damage - armor
            if enemy.armor <= enemy.damage:
                attack_damage = armor - enemy.damage

    def attacking(self, target_health):
        target_health = enemy.health - enemy.damage


enemy = Characters("Gabe", ["pickaxe", "Torch", "Sword", "wallet"], 100, 10, 99,
                   "The Enemies name is Gabe, he is one of the hardest people to fight. He have killed many people \n"
                   "for trying to solve the puzzle. They never got to the question so they weren't able to tell \n"
                   "people the question.")

current_character = Characters("John", ["paper"], 100, 0, 99, "You are yourself. Don't let anyone change that.")
