# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 13:48:47 2024

@author: ronal
"""
from ageconv_kpm import agekpm
import pandas as pd
carsdata=pd.read_csv("D:/Python/datacooking/Toyota/Toyota.csv",na_values=['??','????'],index_col=0)
carsdata.insert(10,'PriceClass',"")
for i in range(0,len(carsdata['Price'])):
    if(carsdata['Price'][i]<=8450):
        carsdata['PriceClass'][i]="Low"
    elif (carsdata['Price'][i]>11950):
        carsdata['PriceClass'][i]="High"
    else:
        carsdata['PriceClass'][i]="Medium"
carsdata['PriceClass'].value_counts()
agekpm(carsdata)