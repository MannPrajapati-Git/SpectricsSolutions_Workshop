import pandas as pd
import numpy as np

# 1. Create a Pandas DataFrame from a dictionary.
data = {
    "Name": ["Mann", "Heli", "Roshni", "DT"],
    "Age": [25, 30, 35, 40],
    "Salary": [50000, 54000, 50000, 48000]
    }
df = pd.DataFrame(data)
print(df)
print("----------")

# 2. Create a DataFrame with 5 rows and 3 columns.

data = {
    "Name": ["Mann", "Heli", "Roshni", "DT","Kadu"],
    "Age": [25, 30, 35, 40, 45],
    "Salary": [50000, 54000, 50000, 48000 , 50000]
    }
df = pd.DataFrame(data)
print(df)
print("----------")



# 3. Display the first 5 rows of a DataFrame.

df = pd.read_csv('employee_large_data.csv')
print(df.head())
print("----------")

# 4. Display the last 3 rows of a DataFrame.

df = pd.read_csv('employee_large_data.csv')
print(df.tail(3))
print("----------")


# 5. Check the shape of a DataFrame.

df = pd.read_csv('employee_large_data.csv')
print(df.shape) # rows and columns
print("----------")

# 6. Display column names of a DataFrame.

df = pd.read_csv('employee_large_data.csv')
print(df.columns)
print("----------")

# 7. Get basic information about a DataFrame using one function.

df = pd.read_csv('employee_large_data.csv')
print(df.info())
print("----------")

# 8. Select a single column from a DataFrame.

df = pd.read_csv('employee_large_data.csv')
print(df['Name'])
print("----------")

# 9. Select multiple columns from a DataFrame.

df = pd.read_csv('employee_large_data.csv')
print(df[['Name', 'Age']])
print("----------")

# 10.Select a row using iloc.

df = pd.read_csv('employee_large_data.csv')
print(df.iloc[2])
print("----------")

# 11.Select rows where a column value is greater than a given number.

df = pd.read_csv('employee_large_data.csv')
print(df[df['Age'] > 30])
print("----------")

# 12.Filter rows using multiple conditions.

df = pd.read_csv('employee_large_data.csv')
print(df[(df['Age'] > 30) & (df['Salary'] > 50000)])
print("----------")

# 13.Count the number of rows in a DataFrame.

df = pd.read_csv('employee_large_data.csv')
print(df.count())
print("----------")

# 14.Find the mean of a numeric column.

df = pd.read_csv('employee_large_data.csv')
print(df['Age'].mean())
print("----------")

# 15.Find the maximum and minimum value of a column.

df = pd.read_csv('employee_large_data.csv')
print(df['Age'].max())
print(df['Age'].min())
print("----------")

# 16.Count unique values in a column.

df = pd.read_csv('employee_large_data.csv')
print(df['Age'].unique())
print(df['Age'].nunique())
print("----------")

# 17.Sort a DataFrame by a column.

df = pd.read_csv('employee_large_data.csv')
print(df.sort_values(by='Age'))
print("----------")

# 18.Find rows with missing values.

df = pd.read_csv('employee_large_data.csv')
print(df.isnull())
print("----------")

# 19.Add a new column to a DataFrame.

df = pd.read_csv('employee_large_data.csv')
df['Bonus'] = df['Salary'] * 0.1
print(df)
print("----------")

# 20.Update values in an existing column.

df = pd.read_csv('employee_large_data.csv')
df['Age'] = df['Age'] + 1
print(df)
print("----------")

# 21.Drop a column from a DataFrame.

df = pd.read_csv('employee_large_data.csv')
df.drop('Age', axis=1, inplace=True)
print(df)
print("----------")

# 22.Rename a column in a DataFrame.

df = pd.read_csv('employee_large_data.csv')
df.rename(columns={'Name': 'First Name'}, inplace=True)
print(df)
print("----------")

# USING CSV (NUMPY & PANDAS)
# 1. Read the CSV file using Pandas.

df = pd.read_csv('employee_large_data.csv')
print(df)
print("----------")

# 2. Display the first 5 rows of the dataset.

df = pd.read_csv('employee_large_data.csv')
print(df.head())
print("----------")

# 3. Display the last 5 rows of the dataset.

df = pd.read_csv('employee_large_data.csv')
print(df.tail())
print("----------")

# 4. Find the number of rows and columns.

df = pd.read_csv('employee_large_data.csv')
print(df.shape)
print("----------")

# 5. Display column names and their data types.

df = pd.read_csv('employee_large_data.csv')
print(df.dtypes)
print("----------")

# 6. Check if there are any missing values.

df = pd.read_csv('employee_large_data.csv')
print(df.isnull())
print("----------")

# 7. Display only the Name, Department, and Salary columns.

df = pd.read_csv('employee_large_data.csv')
print(df[['Name', 'Department', 'Salary']])
print("----------")

# 8. Find all employees working in the IT department.

df = pd.read_csv('employee_large_data.csv')
print(df[df['Department'] == 'IT'])
print("----------")

# 9. Filter employees whose salary is greater than 60,000.

df = pd.read_csv('employee_large_data.csv')
print(df[df['Salary']>60000])
print("----------")

# 10.Find employees with more than 5 years of experience.

df = pd.read_csv('employee_large_data.csv')
print(df[df['Experience']>5])
print("----------")

# 11.Display all employees from Bangalore.

df = pd.read_csv('employee_large_data.csv')
print(df[df['City'] == 'Bangalore'])
print("----------")

# 12.Convert the Salary column into a NumPy array.

df = pd.read_csv('employee_large_data.csv')
print(df['Salary'].to_numpy())
print("----------")

# 13.Calculate the average salary using NumPy.

df = pd.read_csv('employee_large_data.csv')
print(df['Salary'].mean())
print("----------")

# 14.Find the maximum and minimum salary using NumPy.

df = pd.read_csv('employee_large_data.csv')
print(df['Salary'].max())
print(df['Salary'].min())
print("----------")

# 15.Increase all salaries by 10% using NumPy.

df = pd.read_csv('employee_large_data.csv')
df['Salary'] = df['Salary'] * 1.1
print(df)
print("----------")

# 16.Find the average salary for each department.

df = pd.read_csv('employee_large_data.csv')
print(df.groupby('Department')['Salary'].mean())
print("----------")

# 17.Count the number of employees in each department.

df = pd.read_csv('employee_large_data.csv')
print(df.groupby('Department')['Name'].count())
print("----------")

# 18.Find the highest salary in each department.

df = pd.read_csv('employee_large_data.csv')
print(df.groupby('Department')['Salary'].max())
print("----------")

# 19.Add a new column Bonus equal to 10% of salary.

df = pd.read_csv('employee_large_data.csv')
df['Bonus'] = df['Salary'] * 0.1
print(df)
print("----------")

# 20.Create a new column TotalIncome as Salary + Bonus.

df['TotalIncome'] = df['Salary'] + df['Bonus']
print(df)
print("----------")

# 21.Sort the dataset by salary in descending order.

df = pd.read_csv('employee_large_data.csv')
print(df.sort_values(by='Salary', ascending=False))
print("----------")

# 22.Find employees who joined after 2020 and have a performance score of 8 or more.

df = pd.read_csv('employee_large_data.csv')
print(df[(df['JoiningYear'] > 2020) & (df['PerformanceScore'] >= 8)])
print("----------")