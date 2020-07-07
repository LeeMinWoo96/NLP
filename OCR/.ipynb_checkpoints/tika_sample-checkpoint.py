#-*- coding:utf-8 -*-
# In[1]:

from tika import parser
import re
import json


filePath = "/root/Desktop/"
fileName = "2014-20.pdf"

raw = parser.from_file(filePath+fileName)
print(raw["content"])

raw["content"]= re.sub(r"[\n]*", "", raw["content"])

dict = {"resourceName":fileName, "content":raw["content"]}

jsonVal = json.dumps(dict, ensure_ascii=False)

#print(jsonVal)


fileOut = open("/root/Desktop/sample.json", "w",encoding="utf-8")

print(jsonVal, file=fileOut)

fileOut.close()
