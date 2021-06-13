# Python script for the efood analysis challenge. The script is using RFM analysis to segment the customer base.
# Check read me for package installation.
# author : Skarlatos Nikolaos
# Date : 13/6/20

# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import data
data = pd.read_csv("bq-results-20210610-160817-rsvk8j6pyz2z.csv")

# filter & group specific business case
data = data[data.cuisine_parent == "Breakfast"]
data_grouped = data.groupby('user_id').agg({'order_id': lambda num: len(num), \
                                     'basket': lambda ordervalue: ordervalue.sum()})
data_grouped.columns = ['frequency', 'order_value']

# create/show scatter plot
sns.scatterplot(data_grouped.frequency, data_grouped.order_value)
plt.show()

# create/show histograms for analysis
sns.histplot(data_grouped.frequency, bins=20)
plt.show()
sns.histplot(data_grouped.order_value, bins=50)
plt.show()

# perform the FM binning
data_grouped['f_quartile'] = pd.qcut(data_grouped['frequency'], 4, ['2', '1'], duplicates='drop')
data_grouped['m_quartile'] = pd.qcut(data_grouped['order_value'], 2, ['2', '1'])

data_grouped['RFM_Score'] = data_grouped.f_quartile.astype(str) + data_grouped.m_quartile.astype(str)

# save csv results
data_grouped.to_csv(r"efoodfinal.csv")
