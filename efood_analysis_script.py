# Python script for the efood analysis challege. The script is using RFM analysis to segment the customer base.
# Check read me for package installation.
# author : skar
# Date : 23-06-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# data_path = "C:\\Users\\NSkarl\\Desktop"

# import data
data = pd.read_csv("bq-results-20210610-160817-rsvk8j6pyz2z.csv")
print(data.head())

# filter specific business case
data = data[data.cuisine_parent == "Breakfast"]
data2 = data.groupby('user_id').agg({'order_id': lambda num: len(num), \
                                     'basket': lambda ordervalue: ordervalue.sum()})
data2.columns = ['frequency', 'order_value']
print(data2.head())

# save csv snapshot
# data2.to_csv(r"C:\Users\NSkarl\Desktop\user.csv")
# data2 = pd.read_csv(r"C:\Users\NSkarl\Desktop\user.csv")

# show scatter plot
plt.scatter(data2.frequency, data2.order_value)
plt.show()

# show histograms for analysis
sns.histplot(data2.frequency, bins=20)
plt.show()
sns.histplot(data2.order_value, bins = 50)
plt.show()


# perform the FM binning
data2['f_quartile'] = pd.qcut(data2['frequency'], 4, ['2', '1'], duplicates='drop')
data2['m_quartile'] = pd.qcut(data2['order_value'], 2, ['2', '1'])


data2['RFM_Score'] = data2.f_quartile.astype(str) + data2.m_quartile.astype(str)

# save csv results
data2.to_csv(r"efoodfinal.csv")