from email.policy import default
from lib2to3.pgen2 import driver
import pandas as pd
import os
dataObj = pd.read_json('gen8randombattle.json')

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    OKRED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

import json
import urllib.request

def loadData():

    global dataObj
    dataObj = json.loads('gen8randombattle.json')
    
    return dataObj

def get_types(mon_name):
    df = pd.read_json('pokedex.json')
    mon_name = mon_name.lower().replace(" ","").replace("-","")
    mon_types = df[mon_name]['types']
    if(len(mon_types) == 1) : 
        type1 = mon_types[0]
        type2 = "-"
    else : 
        type1 = mon_types[0]
        type2 = mon_types[1]

    return type1,type2
    
def printData(mon_name,mon2_name):
    mon = dataObj[mon_name]
    lv = mon["level"]
    
    type1,type2 = get_types(mon2_name)
    
    print(
        f"{bcolors.BOLD}{bcolors.OKBLUE}{mon_name} Lv {lv}{bcolors.ENDC}{bcolors.ENDC}",end="\t"
        )
    
    print("Abilities : ",end="")
    for j in mon["abilities"] : print(f"{bcolors.OKCYAN}{j}{bcolors.ENDC}",end = "")
    
    print("\nItems : ",end="")
    for j in range(0,len(mon["items"])-1) : 
        s = mon["items"][j]
        print(f"{bcolors.HEADER}{s}{bcolors.ENDC}",end = "/")
    s = mon["items"][-1]
    print(f"{bcolors.HEADER}{s}{bcolors.ENDC}")
    
    moves = pd.read_csv('moves.csv')

    for j in mon["moves"] : 
        move_type = moves[moves['Name'] == j]['Type'].values[0]
        dmg = getDmg(move_type,type1,type2)
        move_cat = moves[moves['Name'] == j]['Category'].values[0]
        
        if(move_cat == 'Status'):
          print(f"{bcolors.WARNING}{j}{bcolors.ENDC} -> Status")  
          continue
        
        if dmg == 4:
            print(
            f"{bcolors.BOLD}{bcolors.OKGREEN}{j}{bcolors.ENDC} -> {dmg}"
            )
        elif dmg == 2:
            print(f"{bcolors.OKGREEN}{bcolors.BOLD}{j}{bcolors.ENDC}{bcolors.ENDC} -> {dmg}")
        elif dmg == 0.5:
            print(f"{bcolors.OKRED}{j}{bcolors.ENDC} -> {dmg}")
        elif dmg == 0.25:
            print(f"{bcolors.OKRED}{j}{bcolors.ENDC} -> {dmg}")
        elif dmg == 0:
            print(f"{j} -> {dmg}")
        else:
            print(f"{bcolors.WARNING}{j}{bcolors.ENDC} -> {dmg}")

pokemon_types = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice",
                 "Fighting", "Poison", "Ground", "Flying", "Psychic",
                 "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]

# A 2 Dimenstional Array Of Damage Multipliers For Attacking Pokemon:

def getDmg(move_type,mon_type1,mon_type2):
    damage_array =      [
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
                        [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
                        [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
                        [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
                        [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
                        [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
                        [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
                        [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
                        [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
                        [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
                        [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
                        [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
                        [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
                        [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
                        [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
                        [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]
                        ]

    if(mon_type2 != '-'):
        dmg = damage_array[pokemon_types.index(move_type)][pokemon_types.index(mon_type1)] * damage_array[pokemon_types.index(move_type)][pokemon_types.index(mon_type2)]
    else:
        dmg = dmg = damage_array[pokemon_types.index(move_type)][pokemon_types.index(mon_type1)]

    return dmg

                