from enemy import *
import random
class Zombie(Enemy):

    def __init__(self, attack_damage, health_points):
        super().__init__(type_of_enemy='Zombie', 
                         attack_damage=attack_damage, 
                         health_points=health_points)


    def talk(self):
        print(f'*Grumbling...*')

    def spread_disease(self):
        print(f'*Spreading disease*')

    def special_attack(self):
        did_special_attack = random.random() < 0.5
        if did_special_attack:
            self.health_points += 2
            print(f'*Zombie regenerates 2 health points*')