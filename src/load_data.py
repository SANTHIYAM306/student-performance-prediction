import pandas as pd

# Load the dataset
df = pd.read_csv("data/student-mat.csv", sep=";")

# Display first 5 rows
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())