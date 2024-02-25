# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:22:51 2024

@author: ronal
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
carsdata=pd.read_csv("D:/Python/datacooking/Toyota/Toyota.csv",index_col=0,na_values=['??','????'])
carsdata.dropna(axis=0,inplace=False)
plt.scatter(carsdata['KM'],carsdata['Price'])
#plt.show()
carsdata.insert(len(carsdata.columns),'AgeKM',0)
carsdata['AgeKM']=round(carsdata['Age']/12,2)
'''sns.set(style="darkgrid")
sns.regplot(x=carsdata['AgeKM'],y=carsdata['Price'],fit_reg=True,marker='^',color='cyan')
sns.lmplot(x='KM',y='Price',data=carsdata,legend=True,palette="Set1",hue='FuelType',fit_reg=True)
'''
'''
sns.distplot(carsdata['AgeKM'],color='purple',kde=True,bins=5)
sns.countplot(x='FuelType',data=carsdata,palette="Set2")
'''
#sns.countplot(x='FuelType',data=carsdata,hue='Automatic',palette='Set1')

#sns.boxplot(x=carsdata['FuelType'],y=carsdata['Price'])

sns.boxplot(x=carsdata['FuelType'],y=carsdata['Price'],hue='Automatic',data=carsdata,palette='Set1')

f,(ax_box,ax_hist)=plt.subplots(2,gridspec_kw={"height_ratios":(.35,.65)})
sns.boxplot(x=carsdata['Price'],ax=ax_box,palette='Set1')
sns.distplot(carsdata['Price'],ax=ax_hist,kde=True,color='purple')

sns.pairplot(carsdata,kind='scatter',hue='FuelType',palette='Set1')


