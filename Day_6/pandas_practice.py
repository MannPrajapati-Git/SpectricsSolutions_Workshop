import pandas as pd
import numpy as np

# df = pd.read_csv("data.csv")

# # default print 
# print(df) # SOME COLUMNS ARE NOT SHOWING

# # forced print
# # .to_string()
# print(df.to_string())

# # default max rows and columns
# print("Max Rows : ",pd.options.display.max_rows)
# print("Max Columns :",pd.options.display.max_columns)

# # to get desc about specific option
# # k = pd.describe_option("display")
# # print(k)

# # change max rows and columns
# changed_max_row = pd.options.display.max_rows=21
# changed_max_column = pd.options.display.max_columns=2
# print("Max 21 rows : ",changed_max_row)
# print("Max 2 columns : ",changed_max_column)

# data manipulation

df = pd.read_csv('data.csv')
print(df)

# print specific 
# print(df['Duration'])
# print("----------")
# print(df['Pulse'])
# print("----------")
# print(df['Maxpulse'])
# print("----------")
# print(df['Calories'])
# print("----------")

# conditions on specific column
adults = df[df["Duration"]>35]
print(adults)

# sort 
sorted_df = df.sort_values(by='Duration')
print(sorted_df)

# head and tail
# default = 5
print(df.tail()) # last 5 rows
print(df.head(10)) # first 10 rows

# prints column names in list 
print(df.columns)

# describes the dataframe
print(df.describe())

# Average 
print("Average Duration:",df['Duration'].mean())

# Max Min
print("Max Pulse :",df["Pulse"].max())
print("Min Pulse :",df["Pulse"].min())