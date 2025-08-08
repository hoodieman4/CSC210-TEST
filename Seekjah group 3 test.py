import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Sample data creation
df_sales = pd.read_csv('sales_dataset.csv')

# 1. Bar chart: Count of sales by region
plt.figure(figsize=(6,4))
df_sales['Region'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Sales Count by Region')
plt.ylabel('Count')
plt.show()

# 2. Pie chart: Sales channel distribution
plt.figure(figsize=(6,6))
df_sales['Sales_Channel'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightgreen'])
plt.title('Sales Channel Distribution')
plt.ylabel('')
plt.show()

# 3. Histogram: Units sold distribution
plt.figure(figsize=(6,4))
df_sales['Units_Sold'].plot(kind='hist', bins=20, color='blue', edgecolor='black')
plt.title('Distribution of Units Sold')
plt.xlabel('Units Sold')
plt.show()

# 4. Boxplot: Unit price by product category
plt.figure(figsize=(6,4))
df_sales.boxplot(column='Unit_Price', by='Product_Category')
plt.title('Unit Price by Product Category')
plt.suptitle('')
plt.ylabel('Unit Price')
plt.xlabel('Product Category')
plt.show()

# 5. Scatter plot: Units sold vs revenue
plt.figure(figsize=(6,4))
plt.scatter(df_sales['Units_Sold'], df_sales['Revenue'], alpha=0.5, color='purple')
plt.title('Units Sold vs Revenue')
plt.xlabel('Units Sold')
plt.ylabel('Revenue')
plt.show()

# 6. Line chart: Average revenue by discount bins
discount_bins = pd.cut(df_sales['Discount'], bins=np.linspace(0, 0.5, 6))
avg_revenue_by_discount = df_sales.groupby(discount_bins)['Revenue'].mean()
plt.figure(figsize=(6,4))
avg_revenue_by_discount.plot(kind='line', marker='o', color='blue')
plt.title('Average Revenue by Discount')
plt.xlabel('Discount Range')
plt.ylabel('Average Revenue')
plt.show()

# 7. Stacked bar: Product category by sales channel
plt.figure(figsize=(6,4))
category_channel = pd.crosstab(df_sales['Product_Category'], df_sales['Sales_Channel'])
category_channel.plot(kind='bar', stacked=True, colormap='coolwarm')
plt.title('Product Category by Sales Channel')
plt.ylabel('Count')
plt.show()

# 8. Violin plot: Distribution of revenue by region
plt.figure(figsize=(6,4))
sns.violinplot(data=df_sales, x='Region', y='Revenue', palette='Pastel1')
plt.title('Revenue Distribution by Region')
plt.show()

# 9. Horizontal bar: Average unit price by region
plt.figure(figsize=(6,4))
df_sales.groupby('Region')['Unit_Price'].mean().sort_values().plot(kind='barh', color='teal')
plt.title('Average Unit Price by Region')
plt.xlabel('Average Unit Price')
plt.show()
