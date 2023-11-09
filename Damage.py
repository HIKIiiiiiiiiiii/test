#Damage caluculating class

def damage_calculate(attacker = float ,defender = float,damage_reduction=float):
    damage = float
    minimal = attacker/20

    if attacker<defender:
        damage = minimal + (attacker*attacker/defender)-(100*damage_reduction*attacker)
    else:
        damage = minimal + (attacker*2/defender)-(100*damage_reduction*attacker)
    return damage

def user_took_damage(user_HP = float , damage_took = float):
    user_curruent_HP = user_HP-damage_took
    if user_curruent_HP<=0:
        user_curruent_HP=0
    return user_curruent_HP
