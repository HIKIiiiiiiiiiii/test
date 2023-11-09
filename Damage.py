#Damage caluculating class

import random

def damage_calculate(attacker = int , defender = int , damage_reduction=int):
    damage = int
    minimal = attacker/20
    
    if attacker<defender:
        damage = minimal + (attacker*attacker/defender)-(100*damage_reduction*attacker)
    else:
        damage = minimal + (attacker*2/defender)-(100*damage_reduction*attacker)

    # In case the damage reduction is too much
    if damage<=0:
        damage=minimal
    else:
        pass

    return damage

def user_took_damage(user_HP = int , damage_took = int):
    user_curruent_HP = user_HP-damage_took

    # In case player HP is displayed as negative number on the terminal
    if user_curruent_HP<=0:
        user_curruent_HP=0

    return user_curruent_HP

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
        if stat > 150:
            stat = 200
    elif stat_type.lower() == "def":
        if stat > 50:
            stat = 50
    elif stat_type.lower() == "spd":
        if stat > 150:
            stat = 150

    return stat
