import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('sales_data.csv')

print(df.head())
print(df.dtypes)
print(df.describe())

#Line plot
plt.figure(figsize=(10, 6))
plt.plot(df['Product'], df['Quantity Sold'], marker='o', linestyle='-', color='blue')
plt.title('Quantity Sold per Product')
plt.xlabel('Date')
plt.ylabel('Quantity Sold')
plt.grid(True)
plt.savefig('quantity_sold_per_product.png')
plt.show()

#Bar plot
plt.figure(figsize=(10, 6))
df.groupby('Product')['Quantity Sold'].sum().plot(kind='bar', color='orange')
# sns.barplot(x='Product', y='Quantity Sold', data=df)
plt.title('Quantity Sold per Product')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.grid(True)
# plt.savefig('quantity_sold_per_product_bar.png')
plt.show()

#histogram
plt.figure(figsize=(10, 6))
plt.hist(df['Quantity Sold'], bins=10, color='green', edgecolor='black')
plt.title('Histogram of Quantity Sold')
plt.xlabel('Quantity Sold')
plt.ylabel('Product')
plt.grid(True)
# plt.savefig('quantity_sold_histogram.png')
plt.show()