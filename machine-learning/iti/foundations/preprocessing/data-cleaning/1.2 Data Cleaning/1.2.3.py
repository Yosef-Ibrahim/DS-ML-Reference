import numpy as np

from sklearn.impute import SimpleImputer

data = np.array([[1,2,np.nan],
        [3,np.nan,1],
        [5,np.nan,0],
        [np.nan,4,6 ],
        [5,0,np.nan],
        [4,5,5]])
print(data.shape)
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp = imp.fit(data)


modifieddata = imp.transform(data)
print(modifieddata)
