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

class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power 

Hero = Hero(10, 5)
Goblin = Goblin(6, 2)

def main():

    while Goblin.health > 0 and Hero.health > 0:
        print("You have {} health and {} power.".format(Hero.health, Hero.power))
        print("The goblin has {} health and {} power.".format(
            Goblin.health, Goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        # print("> ", end='')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            Goblin.health -= Hero.power
            print("You do {} damage to the goblin.".format(Hero.power))
            if Goblin.health <= 0:
                print("The goblin is dead.")
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if Goblin.health > 0:
            # Goblin attacks hero
            Hero.health -= Goblin.power
            print("The goblin does {} damage to you.".format(Goblin.power))
            if Hero.health <= 0:
                print("You are dead.")

main()