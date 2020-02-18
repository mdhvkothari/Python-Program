import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as stats

df = pd.read_csv('clean_df.csv')

print(df.head())
print(df.dtypes)

#for corelation(only for those who have dtypes 'int' or 'float')
print(df[['bore','stroke','compression-ratio','horsepower']].corr())

#engine size is the potential predictor variable of price
sns.regplot(x='engine-size',y='price',data = df)
plt.ylim(0,)
#as engine size goes up the price goes up , so there is a +ve direct corelation b/w variables
# plt.show()

print(df[['engine-size','price']].corr()) #which is greater than .8
print(df[['highway-L/100km','price']].corr())

#these are weak correlations
print(df[['peak-rpm','price']].corr())

#descriptive analysis which exclude NaN value and exclude object datatype
print(df.describe())
#for including object
print(df.describe(include=['object']))


print(df['drive-wheels'].value_counts())
#we convert it into frame
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
print(drive_wheels_counts)

# engine-location as variable
engine_loc_counts = df['engine-location'].value_counts().to_frame()
engine_loc_counts.rename(columns={'engine-location': 'value_counts'}, inplace=True)
engine_loc_counts.index.name = 'engine-location'
print(engine_loc_counts)

#grouping data
print(df['drive-wheels'].unique())

df_group_one = df[['drive-wheels','body-style','price']]
df_group_one = df_group_one.groupby(['drive-wheels'],as_index = False).mean()
print(df_group_one)

df_gptest = df[['drive-wheels','body-style','price']]
grouped_test1 = df_gptest.groupby(['drive-wheels','body-style'],as_index=False).mean()
print(grouped_test1)

#pivot (is like excel sheet)
grouped_pivot = grouped_test1.pivot(index ='drive-wheels',columns='body-style')
print(grouped_pivot)

grouped_pivot = grouped_pivot.fillna(0)
print(grouped_pivot)

# Correlation: a measure of the extent of interdependence between variables.
# Causation: the relationship between cause and effect between two variables.
# 1: Total positive linear correlation.
# 0: No linear correlation, the two variables most likely do not affect each other.
# -1: Total negative linear correlation.
print(df.corr())

# P-value:
#
# What is this P-value? The P-value is the probability value that the correlation between these two variables is statistically significant. Normally, we choose a significance level of 0.05, which means that we are 95% confident that the correlation between the variables is significant.
#
# By convention, when the
#
# p-value is  <  0.001: we say there is strong evidence that the correlation is significant.
# the p-value is  <  0.05: there is moderate evidence that the correlation is significant.
# the p-value is  <  0.1: there is weak evidence that the correlation is significant.
# the p-value is  >  0.1: there is no evidence that the correlation is significant.
pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

# ANOVA: Analysis of Variance
# The Analysis of Variance (ANOVA) is a statistical method used to test whether there are significant differences between the means of two or more groups. ANOVA returns two parameters:
#
# F-test score: ANOVA assumes the means of all groups are the same, calculates how much the actual means deviate from the assumption, and reports it as the F-test score. A larger score means there is a larger difference between the means.
#
# P-value: P-value tells how statistically significant is our calculated score value.
#
# If our price variable is strongly correlated with the variable we are analyzing, expect ANOVA to return a sizeable F-test score and a small p-value.
