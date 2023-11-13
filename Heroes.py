# Heroes class

import random as r
import Damage as dmg

class Hero:
    def __init__(self , ID=int ,name = str , base_hp = int,base_atk = int, base_defend = int , base_spd=int , skill = int) -> None:
        self.name = name
        self.hp = base_hp
        self.atk = base_atk
        self.defend = base_defend
        self.spd = base_spd
        self.id = ID
        self.skill = skill

    def get_name(self):
        return self.name
    def get_hp(self):
        return self.hp
    def get_atk(self):
        return self.atk
    def get_defend(self):
        return self.defend
    def get_spd(self):
        return self.spd
    def get_id(self):
        return self.id

# Boss
boss = Hero(9999,"BOSS   ",r.randint(100,200),r.randint(30,70),r.randint(10,50),r.randint(50,120),0)   