import ccxt
import datetime
import pandas as pd
import keyboard

#####################################
# Class 선언
#####################################
class Myupbit():
    
    # 생성자 선언 (초기에 한번 선언 및 실행 됨)
    def __init__(self, access, secret) -> None:
        # print("딱 한번만 실행")
        self.upbit = ccxt.upbit()
        self.upbit.apiKey = access
        self.upbit.secret = secret
        self.is_buy_count = False
        # self.is_buy = False    

    # 특정키(F4)가 눌리면 while loop에서 빠져나오는 메소드
    def check_f4_pressed(self):
        while True:
            if keyboard.is_pressed('ctrl+c'):
                break

    # (함수 == 메소드) 다건 가상화폐 가격 감시 및 주문
    def watch_and_order_many(self, f, symbol, money, watch_percent):
        infos = self.upbit.fetch_ticker(symbol)
        # print(infos)      # 해당 symbol의 정보 출력 (symbol, 고가, 현재가, 저가, 시작가 등등등)
        buy_sell    = "buy"
        date_time   = infos["datetime"]
        price       = infos["close"]
        preprice    = infos["previousClose"]        # 전일종가
        percent     = infos["percentage"] * 100     # 전일 종가대비 현재가 % 차이
        rounded_percent = round(percent, 2)         # 전일 종가대비 현재가 % 차이 (소숫점 2자리 반올림)
        
        if percent < watch_percent and self.is_buy_count < 100:             # 원하는 등락폭과 충 매수/매도 100번까지만 하도록 제한함
            self.is_buy_count += 1  # 매수/매도 건수 증가
            # self.upbit.create_market_order(symbol, "buy", money, 1)       # 가상화폐를 구입하라
            # print(rounded_percent)    
            if rounded_percent < 0 : 
                rounded_percent_text = "Down"
            else:
                rounded_percent_text = "UP"
            
            log_txt = f'{buy_sell},{date_time},{symbol},{preprice},{price},{rounded_percent}%,{rounded_percent_text},{money}'
            f.write(log_txt + "\n")
            #print(f"'{:03d}'.self.is_buy_count번 - {log_txt}")
            print(f"{self.is_buy_count:03d} - {log_txt}")

            # print(f'{buy_sell} - {date_time} {symbol}의 전일종가 {preprice}원, 현재가 {price}, 전일대비 {rounded_percent}% {rounded_percent_text}, {money}원 주문')
            #result_text = pd.DataFrame([[date_time, buy_sell, symbol, preprice, price, rounded_percent, rounded_percent_text, money]], columns=["date_time", "buy_sell", "symbol", "preprice", "price", "rounded_percent", "rounded_percent_text", "money"], index=["0"])
            #print(result_text)
                  