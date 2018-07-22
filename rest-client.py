# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:04:45 2018

@author: 爸比
"""

import requests

url = 'http://www.broadinstitute.org/oncotator/mutation/7_55259515_55259515_T_G/'
data = dict()

r = requests.get(url)

if r.status_code == requests.codes.ok:
    data = r.json()

for key in data.keys():
    print(key, data[key])
