#Damage caluculating class

import random

def damage_calculate(attacker = int , defender = int , crit = False):
    minimal = attacker/20
    
    if attacker<defender:
        damage = (minimal + attacker*attacker) / (defender * 0.9)
    else:
        damage = (minimal + attacker*2) - (defender * 0.9)

    # In case the damage reduction is too much
    if damage <= 0:
        damage = minimal
    
    if crit == True:
        damage*=2

    return int(damage)

def user_took_damage(user_HP = int , damage_took = int):
    user_HP -= damage_took

    # In case player HP is displayed as negative number on the terminal
    if user_HP <= 0:
        user_HP = 0

    return user_HP

def user_heal(user_curruent_hp = int , heal_amount = int , user_max_hp = int):
    user_curruent_hp+=heal_amount*(random.randint(70,100)/100)

    # In case user overhealed 
    if user_curruent_hp>user_max_hp:
        user_curruent_hp=user_max_hp

    return user_curruent_hp

def user_stat_up(stat = int , amount = int , stat_type = str):
    stat += amount

    # In case the stats went above the maximum stat
    if stat_type.lower() == "atk":
        if stat > 200:
            print("ATK cannot go above 200 !")
            stat = 200
    elif stat_type.lower() == "def":
        if stat > 50:
            print("DEF cannot go above 50 !")
            stat = 50
    elif stat_type.lower() == "spd":
        if stat > 150:
            print("SPD cannot go above 150 !")
            stat = 150

    return stat

def user_stat_down(stat = int , amount = int , stat_type = str):
    stat -= amount

    # Lowest possible stat is 10 for each stat
    if stat < 10:
        print(f"{stat_type} cannot go any lower than 10 !")
        stat=10

    return stat