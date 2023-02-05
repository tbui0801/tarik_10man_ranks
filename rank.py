import requests
import json
import numpy as np
import math
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

valorant_percentiles = {
"iron_1": 0,
"iron_2": 4,
"iron_3": 10,
"bronze_1": 16,
"bronze_2": 23,
"bronze_3": 30,
"silver_1": 40,
"silver_2": 48,
"silver_3": 55,
"gold_1": 62,
"gold_2": 68,
"gold_3": 73,
"plat_1": 77,
"plat_2": 81,
"plat_3": 85,
"diamond_1": 89,
"diamond_2": 91,
"diamond_3": 93,
"ass_1": 94,
"ass_2": 95,
"ass_3": 96,
"imm_1": 97,
"imm_2": 98,
"imm_3": 99,
"radiant_1": 100,
}

def get_player_list():
    site = "https://www.neatqueue.com/leaderboard/1061301529597976700/1061303977460908173"
    response = requests.get(site)
    chrome_options = Options()

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
        options=chrome_options)

    driver.get(site)
    driver.implicitly_wait(5) #allow some time to fully load, you may tweak accordingly

    # driver.set_window_size(w, h)
    driver.maximize_window()

    html = driver.page_source
    soup = BeautifulSoup(html)

    # rank_divs = soup.findAll("div", {"class":"nq-leaderboard-item row"})
    rank_divs = soup.findAll(class_="nq-leaderboard-item row")

    rank_list = []
    for div in rank_divs:
        player = div.text.split(" ")[1]
        rank_list.append(player)

    driver.quit()

    rank_list.reverse()

    return rank_list
    
def percentile(list, n): 
    total_values = len(list) 
    n_index = list.index(n)
    perc = (n_index/total_values) * 100

    return perc

# player_list = get_player_list()
player_list = ['tarikcelik', 'steel', 'hazed', 'Rawkus', 'tupperware', 'retrQ', 'thief', 'Cryo', 'mina', 'jawgemo', 'genghsta', 'kaay', 'bENITA', 'pho', 'Curry', 'FNS', 'BabyJ', 'nerve', 'ROY', 'PureVNS', 'Governor', 'Jazzyk1ns', 'bungee', 'reformed', 'C0M', 'vanity', 'qpert', 'gMd', 'nillyaz', 'Lear', 'Jerk', 'POACH', 'valyn', 'snirot', 'Boostio', 'Slandy', 'virt', 'Asuna', 'scratches', 'Pimzo', 'mle', 'Apoth', 'runi', 'katsumi', 'stewie2kk', 'shonk', 'Derrek', 'ethos', 'victor', 'zekken', 'mitch', 'acrian', 'KPfps', 'syfi', 'bdog', 'keenc', 'iiTzTimmy', 'sym', 'sonder', 'HUYNH', 'zombs', 'Cohburg', 'Precision', 'Stefanie', 'zam', 'BearZ', 'Noia', 'zeldris', 'Rossy', 'Will', 'clear', 'panini', 'NismO', 'Verno', 'koalanoob', 'dazzLe', 'Nurfed', 'stellar', 'crashies', 'harmful', 'TiGG', 'leaf', 'effys', 'VIC', 'Subroza', 'mummAy', 'Exalt', 'jmoh', 'TenZ', 'ardiis', 'eeiu', 'aproto', 'Wedid', 'oke', 's0m', 'tyfoon', 'Kanpeki', 'zinc', 'johnqt', 'c4Lypso', 'FaZe', 'Ange', 'meL', 'Zellsis', 'Naturee', 'edith', 'LFTOXY', 'SOTO', 'bang', 'thwifo', 'Gucc1', 'tdawgg', 'add3r', 'florescent', 'Jonaaa', 'Trick', 'sarahcat', 'Xeppaa', 'mada', 'sharky', 'furbsa', 'moose', 'ScrewFace', 'yay', 'flyuh', 'trent', 'dapr', 'Corey', 'ethanVAL', 'Demon1_', 'b0i', 'BcJ', 'Dark3st', 'ZexRow', 'reduxx', 'tex', 'Paincakes', 'dicey', 'neT-']

for eachplayer in player_list:
    player_percentile = math.ceil(percentile(player_list, eachplayer))
    
    player_rank = "Unranked"
    for rank in valorant_percentiles: 
        if player_percentile >= valorant_percentiles[rank]:
            player_rank = rank

    print(eachplayer + " " + str(player_percentile) + " " + player_rank)




    


