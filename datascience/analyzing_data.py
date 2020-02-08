import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clean_df.csv')

print(df.head())
print(df.dtypes)

#for corelation(only for those who have dtypes 'int' or 'float')
print(df[['bore','stroke','compression-ratio','horsepower']].corr())

#engine size is the potential predictor variable of price
sns.regplot(x='engine-size',y='price',data = df)
plt.ylim(0,)
#as engine size goes up the price goes up , so there is a +ve direct corelation b/w variables
plt.show()

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
