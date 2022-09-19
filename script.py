from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import functions

import os
import time

os.system('clear')

def get_turn():
    try:
        turn = driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div[10]/div").text 
        return turn
    except:
        time.sleep(5)
        get_turn()


def printTurn():
    active_mons = driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div[6]").text
    print()
    temp = active_mons.split()
    mon_usr,mon_opp = functions.extract_mon_names(temp)
    functions.printData(mon_usr,mon_opp)
    print()
    functions.printData(mon_opp,mon_usr)

driver = webdriver.Chrome("chromedriver")

driver.get("https://play.pokemonshowdown.com/")

msg = input()

flag = True

temp = ""


if(msg == "R" or msg == "r"):
    while(True):
        turn = get_turn()
        if(turn is None) == False:
            if(turn != temp):
                temp = turn
                if(turn.split(" ")[0] == "Turn"):
                    os.system('clear')
                    print()
                    print(turn)
                    print()
                    printTurn()
