import pandas as pd

# Step 1: Load the dataset (use raw string for Windows path)
df = pd.read_csv(r'C:\Users\kanag\OneDrive\Desktop\intenship\sales_analysis\sales_data.csv')

# Step 2: Display first few rows
print("First 5 rows of data:")
print(df.head())

# Step 3: Check dataset shape (rows × columns)
print("\nDataset shape (rows, columns):")
print(df.shape)

# Step 4: Check column names
print("\nColumn names:")
print(df.columns)

# Step 5: Check data types and null values
print("\nDataset info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

# Step 6: Quick statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())