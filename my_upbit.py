import datetime
# import threading
from my_upbit_class import Myupbit

access_key = "NKKTfqpYqMKYWbbwJSkn5rEQPuJg35ExOr8Hpst2"
secret_key = "2vhZZI6h9yP4vzBLJa2cMlx1UJgMmj2u7dKBRCun"
goias_upbit = Myupbit(access_key, secret_key)

# 파일명 생성
now = datetime.datetime.now()
file_name = now.strftime("%Y%m%d_%H%M%S.txt")

# 파일 생성 및 Open
with open(file_name, "a") as f:
    # 로그파일의 Header 작성
    title_txt = "buy_sell,date_time,symbol,전일종가,현재가,전일대비(%),등락,주문금액"
    f.write(title_txt + "\n")   

    # 루프를 돌림
    while True:
        goias_upbit.watch_and_order_many(f, "BTC/KRW", 6000, 0.5)   # f : 파일패스 및 파일명을 던져준다
        goias_upbit.watch_and_order_many(f, "DOGE/KRW", 6000, 0.5)
        goias_upbit.watch_and_order_many(f, "XRP/KRW", 6000, 0.5)
        
        # if not thread.is_alive():    
        #     break
        #     # infos = goias_upbit.fetch_ticker("BTC/KRW")    # 

        # goias_upbit.watch_and_order("BTC/KRW", 6000, 0.5)
        # goias_upbit.watch_and_order("DOGE/KRW", 6000, 0.5)
        # goias_upbit.watch_and_order("XRP/KRW", 6000, 0.5)

    # 로그 파일 내용 확인
    with open(file_name, "r") as f:
        print(f.read())

# import ccxt

# bithumb = ccxt.bithumb()
# bithumb.load_markets()

# infos = bithumb.fetch_ticker('DOGE/KRW')
# print(infos)



