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
