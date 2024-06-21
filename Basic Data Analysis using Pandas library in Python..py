import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('C:\\Users\\mdazi\\Downloads\\Data.csv')

# Display the first few rows of the DataFrame
print("Initial DataFrame:")
print(df)


# Fill missing values with 0
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values:")
print(df_filled)

# Drop rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)


# Remove duplicate rows based on all columns
df_no_duplicates = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)


# Filter rows where 'Age' is greater than 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame where Age > 30:")
print(filtered_df)


# Sort the DataFrame by 'Age' in descending order
sorted_df = df.sort_values(by='Age', ascending=False)
print("\nDataFrame sorted by Age (descending):")
print(sorted_df)


# Group by 'Department' and calculate the mean of each group
grouped_df = df.groupby('Department').mean()
print("\nGrouped DataFrame by Department (mean values):")
print(grouped_df)
