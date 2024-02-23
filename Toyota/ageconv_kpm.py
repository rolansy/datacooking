# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 14:12:00 2024

@author: ronal
"""

from km_p_mnth import kpm
import pandas as pd
carsdata=pd.read_csv("D:/Python/datacooking/Toyota/Toyota.csv",index_col=0,na_values=['??','????'])
def conv(v1,v2):
    
    return [v1/12,v2/v1]
    
def agekpm(carsdata):
    carsdata.insert(len(carsdata.columns),"AgeConverted",0)
    kpm(carsdata)
    carsdata["AgeConverted"],carsdata["KM_per_Mnth"]=conv(carsdata["Age"],carsdata['KM'])
    carsdata["AgeConverted"]=round(carsdata["AgeConverted"],2)
agekpm(carsdata)

