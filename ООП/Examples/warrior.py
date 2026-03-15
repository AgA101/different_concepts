from random import randint, choice
class Warrior:
    def __init__(self, id: int):
        self.health = 100
        self.id = id

    def take_damage(self, damage: int):
        self.health -= damage
        if self.health < 0:
            self.health = 0 
        
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class CombatZone:
    def __init__(self, warriors: list[Warrior]):
        self.warriors = warriors

    def start_battle(self):
        
        while len(self.warriors) > 1:
            attacked_warrior = choice(self.warriors)
            damage = randint(10,20)
            attacked_warrior.take_damage(damage)
            print(f'Атакован воин с id={attacked_warrior.id} получил урон={damage}, здоровье=({attacked_warrior.health}/100)')

            if not(attacked_warrior.is_alive()):
                self.warriors.remove(attacked_warrior)
                print(f'Воин с id={attacked_warrior.id} был убит.')
        
        else:
            print(f'Воин с id={self.warriors[0].id} выиграл')


def main():
    warriors = [Warrior(i) for i in (1, 2, 3, 4, 5)]
   
    zone = CombatZone(warriors)
    zone.start_battle()
    
if __name__ == '__main__':
    main()