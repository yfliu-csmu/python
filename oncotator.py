# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 22:09:15 2018

@author: 爸比
"""
import openpyxl as xls

fn = open('oncotator.maf.txt')
wb = xls.Workbook()
ws = wb.active

for line in fn.readlines():
    if (line[0] != '#'):
        words = line.split('\t')
        ws.append(words)

fn.close()
wb.save('tt.xlsx')
