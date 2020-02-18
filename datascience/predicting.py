import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('clean_df.csv')
print(df.head())

#linear regression y^ (y hat) = a+bX a = intercept and b = slope
from sklearn.linear_model import LinearRegression

lm = LinearRegression()

#we want to look at how highway-mpg can help us predict car price. Using simple linear regression, we will create a linear function with "highway-mpg" as the predictor variable and the "price" as the response variable.
X = df[['highway-L/100km']]
Y = df['price']
lm.fit(X,Y)

Y_hat = lm.predict(X)
print(Y_hat[0:5])
print(df['price'].head())
print(lm.intercept_)
print(lm.coef_)

X = df[['engine-size']]
Y = df['price']
lm.fit(X,Y)
Y_hat1 = lm.predict(X)
print(Y_hat1[0:5])
print(df['price'].head())
print(lm.intercept_)
print(lm.coef_)


#what if we want to predict a price with the help of more than one variable
#we use multiple linear regression
Z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-L/100km']]
lm.fit(Z,df['price'])
print(lm.intercept_)
print(lm.coef_)


#when it come to linear regression an excellent way to visualize the fit of our model is by using regression plot
#This plot will show a combination of a scattered data points (a scatter plot), as well as the fitted linear regression line going through the data. This will give us a reasonable estimate of the relationship between the two variables, the strength of the correlation, as well as the direction (positive or negative correlation).
# width = 12
# height = 10
# plt.figure(figsize=(width,height))
sns.regplot(x="highway-L/100km",y ='price',data = df)
plt.ylim(0,)
plt.show()


# A good way to visualize the variance of the data is to use a residual plot.
#
# What is a residual?
#
# The difference between the observed value (y) and the predicted value (Yhat) is called the residual (e). When we look at a regression plot, the residual is the distance from the data point to the fitted regression line.

# What do we pay attention to when looking at a residual plot?
#
# We look at the spread of the residuals:
#
# - If the points in a residual plot are randomly spread out around the x-axis, then a linear model is appropriate for the data. Why is that? Randomly spread out residuals means that the variance is constant, and thus the linear model is a good fit for this data.
sns.residplot(df['highway-L/100km'], df['price'])
plt.show()
