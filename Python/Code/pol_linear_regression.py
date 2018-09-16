# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#auto backward elm method
import statsmodels.formula.api as sm
def auto_backward_elm(X,y, SL):
    numVars= len(X[0])
    for i in range(0,numVars):
        regressor_OLS=sm.OLS(y, X).fit()
        maxVar= max(regressor_OLS.pvalues).astype(float)
        if maxVar>SL:
            for j in range(0, numVars-i):
                if(regressor_OLS.pvalues[j] ==maxVar):
                    X=np.delete(X,j,1)
    regressor_OLS.summary()
    return X



dataset = pd.read_csv("D:\\Udemy_ML\\Polynomial_linear_regression\\Polynomial_Regression\\Position_Salaries.csv")
X= dataset.iloc[:,1:-1].values
y= dataset.iloc[:,len(dataset.columns)-1].values

"""from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3]= imputer.transform(X[:,1:3])"""

"""from sklearn.preprocessing import LabelEncoder, OneHotEncoder
oneHotEncoder = OneHotEncoder(categorical_features=[3])
labelEncoder_X= LabelEncoder()
X[:,3] = labelEncoder_X.fit_transform(X[:,3])
X=oneHotEncoder.fit_transform(X).toarray()"""


#avoiding dummy var trap
"""X=X[:,1:]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=0)"""

#Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#linear regression
from sklearn.linear_model import LinearRegression
lin_regressor= LinearRegression()
lin_regressor.fit(X, y)

#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg= PolynomialFeatures(degree=4)
X_poly= poly_reg.fit_transform(X)
lin_reg2= LinearRegression()
lin_reg2.fit(X_poly, y)

#visualize lin reg
plt.scatter(X, y, color='red')
plt.plot(X, lin_regressor.predict(X), color='blue')
plt.title('Linear Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#visualize poly reg
X_grid= np.arange(min(X), max(X), 0.1)
X_grid= X_grid.reshape(len(X_grid),1)
plt.scatter(X, y, color='red')
plt.plot(X_grid, lin_reg2.predict(poly_reg.fit_transform(X_grid)), color='blue')
plt.title('Polynomial Regression')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#predict - linear reg
ypred=lin_regressor.predict(6.5)

#predict - poly reg
ypred= lin_reg2.predict(poly_reg.fit_transform(6.5))



#backward elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((dataset.shape[0],1)).astype(int), values= X, axis=1) 
X_opt= X[:, [0,1,2,3,4,5]]
regressor_ols= sm.OLS(endog= y, exog= X_opt).fit()
regressor_ols.summary()
X_opt= X[:, [0,1,3,4,5]]
regressor_ols= sm.OLS(endog = y, exog= X_opt).fit()
regressor_ols.summary()
X_opt= X_opt[:, [0,2,3,4]]
regressor_ols= sm.OLS(endog = y, exog= X_opt).fit()
regressor_ols.summary()
X_opt= X_opt[:, [0,1,3]]
regressor_ols= sm.OLS(endog = y, exog= X_opt).fit()
regressor_ols.summary()
X_opt= X_opt[:, [0,1]]
regressor_ols= sm.OLS(endog = y, exog= X_opt).fit()
regressor_ols.summary()

#automatic backward elimination with p vals
X_opt=X[:,[0,1,2,3,4,5]]
SL=0.05
X_opt=auto_backward_elm(X_opt,y, SL)
regressor_ols= sm.OLS(endog=y, exog=X_opt).fit()


















