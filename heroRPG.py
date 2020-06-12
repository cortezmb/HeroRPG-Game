#!/usr/bin/env python

# In this simple RPG game, the Hero fights the Goblin. He has the options to:

# 1. fight Goblin
# 2. do nothing - in which case the Goblin will attack him anyway
# 3. flee

# Import random.py module
import random

chance_double = random.randint(1, 10)
# Character class that will be the parent of Hero and Goblin
class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        self.power_double = self.power * 2  
    
    def alive(self):
        if self.health > 0:
            return True
        else: 
            return False

    def attack(self, enemy):
        enemy.health -= self.power
        chance_double = random.randint(1, 10)

         # Hero attacks Goblin
        if self.character_name == "hero":
            if chance_double == 2:
                print(f"You do {self.power_double} damage to the {enemy.character_name}.")
                return main()
            else:
                print(f"You do {self.power} damage to the {enemy.character_name}.")                       
            if enemy.health <= 0:
                print(f"The {enemy.character_name} is dead.")
            return main() 

        #Goblin attacks Hero
        if self.character_name == "goblin":
            print(f"The {self.character_name} does {self.power} damage to you.")
            if enemy.health <= 0:
                print(f"The {enemy.character_name} is dead.")
            return main()

        #Goblin attacks medic
        if enemy.character_name == "medic":
            if chance_double == 2:
                print(f"The {self.character_name} does {self.power} damage to {enemy.character_name}.")
        return main()

        #Goblin attacks shadow
        if enemy.character_name == "shadow":
            if chance_double == 1:
                print(f"The {self.character_name} does {self.power} damage to {enemy.character_name}.")
            elif enemy.health <= 0:
                print(f"The {enemy.character_name} is dead.")
            return main()

    def print_status(self, enemy):
        self.power_double = self.power * 2 
        chance_double = random.randint(1, 10)


        #Health and power status of Hero
        if self.character_name == "hero":
            print(f"You have {self.health} health and {self.power} power.")

        #Health and power status of Goblin
        if self.character_name == "goblin": 
            if self.power_double == True:
                enemy.health_half = enemy.health / 2     
                print(f"The {enemy.character_name} has {enemy.health_half} health and {enemy.power} power.")
            else:
                print(f"The {enemy.character_name} has {enemy.health} health and {enemy.power} power.")

        #Health and power status of Medic
        if self.character_name == "medic":
            if chance_double == 2:
                enemy.health = enemy.health + 2
                print(f"The {enemy.character_name} has {enemy.health} health and {enemy.power} power.")
            else:
                enemy.health != enemy.health + 2
                print(f"The {enemy.character_name} has {enemy.health} health and {enemy.power} power.")

        #Health and power status of Shadow
        if self.character_name == "shadow":
            chance_single = random.randint(1, 10)
            if chance_single == 1:
                enemy.health -= self.power
                print(f"The {enemy.character_name} has {enemy.health} health and {enemy.power} power.")
            elif chance_single != 1:
                print(f"The {enemy.character_name} has {enemy.health} health and {enemy.power} power.")

# Hero class that stores health and power
class Hero(Character):
    def __init__(self, health, power):
        self.character_name = "hero"
        # Manually call the constructor in base class. Then pass in health and power. 
        super(Hero, self).__init__(health, power)
        

# Goblin class that stores health and power
class Goblin(Character):
    def __init__(self, health, power):
        self.character_name = "goblin"
        super(Goblin, self).__init__(health, power)
        self.alive_name = "goblin"

# Medic class that stores health and power
class Medic(Character):
    def __init__(self, health, power):
        # Manually call the constructor in base class. Then pass in health and power. 
        self.character_name = "medic"
        super(Medic, self).__init__(health, power)

# Shadow class that stores health and power
class Shadow(Character):
    def __init__(self, health, power):
        self.character_name = "shadow"
        super(Shadow, self).__init__(health, power)

hero = Hero(10, 1)
goblin = Goblin(10, 1)
medic = Medic(10, 1)
shadow = Shadow(1, 0)

def main():

    while goblin.alive() and hero.alive() and medic.alive() and shadow.alive():
        hero.print_status(hero) 
        goblin.print_status(goblin)
        medic.print_status(medic)
        shadow.print_status(shadow)
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

            #Goblin attacks Hero
            return goblin.attack(hero) and goblin.attack(shadow) and goblin.attack(medic)
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))
            return False

main()