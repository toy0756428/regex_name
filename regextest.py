# -*- coding: utf8 -*-
import requests, re, sys
name_reg = r'[\u4e00-\u9fa5]+'
test = '黃三張asd張祐為fsdkf;sf黃三小'
#print(test)
result = re.findall(name_reg, test)
#print(result)
for results in result:
    print(results)
