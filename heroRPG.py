#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

# Parent is Character. This will allow us to add more characters in addition to Hero and Goblin
class Character(): 
    # Creating a constructor
    def __init__(self, health, power):
        # Adding instance variables
        self.health = health
        self.power = power 


# One of the children is Hero. Hero is a child of Character due to universal attributes of a character. 
class Hero(Character):
    # Creating a constructor
    def __init__(self):
       self.hero_health = 10
       self.hero_power = 5
    
    # Creating a method for Hero attacking the Goblin
    def attack(self, Goblin):
        # goblin_health -= hero_power
        goblin.health -= hero.power
        print("You do {} damage to the goblin.".format(hero_power))
        if goblin_health <= 0:
        print("The goblin is dead.")

    def alive(self):
        hero_health > 0

    def print_status(self):
        print("You have {} health and {} power.".format(hero_health, hero_power))

# One of the childer is Goblin. Hero is a child of Character due to universal attributes of a character. 
class Goblin(Character):
    # Creating a constructor
    def __init__(self):
        self.goblin_health = 6
        self.goblin_power = 2

    # Creating a method for Hero attacking the Goblin
    def attack(self, Hero):
        # hero_health -= goblin_power
        hero.health -= goblin.power 
        print("The goblin does {} damage to you.".format(goblin_power))
        if hero_health <= 0:
            print("You are dead.")   

    def alive(self):
    goblin_health > 0     

    def print_status(self):
        print("The goblin has {} health and {} power.".format(
        goblin_health, goblin_power))

# hero = Hero(10, 5)
# hero.health() 
# hero.power()

# goblin = Goblin(6, 2)
# goblin.health()
# goblin.power()
    
    def main():
        hero = Hero() 
        goblin = Goblin()

        while goblin.alive and hero.alive():
            hero.print_status()
            goblin.print_status()
            # print("You have {} health and {} power.".format(hero_health, hero_power))
            # print("The goblin has {} health and {} power.".format(
            #     goblin_health, goblin_power))
            print()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                hero.attack(Goblin)
                # Hero attacks goblin
                # goblin_health -= hero_power
                # print("You do {} damage to the goblin.".format(hero_power))
                # if goblin_health <= 0:
                #     print("The goblin is dead.")
            elif raw_input == "2":
                pass
            elif raw_input == "3":
                print("Goodbye.")
                break
            else:
                print("Invalid input {}".format(raw_input))

            if goblin_health > 0:
                # Goblin attacks hero
                # hero_health -= goblin_power
                # print("The goblin does {} damage to you.".format(goblin_power))
                # if hero_health <= 0:
                #     print("You are dead.")
                goblin.attack(Hero)


main()
# Method example
#goblin.attack
#make a parent class called: character
#all characters will have a health, power, attack
#when either reaches 0 health, the other wins