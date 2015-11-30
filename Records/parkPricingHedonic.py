import numpy as np
import pandas as pd

import statsmodels.api as sm
df=pd.read_csv('HousesCompleteNo0s.csv', index_col=0)
df.head()
print df.mean()
#print df.SalesPrice

y = np.log(np.nan_to_num(df.SalesPrice))
X = df[np.nan_to_num(['Lot Size', 'Date Built', 'Square Feet', 'Bathroom', 'Bedroom'])]
X = sm.add_constant(X)

est = sm.OLS(y,X).fit()
print est.summary()