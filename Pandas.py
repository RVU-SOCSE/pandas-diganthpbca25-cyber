import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Karan", "Sneha"],
    "Marks": [78, 85, 67, 90]
}

df1 = pd.DataFrame(data)

print("DataFrame created from dictionary:")
print(df1)


df1["Percentage"] = df1["Marks"] * 1.0

print("\nDataFrame after adding new column:")
print(df1)


df2 = pd.read_csv("Mcd.csv")

print("\nDataFrame loaded from CSV file:")
print(df2)


print("\nMissing values in each column:")
print(df2.isnull().sum())


df2.fillna(df2.mean(numeric_only=True), inplace=True)

print("\nDataFrame after filling missing values:")
print(df2)
