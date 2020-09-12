import requests,time



url = 'https://api.seniverse.com/v3/weather/now.json?key=SNWyN3Clu9qlESegd&location=%s'

data = ('深圳', '成都', '拉萨', '北京')
for i in data:
    res = requests.get(url % i)
    print(res.json()['results'][0]['location']['name']+'\t'+res.json()['results'][0]['now']['text']+'\t'+res.json()['results'][0]['now']['temperature'])
    time.sleep(6)