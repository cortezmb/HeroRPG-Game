#!/usr/bin/env python

# In this simple RPG game, the Hero fights the Goblin. He has the options to:

# 1. fight Goblin
# 2. do nothing - in which case the Goblin will attack him anyway
# 3. flee

# Character class that will be the parent of Hero and Goblin
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    def attack(self, enemy):
        # Hero attacks Goblin
        if enemy.character_name != "zombie":
            enemy.health -= self.power

        if self.character_name == "hero":
            print(f"You do {self.power} damage to the {enemy.character_name}.")

        if enemy.health <= 0:
            print(f"The {enemy.character_name} is dead.")

        #Goblin attacks Hero
        if self.character_name == "goblin":
            print(f"The {self.character_name} does {self.power} damage to you.")

        if self.character_name == "zombie":
            self.health += hero.power
            print(f"The {self.character_name} does {self.power} damage to you.")             
        return main()

    def print_status(self, enemy):
        if self.character_name == "hero":
            print(f"You have {self.health} health and {self.power} power.")
        elif self.character_name == "goblin":
            print(f"The {enemy.character_name} has {enemy.health} health and {enemy.power} power.") 
        if self.character_name == "zombie":
            print(f"The {self.character_name} has {self.health} health and {self.power}")

# Hero class that stores health and power
class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        # Manually call the constructor in base class. Then pass in health and power. 
        super(Hero, self).__init__(health, power)

class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power)
        self.alive_name = "goblin"

class Zombie(Character):
    def __init__(self, health, power):
        self.character_name = "zombie"
        # Manually call the constructor in base class. Then pass in health and power. 
        super(Zombie, self).__init__(health, power)

hero = Hero(10, 5)
goblin = Goblin(6, 2)
zombie = Zombie(10, 1)

def main():

    while goblin.alive() and hero.alive() and zombie.alive():
        hero.print_status(hero) 
        goblin.print_status(goblin)
        zombie.print_status(zombie)
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. have zombie attack")
        print("4. flee")
        print("> ", end='')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            return hero.attack(goblin)
        elif raw_input == "2":
            #Goblin attacks Hero
            return goblin.attack(hero)
        elif raw_input == "3":
            #Zombie attack Hero
            return zombie.attack(hero)
        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
            return False

main()