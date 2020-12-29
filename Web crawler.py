import requests
import time
years=[2015]

for y in years:
    for m in range(1,13):
        param={'response':'csv','stockNo':'2330','date':''}
        param['date'] = '%d%02d01'%(y,m)
        url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY'
        r = requests.get(url,param)
        print(param['date'])
        with open(r'D:\2330\%d%02d.txt'%(y,m),'w') as f:
            f.writelines(r.text)
        time.sleep(5)
