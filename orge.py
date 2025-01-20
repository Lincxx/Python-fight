from enemy import *
import random
class Orge(Enemy):

    def __init__(self, attack_damage, health_points):
        super().__init__(type_of_enemy='Orge', 
                         attack_damage=attack_damage, 
                         health_points=health_points)


    def talk(self):
        print(f'*Slamming hands all around*')
    
    def special_attack(self):
        did_special_attack = random.random() < 0.2
        if did_special_attack:
            self.attack_damage += 4
            print(f'*Orge gets anrgy and does 4 attack damage*')
