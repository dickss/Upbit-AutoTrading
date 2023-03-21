from my_upbit_class import Myupbit

access_key = "NKKTfqpYqMKYWbbwJSkn5rEQPuJg35ExOr8Hpst2"
secret_key = "2vhZZI6h9yP4vzBLJa2cMlx1UJgMmj2u7dKBRCun"
goias_upbit = Myupbit(access_key, secret_key)

while True:
    goias_upbit.watch_and_order_many("BTC/KRW", 6000, 0.5)
    goias_upbit.watch_and_order_many("DOGE/KRW", 6000, 0.5)
    goias_upbit.watch_and_order_many("XRP/KRW", 6000, 0.5)
    
    # infos = goias_upbit.fetch_ticker("BTC/KRW")    # 

    # goias_upbit.watch_and_order("BTC/KRW", 6000, 0.5)
    # goias_upbit.watch_and_order("DOGE/KRW", 6000, 0.5)
    # goias_upbit.watch_and_order("XRP/KRW", 6000, 0.5)


# import ccxt

# bithumb = ccxt.bithumb()
# bithumb.load_markets()

# infos = bithumb.fetch_ticker('DOGE/KRW')
# print(infos)



