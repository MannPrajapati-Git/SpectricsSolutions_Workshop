import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# 1. Load the Excel dataset using Pandas and display first 10 rows.
data = pd.read_excel('practice.xlsx')
print(data.head(10))

# 2. Display dataset shape and create a simple bar chart showing total rows vs total columns.

# total_rows = len(data)
# total_cols = len(data.columns)
# shape = data.shape
# print(shape)
# plt.bar(['Rows', 'Columns'], [total_rows, total_cols])
# plt.title("Total Rows vs Total Columns")
# plt.xlabel("Rows/Columns")
# plt.ylabel("Count")
# plt.show()

# 3. Display column names and plot a bar chart showing length of each column name.

# col = data.columns
# print("Column Names:\n", col)
# lengths = [len(c) for c in col]
# plt.figure(figsize=(10, 6)) 
# plt.bar(col, lengths, color='skyblue')
# plt.title("Length of each column name")
# plt.xlabel("Columns")
# plt.ylabel("Length (Number of Characters)")
# plt.xticks(rotation=60)
# plt.tight_layout()  
# plt.show()

# 4. Check data types of all columns and visualize numeric vs non-numeric column count.

print(data.dtypes)
is_numeric = data.dtypes.apply(lambda x: 'Numeric' if x in ['int64', 'float64'] else 'Non-Numeric')
is_numeric.value_counts().plot(kind='bar', color=['skyblue', 'orange'])
plt.title("Numeric vs Non-Numeric Column Count")
plt.ylabel("Number of Columns")
plt.xticks(rotation=60)
plt.tight_layout()
plt.show()



# 5. Convert signup_date column to datetime format and plot number of signups per year.



# 6. Check for missing values in each column and visualize missing values using bar chart.
# 7. Count total number of customers and create a single bar chart representing total count.
# 8. Count number of unique cities and visualize top 5 cities using bar chart.
# 9. Count number of unique states and plot state distribution using pie chart.
# 10. Display only first_name, email, city and visualize city frequency using horizontal bar chart.
# 11. Filter customers whose age is greater than 25 and plot age distribution histogram.
# 12. Filter customers from a specific state and plot their age distribution.
# 13. Filter customers who signed up after a specific year and plot signup trend.
# 14. Sort customers by age (ascending) and plot line graph of sorted ages.
# 15. Sort customers by signup_date (descending) and plot signup timeline.
# 16. Filter customers whose email contains "gmail" and compare count vs non-gmail using bar chart.
# 17. Filter customers whose first_name starts with 'A' and plot their city distribution.
# 18. Filter customers between age 20 and 35 and compare with other age groups using bar chart.
# 19. Display top 10 youngest customers and plot their ages using line graph.
# 20. Display top 10 oldest customers and visualize their age comparison using bar chart.
# 21. Calculate mean, median, std of age using NumPy and visualize age distribution using histogram
# 22. Find minimum and maximum age using NumPy and highlight them on a bar chart
# 23. Calculate 25th, 50th, 75th percentile of age and visualize using boxplot
# 24. Normalize age column using NumPy formula and plot normalized age distribution
# 25. Create age frequency distribution using NumPy and plot bar chart
# 26. Calculate variance of age and compare actual vs mean age using line graph
# 27. Identify customers above average age and visualize comparison bar chart
# 28. Create age bins using NumPy and visualize grouped histogram
# 29. Calculate z-score of age and plot scatter plot of z-scores
# 30. Compare age distribution between two states using histogram
# 31. Extract signup year and calculate yearly customer growth using Pandas, compute growth % using
# NumPy, plot line graph
# 32. Extract signup month and visualize monthly trend using bar chart
# 33. Calculate cumulative customer count per year using NumPy and plot cumulative line graph
# 34. Compare signup trend between top 3 states using multi-line graph
# 35. Calculate moving average of monthly signups using NumPy and plot trend
# 36. Identify peak signup month and highlight it in graph
# 37. Compare weekday vs weekend signups and visualize using bar chart
# 38. Create pivot table (year vs state), convert to NumPy array and visualize heatmap
# 39. Calculate yearly growth rate and visualize using line graph
# 40. Create subplot dashboard (Yearly trend + Monthly trend)
# 41. Calculate customer count per city and plot horizontal bar chart
# 42. Find top 5 cities and visualize percentage share using pie chart
# 43. Calculate average age per state and plot bar chart
# 44. Compare average age of top 3 states using grouped bar chart
# 45. Create stacked bar chart (state vs age group)
# 46. Calculate state-wise age variance using NumPy and visualize
# 47. Identify city with maximum customers and highlight in bar graph
# 48. Compare top 3 cities age distribution using multiple histograms
# 49. Create scatter plot of city index vs average age
# 50. Create 2x2 subplot dashboard (City Count, State Count, Avg Age, Age Histogram)
# 51. Create correlation matrix using Pandas and visualize using imshow
# 52. Calculate age density distribution using NumPy and plot
# 53. Identify outliers in age using IQR method and visualize
# 54. Compare mean vs median age per state using grouped bar chart
# 55. Create cumulative age distribution graph
# 56. Calculate standard deviation per state and visualize
# 57. Create boxplot comparing age distribution across states
# 58. Calculate percentage contribution of each state and visualize donut chart
# 59. Create ranking based on signup count and visualize ranking chart
# 60. Compare customers above 30 vs below 30 using pie chart
# 61. Create complete demographic dashboard (Age histogram + State bar + Signup trend)
# 62. Create advanced pivot heatmap (State vs Age Group)
# 63. Calculate growth trend and overlay moving average
# 64. Compare top 5 cities yearly signup trend
# 65. Create regression-style scatter plot (Signup year vs count)
# 66. Build multi-line graph comparing state-wise growth
# 67. Create final analytics dashboard with 4 subplots combining:
# • Age distribution
# • State distribution
# • Signup yearly trend
# • Top cities comparison