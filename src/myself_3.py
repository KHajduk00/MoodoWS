import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data - replace this with your actual data
data = {
    'Type': ['Shirt', 'Pants', 'Dress', 'Shirt', 'Pants', 'Dress'],
    'Last_Price': [50, 30, 80, 45, 28, 75],
    'Current_Price': [60, 35, 75, 40, 25, 70],
}

# Create a DataFrame
df = pd.read_csv("src/merged_data.csv")

# Calculate percentage change
df['Percentage_Change'] = ((df['Product Price before Discount'] - df['Product Price']) / df['Product Price before Discount']) * 100

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Percentage_Change', y='Product Price', hue='Product Type', data=df, s=100)
plt.title('Price Change Analysis')
plt.xlabel('Percentage Change in Price')
plt.ylabel('Current Price')
plt.legend(title='Type')
plt.grid(True)
plt.show()

# Correlation analysis
correlation_matrix = df[['Percentage_Change', 'Product Price']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()