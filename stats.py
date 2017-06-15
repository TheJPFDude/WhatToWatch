import pandas as pd

data = pd.read_csv("calculated.csv")

mean = data['point_value'].mean()
median = data['point_value'].median()
std = data['point_value'].std()

print('Mean: %s' % mean)
print('Median: %s' % median)
print('Standard Deviation: %s' % std)