# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:56:51 2018

@author: 爸比
"""

import openpyxl as xls

wb = xls.Workbook()
ws = wb.active

ws.append([1,2,3])

wb.save('text.xlsx')


