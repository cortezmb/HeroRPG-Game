#!/usr/bin/env python

# In this simple RPG game, the Hero fights the Goblin. He has the options to:

# 1. fight Goblin
# 2. do nothing - in which case the Goblin will attack him anyway
# 3. flee

# Hero class that stores health and power
class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self):
        # Hero attacks goblin
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero.power))
        if goblin.health <= 0:
            print("The goblin is dead.")

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power 

    def attack(self):
        # Goblin attacking Hero
        hero.health -= goblin.power
        print("The goblin does {} damage to you.".format(goblin.power))
        if hero.health <= 0:
            print("You are dead.")

hero = Hero(10, 5)
goblin = Goblin(6, 2)

def main():

    while goblin.health > 0 and hero.health > 0:
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end='')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            Hero.attack(Goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            Goblin.attack(Hero)

main()