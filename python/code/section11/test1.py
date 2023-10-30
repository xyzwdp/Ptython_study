# _*_ coding:UTF-8 _*_
import requests;
import time;
import json;

def lottery(host, type, bizType):
    req_url = f"{host}api/moyi/finance/web/v2/prizewheel/lottery/ticket/consume/v1?type={type}&bizType={bizType}&lotteryScene=''"
    newSession = requests.session()
    cookie={'cookie_name': 'cookie_value'}
    res = newSession.get(url=req_url,cookies=cookie).json()
    if (res['code'] == 200):
        time.sleep(0.1)
    else:
        print(newSession.get(req_url).status_code)

if __name__ == "__main__":
    testHost = 'http://api-qa-uuu.moyis.163.com'
    while True:
        lottery(testHost, 1, 10)

