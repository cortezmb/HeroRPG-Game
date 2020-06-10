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
        # Hero attacks goblin
        enemy.health -= self.power
        if self.character_name == "hero":
            print(f"You do {self.power} damage to the {enemy.character_name}.")
        if enemy.health <= 0:
            print(f"The {enemy.character_name} is dead.")
        if self.character_name == "goblin":
            print(f"The {self.character_name} does {self.power} damage to you.")      
        return main()

# Hero class that stores health and power
class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        #Why and when is this needed?
        super(Hero, self).__init__(health, power)
    # def attack(self):
    #     # Hero attacks goblin
    #     goblin.health -= hero.power
    #     print("You do {} damage to the goblin.".format(hero.power))
    #     if goblin.health <= 0:
    #         print("The goblin is dead.")
    #     else:
    #         return main()

    def print_status(self):
        if self.alive():
            print(f"You have {hero.health} health and {hero.power} power.")
        else:
            return main()

class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power)
    # def attack(self):
    #     # Goblin attacking Hero
    #     hero.health -= goblin.power
    #     print("The goblin does {} damage to you.".format(goblin.power))
    #     if hero.health <= 0:
    #         print("You are dead.")
    #     else:
    #         return main()

    def print_status(self):
        if self.alive():
           print(f"The goblin has {goblin.health} health and {goblin.power} power.") 
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
            return hero.attack(goblin)
        elif raw_input == "2":
            return goblin.attack(hero)
            # pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
        # if goblin.alive():
        #     # Goblin attacks hero
        #     return goblin.attack(hero)
        # else:
            return False

main()