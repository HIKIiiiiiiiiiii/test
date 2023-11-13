# Heroes class

import random
import Damage as dmg

class Hero:
    def __init__(self , ID=int ,name = str , base_hp = int,base_atk = int, base_defend = int , base_spd=int , skill = str) -> None:
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
boss=Hero(9999,"BOSS   ",random.randint(100,200),random.randint(30,70),random.randint(10,50),random.randint(50,120))    

# List of heroes :
hero_list = []
hero_list.append(Hero(1,"Rei     ",100,30,20,100,"Defend break"))
hero_list.append(Hero(2,"Sei     ",100,20,30,90,"Heal"))
hero_list.append(Hero(3,"Hina    ",150,10,40,80,"Block"))
hero_list.append(Hero(4,"Ichi    ",50,70,20,120,""))