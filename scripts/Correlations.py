import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('data/Mall_Customers.csv')  # Relative path to the file

# Display the first few rows
print(df.head())

# Plot distributions
plt.figure(figsize=(15, 6))
n = 0
for x in ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']:  # Ensure column names match
    n += 1
    plt.subplot(1, 3, n)
    plt.subplots_adjust(hspace=0.5, wspace=0.5)
    sns.histplot(df[x], bins=20, kde=True)  # Use sns.histplot
    plt.title(f'Distplot of {x}')
plt.show()
