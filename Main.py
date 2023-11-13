# Main runnning file

import os
import random
# My mpduels or whatever it called
import Heroes
import Damage



def main():
    os.system("clear")

    turn_1 = turn_2 = [int , str , int , int , int ,int]
    turn_counter = 1
    boss = Heroes.boss

    print("===============================================================================")
    print("                           WELCOME TO THE FIGHTING GAME                        ")
    print("\nYou will choose one of the hero and you need to defeat a boss that have random stat ! ")
    print("Please select your hero : ")
    print("ID Name     HP  ATK  DEF  SPD\n ")

    for i in range(len(Heroes.hero_list)):
        print(f"{Heroes.hero_list[i].get_id()}  {Heroes.hero_list[i].get_name()} ",end="")
        print(f"{Heroes.hero_list[i].get_hp()} {Heroes.hero_list[i].get_atk()} ",end="")
        print(f"{Heroes.hero_list[i].get_defend()} {Heroes.hero_list[i].get_spd()} \n")

    while True:
        user_input = input("Input a number indicated to the fighter : ")

        if user_input.isdigit() == False:
            print("Please input a number")
            continue
        else:
            player_data = Heroes.hero_list[int(user_input)-1]
            break

    os.system("clear")

    if boss.spd > player_data.get_spd():
        turn_1 = boss
        turn_2 = player_data
    else:
        turn_2 = boss
        turn_1 = player_data

    while True:
        print("===============================================================================")
        print("You  : ")
        print("Name     HP  ATK  DEF  SPD")
        print(f"{player_data.get_name()} {player_data.get_hp()} {player_data.get_atk()}   {player_data.get_defend()}  {player_data.get_spd()}")
        print("\nBoss : ")
        print("Name     HP  ATK  DEF  SPD")
        print(f"{boss.get_name()}  {boss.get_hp()} {boss.get_atk()}   {boss.get_defend()}  {boss.get_spd()}\n")

        if turn_1.hp == 0 :
            print("*******************")
            print(f"{turn_2.name} won !")
            print("*******************")
            break
        elif turn_2.hp == 0:
            print("*******************")
            print(f"{turn_1.name} won !")
            print("*******************")
            break
        else:
            if turn_counter == 1:
                a = int(Damage.damage_calculate(turn_1.atk,turn_2.defend))
                turn_2.hp = Damage.user_took_damage(turn_2.hp,a)
                print(f"{turn_1.name} did {a} damage to {turn_2.name} !")
                turn_counter = 2
            else :
                a = Damage.damage_calculate(turn_2.atk,turn_1.defend)
                turn_1.hp = Damage.user_took_damage(turn_1.hp,a)
                print(f"{turn_2.name} did {a} damage to {turn_1.name} !")
                turn_counter = 1
        
main()