
import pandas as pd



df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Salary': [50000, 60000, 70000],
    'Department': ['HR', 'Finance', 'IT']
})

df3 = pd.DataFrame({
    'ID': [1, 3, 4],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Country': ['USA', 'USA', 'USA']
})


merged_df = pd.merge(df1, df2, on='ID', how='left')


final_merged_df = pd.merge(merged_df, df3, on='ID', how='outer')


print(final_merged_df)
