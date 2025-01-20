from enemy import * 
from zombie import *
from orge import *

# polymorphism
def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()
    while e1.health_points > 0 and e2.health_points > 0:
        print('------------')
        e1.special_attack()
        e2.special_attack()
        print(f'{e1.get_type_of_enemy()}: {e1.health_points} HP left')
        print(f'{e2.get_type_of_enemy()}: {e2.health_points} HP left')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage
        
    print('------------')
    if e1.health_points <= 0:
        print(f'{e2.get_type_of_enemy()} wins!')
    else:
        print(f'{e1.get_type_of_enemy()} wins!')
zombie = Zombie(5, 20)
orge = Orge(3, 20)
# # zombie.type_of_enemy = "Zombie"
# # zombie.attack_damage = 1
# # zombie.health_points = 10

# print(zombie.get_type_of_enemy())
# print(zombie.talk())
# print(zombie.spread_disease())

# print(orge.get_type_of_enemy())
# print(orge.talk())
# # print(orge.spread_disease())


battle(zombie, orge)

