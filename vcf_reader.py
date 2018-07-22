# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 18:12:52 2018

@author: Y.F. Liu
"""

import vcf

vcf_reader = vcf.Reader(open('example.txt', 'r'))


for record in vcf_reader:
    print (record)