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

# Hero class that stores health and power
class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self):
        # Hero attacks goblin
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))
        if goblin.health <= 0:
            print("The goblin is dead.")
        else:
            return main()

    def alive(self):
        # Since I am in the Hero class, I use self.health
        if self.health > 0:
            return True
        else: 
            return False

    def print_status(self):
        if self.alive():
            print("You have {} health and {} power.".format(hero.health, hero.power))
        else:
            return main()

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power 

    def attack(self):
        # Goblin attacking Hero
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")
        else:
            return main()

    # Every method has a self parameter
    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    def print_status(self):
        if self.alive():
           print("The goblin has {} health and {} power.".format(goblin.health, goblin.power)) 
        else:
            return main()

hero = Hero(10, 5)
goblin = Goblin(6, 2)

def main():

    while goblin.alive() and hero.alive():
        hero.print_status() 
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end='')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            return hero.attack()

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive():
            # Goblin attacks hero
            return goblin.attack()
        else:
            return False

main()