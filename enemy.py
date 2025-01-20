class Enemy:
    
    # type_of_enemy:str
    # health_points: int 
    # attack_damage: int 

    def __init__(self, type_of_enemy, attack_damage, health_points):
        self.__type_of_enemy = type_of_enemy # private variable
        self.attack_damage = attack_damage 
        self.health_points = health_points

    # setters

    # getters
    def get_type_of_enemy(self):
        return self.__type_of_enemy

    def talk(self):
        print(f'I am a {self.type_of_enemy}. Be prepared to fight!')

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you.')

    def attack(self):   
       print(f'{self.type_of_enemy} attacks you for {self.attack_damage} damage.') 