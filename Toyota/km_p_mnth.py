# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:32:01 2024

@author: ronal
"""
import pandas as pd
carsdata=pd.read_csv("D:/Python/datacooking/Toyota/Toyota.csv",index_col=0,na_values=['??','????'])
def kpm(carsdata):
    carsdata.insert(len(carsdata.columns),"KM_per_Mnth",0)
    
    
kpm(carsdata)    
