# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 16:04:45 2018

@author: 爸比
"""
import requests
#import json
from bs4 import BeautifulSoup

res = requests.get('https://www.ncbi.nlm.nih.gov/nuccore/NM_000546.5?report=fasta')
soup = BeautifulSoup(res.text, "html.parser")

print(soup)