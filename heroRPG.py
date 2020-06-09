#!/usr/bin/env python

# In this simple RPG game, the Hero fights the Goblin. He has the options to:

# 1. fight Goblin
# 2. do nothing - in which case the Goblin will attack him anyway
# 3. flee

# Parent is Character. This will allow us to add more characters in addition to Hero and Goblin
class Character(): 
    # Creating a constructor
    def __init__(self):

    def alive(self):
        # health > 0
        Hero_health = Hero_health > 0
        Goblin_health = Goblin_health > 0  

    # Creating a method for Hero attacking the Goblin
    def attack(self):
        # Goblin_health -= Hero_power
        Goblin.health -= Hero.power
        print("You do {} damage to the Goblin.".format(Hero_power))
        if Goblin_health <= 0:
            print("The Goblin is dead.")

    def print_status(self):
        print("You have {} health and {} power.".format(Hero_health, Hero_power))
        print("The Goblin has {} health and {} power.".format(
        Goblin_health, Goblin_power))

# One of the children is Hero. Hero is a child of Character due to universal attributes of a character. 
class Hero(Character):
    # Creating a constructor
    def __init__(self):
        self.Hero_health = 10
        self.Hero_power = 5
    
# One of the childer is Goblin. Hero is a child of Character due to universal attributes of a character. 
class Goblin(Character):
    # Creating a constructor
    def __init__(self):
        self.Goblin_health = 6
        self.Goblin_power = 2

def main():
    Hero = Hero() 
    Goblin = Goblin()

    while Goblin.alive(Hero) and Hero.alive(Goblin):
        Hero.print_status(Hero)
        Goblin.print_status(Goblin)
        print()
        print("What do you want to do?")
        print("1. fight Goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            Hero.attack(Goblin)

        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if Goblin_health > 0:
            Goblin.attack(Hero)

main()
# Method example
#Goblin.attack
#make a parent class called: character
#all characters will have a health, power, attack
#when either reaches 0 health, the other wins