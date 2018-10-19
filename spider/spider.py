
import requests
from bs4 import BeautifulSoup
import json
import time

def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_%E5%A2%9E%E9%95%BF%E9%BB%91%E5%AE%A2?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie':'user_trace_token=20181017232338-9f31a24d-d220-11e8-bc71-525400f775ce; LGUID=20181017232338-9f31a50d-d220-11e8-bc71-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; _gid=GA1.2.1427831968.1539789821; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539789821,1539793929; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1539794106; _ga=GA1.2.322102797.1539789821; LGRID=20181018003503-9956f6b5-d22a-11e8-bd24-5254005c3644; JSESSIONID=ABAAABAAAIAACBI3A9178E71D7EC0F6AC9E09369596D8B2; TG-TRACK-CODE=search_code; SEARCH_ID=ef9ce42567c74ae682a873006fe33796',

    }
    # data = {
    #     'first': 'true',
    #     'pn': 1,
    #     'kd': '增长黑客',
    # }
    # result = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false', headers=headers, data=data)
    # #print(result.content.decode())
    # json_result = result.json()
    # positions = json_result['content']['positionResult']['result']
    # # for position in positions:
    # #     print('-'*20)
    # #     print(positions)

    positions = []
    positionsIds = []
    for x in range(1, 30):
        form_data = {
        'first': 'true',
        'pn': x,
        'kd': '产品经理',
        }
        result = requests.post('https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false', headers=headers, data=form_data)
        json_result = result.json()
        page_positions = json_result['content']['positionResult']['result']
        for position in  page_positions:
            pId = position['positionId']
            positionsIds.append(pId)
        # positions.extend(page_positions)
        time.sleep(5)
        print('===='*20)
        print(x)
        print('====' * 20)
    print('total:' + str(len(positionsIds)))
    line = json.dumps(positionsIds, ensure_ascii=False)
    print(line)
    with open('positionIds.json', 'w') as fp:
        fp.write(line)


if __name__ == '__main__':
    main()