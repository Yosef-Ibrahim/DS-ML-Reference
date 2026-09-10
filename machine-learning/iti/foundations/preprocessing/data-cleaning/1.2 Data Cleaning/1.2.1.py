# Import Libraries

from sklearn.impute import SimpleImputer
import numpy as np
#----------------------------------------------------


# Cleaning data

'''
impute.SimpleImputer(missing_values=nan, strategy='mean’, fill_value=None, verbose=0, copy=True)
'''

ImputedModule = SimpleImputer(missing_values = np.nan, strategy ='mean')
ImputedX = ImputedModule.fit_tranform(X)



#X Data
print('X Data is \n' , X[:10])

#y Data
print('y Data is \n' , y[:10])