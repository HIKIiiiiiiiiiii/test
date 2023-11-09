# Main runnning file
import os
import random

import Heroes
import Damage



def main():
    os.system("clear")

    print("Please select one of the fighter : ")
    print("ID Name    HP  ATK  DEF  SPD\n ")

    for i in range(len(Heroes.hero_list)):
        print(f"{Heroes.hero_list[i].get_id()}  {Heroes.hero_list[i].get_name()} ",end="")
        print(f"{Heroes.hero_list[i].get_hp()} {Heroes.hero_list[i].get_atk()} ",end="")
        print(f"{Heroes.hero_list[i].get_defend()} {Heroes.hero_list[i].get_spd()} \n")

    while True:
        user_input=input("Input a number indicated to the fighter : ")

        if user_input.isdigit()==False:
            print("Please input a number")
            continue
        else:
            player_data = Heroes.hero_list[int(user_input)-1]
            break

    os.system("clear")

    print("You  : ")
    print("Name    HP  ATK  DEF  SPD")
    print(f"{player_data.get_name()} {player_data.get_hp()} {player_data.get_atk()}   {player_data.get_defend()}  {player_data.get_spd()}")
    print("\nBoss : ")
    print("Name    HP  ATK  DEF  SPD")
    print(f"{Heroes.boss.get_name()} {Heroes.boss.get_hp()} {Heroes.boss.get_atk()}   {Heroes.boss.get_defend()}  {Heroes.boss.get_spd()}")

main()