# Heroes class

import random

class Hero:
    def __init__(self,name = str , base_hp = int,base_atk = int, base_defend = int ,base_spd=int, id=int) -> None:
        self.name = name
        self.hp = base_hp
        self.atk = base_atk
        self.defend = base_defend
        self.spd=base_spd
        self.id=id

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
boss=Hero("BOSS   ",random.randint(100,200),random.randint(30,70),random.randint(10,50),random.randint(50,120),9999)    

# List of heroes :
hero_list = []
hero_list.append(Hero("Rei    ",100,30,20,100,1))
hero_list.append(Hero("Sei    ",100,20,30,90,2))
hero_list.append(Hero("Hina   ",150,10,40,80,3))
hero_list.append(Hero("Ben    ",50,70,20,120,4))