# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:38:59 2024

@author: ronal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
carsdata=pd.read_csv("D:/Python/datacooking/Toyota/Toyota.csv",index_col=0,na_values=['??','????'])
carsdata.dropna(axis=0,inplace=True)
plt.scatter(carsdata['Age'],carsdata['Price'],c='red')
plt.title("Scatter plot of Age vs Price")
plt.xlabel('Age(months')
plt.ylabel('Price')
plt.show()
'''
plt.hist(carsdata['KM'])
plt.hist(carsdata['KM'],color='red',edgecolor='yellow',bins=5)
plt.title('KM')
plt.xlabel('KiloMeter')
plt.ylabel('Frequency')'''
#counts=[968,120,10]
fueldict=dict(carsdata['FuelType'].value_counts())
counts=list(carsdata['FuelType'].value_counts())
#fuelType=('Petrol','Diesel','CNG')
fuelType=list(fueldict.keys())
index=np.arange(len(fuelType))
#plt.bar(index,counts,color=['red','blue','cyan'])
plt.bar(fuelType,counts,color=['red','blue','cyan'])
plt.title('Bar Plots of Fuel Types')
plt.xlabel('Fuel Types')
plt.ylabel('Frequency')
plt.xticks(index,fuelType,rotation=90)
plt.show()