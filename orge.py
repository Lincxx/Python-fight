from enemy import *

class Orge(Enemy):

    def __init__(self, attack_damage, health_points):
        super().__init__(type_of_enemy='Orge', 
                         attack_damage=attack_damage, 
                         health_points=health_points)


    def talk(self):
        print(f'*Slamming hands all around*')
