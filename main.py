from enemy import * 
from zombie import *
from orge import *


zombie = Zombie(1, 10)
orge = Orge(3, 20)
# zombie.type_of_enemy = "Zombie"
# zombie.attack_damage = 1
# zombie.health_points = 10

print(zombie.get_type_of_enemy())
print(zombie.talk())
print(zombie.spread_disease())

print(orge.get_type_of_enemy())
print(orge.talk())
# print(orge.spread_disease())



