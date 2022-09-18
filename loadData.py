import json
import urllib.request

def loadData():

    global dataObj
    dataObj = json.loads('gen8randombattle.json')
    
    return dataObj


