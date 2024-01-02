import requests
import time
from datetime import datetime, timedelta
import sqlite3

con = sqlite3.connect("btcprice.db")
cur = con.cursor()


def get_price(coin_pair):
    #coin_pair  = "BTCFDUSD" #需要获取价格的币种对
    url = "https://api.binance.com/api/v3/ticker/price?symbol=" + coin_pair 
    response = requests.get(url)
    data = response.json()
    price = data["price"]

    # return print(data) #打印价格
    return price

while True:
    time_now = int(time.time())
    price_now = float(get_price("BTCFDUSD"))
    cmd = "insert into tp (utc, prc) values (" + str(time_now) + "," + str(price_now) + ")"
    print(cmd)
    
    time.sleep(0.1)






















