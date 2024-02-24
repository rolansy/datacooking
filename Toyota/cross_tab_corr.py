# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:34:17 2024

@author: ronal
"""
import pandas as pd
carsdata=pd.read_csv("D:/Python/datacooking/Toyota/Toyota.csv",index_col=0,na_values=['????','??'])
carsdatacopy=carsdata.copy()
#frequenytable
print(pd.crosstab(index=carsdatacopy['FuelType'],columns='count',dropna=True))
#twowaytable
print(pd.crosstab(index=carsdatacopy['Automatic'],columns=carsdatacopy['FuelType'],dropna=True))
#two way table joint probability
print(pd.crosstab(carsdatacopy['Automatic'],columns=carsdatacopy['FuelType'],normalize=True,dropna=True))
#marginal probability
print()
print(pd.crosstab(index=carsdatacopy['Automatic'],columns=carsdatacopy['FuelType'],normalize=True,margins=True,dropna=True))
#conditional probability
#p(fueltype),given automatic has occured
print()
print(pd.crosstab(carsdatacopy['Automatic'],columns=carsdatacopy['FuelType'],margins=True,dropna=True,normalize='index'))
#p(automatic) given fueltype has occured
print()
print(pd.crosstab(carsdatacopy['Automatic'],columns=carsdatacopy['FuelType'],margins=True,normalize='columns',dropna=True))

numerical_data=carsdatacopy.select_dtypes(exclude=[object])
print(numerical_data.shape)

#correlation of numerical variables
#default method='pearson'
corr_data=numerical_data.corr()
print(corr_data)
#method='kendall'
corr_data2=numerical_data.corr(method='kendall')
print(corr_data2)



