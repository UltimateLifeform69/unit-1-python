"""
Task 0

make a class for a videogame character
    -Create a method for healing
    -Make a player subclass with more health
"""

class Character:
    health = 20
    def __init__(self, name):
        self.name = name
        

        def damage(self, dmg=1):
            self.health = self.health - dmg
    


 
enemy1 = Character("Shadow")
enemy1.damage()
print(enemy1.health)

class player(Character):
    health = 50
    def healing(self):
        if self.health < 50:
            self.health = self.health + 2

player1 = player('Sonic')