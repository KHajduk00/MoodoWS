import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV file (replace 'your_data.csv' with the actual file name)
df = pd.read_csv('src/merged_data.csv')

# Create a histogram for each type of clothing
plt.figure(figsize=(12, 8))

for clothing_type in types_of_clothing:
    subset = df[df['Product Type'] == clothing_type]
    plt.hist(subset['Product Price'], bins=20, alpha=0.7, label=clothing_type)

plt.title('Price Distribution Over Time for Different Types of Clothing')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.legend()
plt.show()