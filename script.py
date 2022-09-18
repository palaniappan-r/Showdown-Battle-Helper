from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import printTurn

import os

os.system('clear')

driver = webdriver.Chrome("chromedriver")

driver.get("https://play.pokemonshowdown.com/")

msg = input()

if(msg == "ok"):
    os.system('clear')
    active_mons = driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div[6]").text
    turn = driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/div[10]/div").text
    print(turn)
    print()
    temp = active_mons.split()
    mon_usr = temp[0].strip()
    mon_opp = temp[3].strip()
    printTurn.printData(mon_usr,mon_opp)
    print()
    printTurn.printData(mon_opp,mon_usr)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    finally:
        driver.quit()
    



#driver.find_element_by_name("username").send_keys(Keys.RETURN)