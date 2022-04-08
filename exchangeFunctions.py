import ccxt
from binance.client import Client
def get_cash(exchange):
    wallet = exchange.privateGetWalletBalances()['result']
    cash = []
    for t in wallet:
        if float(t['availableWithoutBorrow']) > 0:
            currentToken = f"{t['coin']}: {t['availableWithoutBorrow']}"
            cash.append(currentToken)
    return cash



def create_buy_order_market(exchange,pair,side,size):
    # Order Parameter
    import requests
    import json
    url = 'https://ftx.com/api/markets/'
    session = requests.Session()
    r = session.get(url + pair)
    price = (r.json()['result']['price'])
    quantity = float(size)/int(price)
    types = 'market'

    print(exchange.create_order(pair, types, side, quantity))
    print("{} Buy Order Created")

def create_buy_order_marketBinance(binanceApiKey, binanceSecretKey, size, pair,side):
    binanceClient = Client(binanceApiKey, binanceSecretKey)
    price = binanceClient.get_symbol_ticker(symbol=pair)
    print(price)
    print(float(price['price']))
    print(size)
    quantity = float(size)/float(price['price'])
    quantity = float(round(quantity, 0))
    print(quantity)
    try:
        while True:
            buy_limit = binanceClient.futures_create_order(symbol=pair,side=side, type='MARKET', quantity=quantity)
            print(buy_limit)
            # order = binanceClient.futures_get_all_orders(symbol='BNBUSDT', limit=1)
            if buy_limit:

                print(
                    f"order {buy_limit[0]['orderId']} has been placed on BNB with {buy_limit[0]['origQty']}")
                return 'Совершена покупка ' + str(size) + ' BNB'
                print('я хуй')
                break
            else:
                continue
                print('Could not get last order from Binance!')
    except Exception as e:
        print(e)

