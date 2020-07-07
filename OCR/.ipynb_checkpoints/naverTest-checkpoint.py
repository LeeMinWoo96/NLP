import json

import base64

import requests



with open("./page_6.jpg", "rb") as f:

    img = base64.b64encode(f.read())



 # 본인의 APIGW Invoke URL로 치환

URL = ""

    

 # 본인의 Secret Key로 치환

KEY = ""

    

headers = {

    "Content-Type": "application/json",

    "X-OCR-SECRET": KEY

}

    

data = {

    "version": "V1",

    "requestId": "sample_id", # 요청을 구분하기 위한 ID, 사용자가 정의

    "timestamp": 0, # 현재 시간값

    "images": [

        {

            "name": "test",

            "format": "jpg",

            "data": img.decode('utf-8')

        }

    ]

}

data = json.dumps(data)

response = requests.post(URL, data=data, headers=headers)

res = json.loads(response.text)

fileOut = open("./naverResult.json", "w", encoding="utf-8")

print(res, file=fileOut)

fileOut.close()

import json

data = open('naverResult.json','r',encoding='utf-8')
#print(type(data.read()))
txt = data.read()
json_acceptable_string = txt.replace("'","\"")
#print(json.loads(json_acceptable_string))

dic = json.loads(json_acceptable_string)
result = ""
for i in range(len((dic['images'][0]['fields']))):
    result = result + ' ' +dic['images'][0]['fields'][i]['inferText']

print(result)

f = open("naverResult.txt", 'w')
f.write(result)

