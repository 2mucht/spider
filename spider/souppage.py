import requests
from bs4 import BeautifulSoup
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Host': 'www.lagou.com',
    'Referer': 'https://www.lagou.com/jobs/list_%E5%A2%9E%E9%95%BF%E9%BB%91%E5%AE%A2?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'user_trace_token=20181017232338-9f31a24d-d220-11e8-bc71-525400f775ce; LGUID=20181017232338-9f31a50d-d220-11e8-bc71-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; _gid=GA1.2.1427831968.1539789821; _ga=GA1.2.322102797.1539789821; JSESSIONID=ABAAABAAAGFABEFD9618FF67454A090DC18A782CA407F43; LGSID=20181019000346-64e3b69c-d2ef-11e8-82de-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539789821,1539793929,1539878631; TG-TRACK-CODE=index_search; SEARCH_ID=d60053ef0b4f410983e414c0c2735a9b; _gat=1; LGRID=20181019005823-05c6e26c-d2f7-11e8-bdf3-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539881907',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',

}

desStrSum = ''

with open("positionIds.json",'r') as load_f:
    load_dict = json.load(load_f)
countNum = 1
for postionId in load_dict:
    urlStr = 'https://www.lagou.com/jobs/'+str(postionId)+'.html'
    print(urlStr)
    html = requests.get(urlStr, headers=headers)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, 'html.parser') # 爬取网页
    positionDes = soup.select('.job_bt')
    length = len(positionDes)
    print(str(length))
    #print(positionDes)
    desStrSum = desStrSum + str(positionDes)
    print(str(countNum))
    countNum += 1
    time.sleep(2)
    if length < 1:
        print(str(positionDes))
        break


file_handle = open('des.txt', mode='w', encoding='utf-8')
file_handle.write(desStrSum)
file_handle.close()

