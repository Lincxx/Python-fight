from enemy import *

class Zombie(Enemy):

    def __init__(self, attack_damage, health_points):
        super().__init__(type_of_enemy='Zombie', 
                         attack_damage=attack_damage, 
                         health_points=health_points)


    def talk(self):
        print(f'*Grumbling...*')

    def spread_disease(self):
        print(f'*Spreading disease*')