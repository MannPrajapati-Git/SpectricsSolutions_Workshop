import pandas as pd

# CSV read karo
df = pd.read_csv("data.csv")

# 1) Default print
# print("===== 1) Default print(df) =====")
# print(df)

# 2) .to_string() => force ALL rows & ALL columns show kare
# print("\n===== 2) df.to_string() =====")
# print(df.to_string())

# 3) Show max_rows & max_columns default values
# print("\n===== 3) Default max_rows & max_columns =====")
# print("max_rows:", pd.options.display.max_rows)
# print("max_columns:", pd.options.display.max_columns)

# pd.describe_option("display")


# 4) Change max_rows = 22 (atle ek vaar ma 22 rows j display karse)
# pd.options.display.max_rows = 6
# print("\n===== 4) After setting max_rows = 22 =====")
# print(df)

# 5) Change max_columns = 10 (atle ek vaar ma max 10 columns j display karse)
pd.options.display.max_columns = 1
print("\n===== 5) After setting max_columns = 10 =====")
print(df)


# Examples!

# df = pd.read_csv('data.csv')
# print(df)sss

# print(df['Duration'])
# print(df['Pulse'])
# print(df['Maxpulse'])
# print(df['Calories'])

# adults = df[df['Duration'] > 25]
# print(adults)

# sorted_df = df.sort_values(by='Maxpulse')
# print(sorted_df)


# print(df.tail()) # last 5 rows
# print(df.head(10)) # first 10 rows

# print(df.columns)

# print(df.describe())

# print("Average Duration:", df['Duration'].mean())
    
# print("Maximum Pulse:", df['Pulse'].max())
# print("Minimum Pulse:", df['Pulse'].min())

# print("Minimum Calories:", df['Calories'].min())
# print("Maximum Calories:", df['Calories'].max())
# print("Average Calories:", df['Calories'].mean())

# print(df[df['Duration'] > 50])

# print(df.sort_values(by='Calories', ascending=False).head()) #Top 5 rows with highest Calories.

# print(df.groupby('Duration')['Calories'].mean())
