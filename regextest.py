# -*- coding: utf8 -*-
import requests, re, sys
reload(sys)
sys.setdefaultencoding('utf-8')
name_reg = b'[\xe5\xbc\xb5|\xe9\xbb\x83]+[\u4e00-\u9fa5]+'
#print(name_reg)
test = '黃三張asd張祐為fsdkf;sf黃三小'.encode()
result = re.findall(name_reg, test)
for results in result:
    print(results.decode('utf-8'))