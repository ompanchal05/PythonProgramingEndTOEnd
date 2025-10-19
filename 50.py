# Basic Seaborn Example
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load a sample dataset
data = sns.load_dataset('tips')   # Built-in dataset

# View first few rows
print(data.head())

# Set basic style
sns.set_style("whitegrid")

# 1️⃣ Histogram
sns.histplot(data['total_bill'], kde=True)
plt.title("Distribution of Total Bill")
plt.show()

# 2️⃣ Scatter Plot
sns.scatterplot(x='total_bill', y='tip', data=data, hue='sex')
plt.title("Tip vs Total Bill")
plt.show()

# 3️⃣ Box Plot
sns.boxplot(x='day', y='total_bill', data=data)
plt.title("Box Plot - Total Bill by Day")
plt.show()

# 4️⃣ Pair Plot
sns.pairplot(data, hue='sex')
plt.suptitle("Pairplot of Tips Dataset", y=1.02)
plt.show()

# 5️⃣ Heatmap (Correlation)
corr = data.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
