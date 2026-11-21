
import pandas as pd
df = pd.read_csv('glass-1.csv')
df
# Question 1: How many samples are present for each glass type?
# Using value_counts()
print(df['Type'].value_counts().sort_index())
# Question 2: Calculate the average and range of RI, Na, Mg, Al
# Using NumPy for mean, median, min, max
import numpy as np
for col in ['RI', 'Na', 'Mg', 'Al']:
    arr = df[col].to_numpy()  # NumPy array requirement
    print(f"{col} -> Mean: {np.mean(arr):.4f}, Median: {np.median(arr):.4f}, Min: {np.min(arr)}, Max: {np.max(arr)}, Range: {np.max(arr)-np.min(arr):.4f}")
  # Question 2: Calculate the average and range of RI, Na, Mg, Al
# Using NumPy for mean, median, min, max
import numpy as np
for col in ['RI', 'Na', 'Mg', 'Al']:
    arr = df[col].to_numpy()  # NumPy array requirement
    print(f"{col} -> Mean: {np.mean(arr):.4f}, Median: {np.median(arr):.4f}, Min: {np.min(arr)}, Max: {np.max(arr)}, Range: {np.max(arr)-np.min(arr):.4f}")
  # Question 3: Which glass type has the highest average magnesium value?
# Using groupby()
mg_avg = df.groupby('Type')['Mg'].mean()
print(mg_avg)
print(f"Highest Average Mg: Type {mg_avg.idxmax()} with {mg_avg.max():.2f}")
# Question 4: Find the 10 samples with the highest sodium values
# Using sorting
top10_na = df.sort_values(by='Na', ascending=False).head(10)
print(top10_na[['Id', 'RI', 'Na', 'Mg', 'Al', 'Type']])
# Question 5: Check for missing values and duplicates
print("Missing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
# Question 6: Compare the average chemical values between glass types
# Using groupby() and mean()
print(df.groupby('Type')[['RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe']].mean())
# Chart 1: Glass-type bar chart
import matplotlib.pyplot as plt
df['Type'].value_counts().sort_index().plot(kind='bar')
plt.title('Number of Samples per Glass Type')
plt.xlabel('Glass Type')
plt.ylabel('Count')
plt.show()
# Chart 2: Histogram of Refractive Index (RI)
import matplotlib.pyplot as plt

plt.hist(df['RI'], bins=20)
plt.title('Distribution of Refractive Index (RI)')
plt.xlabel('RI')
plt.ylabel('Frequency')
plt.show()
print("1. Building Float has maximum samples, Tableware has minimum samples. Data is imbalanced.")
print("2. Building Non-Float has highest average Magnesium, while Vehicle Float has very low Magnesium.")
print("3. Sodium is high in all types and RI is in a narrow range (1.51 to 1.53).")
