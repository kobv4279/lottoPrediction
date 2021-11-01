#ip주소와 도메인 이름을 위치정보로 바꿔주는 서비스 



import requests
import json

domain_name = input('domain_name: ')
url = 'http://ip-api.com/json/'+ domain_name


response = requests.get(url)
dict1 = json.loads(response.text)
#print(dict1)


for i in dict1.keys():
    print(i, ":", dict1[i])


