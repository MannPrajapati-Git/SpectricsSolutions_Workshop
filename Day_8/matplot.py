import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

# Line Chart
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])
plt.plot(xpoints, ypoints)
plt.show()


# line chart with labels
x = [1, 2, 3, 4]
y = [2, 3, 5, 54]
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()

# bar chart
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 7, 12]
plt.bar(categories, values, color='red')
plt.title("Bar Chart Example")
plt.show()


# line chart with styke
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker='o', linestyle='--', color='green')
plt.title("Line with Markers")
plt.show()

# horizontal bar chart
categories = ['Apple', 'Banana', 'Mango']
values = [40, 70, 30]
plt.barh(categories, values, color='orange')
plt.title("Fruit Sales")
plt.show()

# pie chart
labels = ['Python', 'C++', 'Java']
sizes = [45, 30, 25]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Programming Language Usage")
plt.axis('equal')
plt.show()


# scatter chart
x = [5, 6, 7, 8, 9]
y = [1, 3, 2, 5, 4]
plt.scatter(x, y, color='darkblue', marker='*')
plt.title("Simple Scatter Plot")
plt.show()

# line(plot) + bar chart both
x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 3, 5, 7]
plt.plot(x, y1, label="Even", color='blue')
plt.bar(x, y2, label="Odd", color='green')
plt.legend()
plt.title("Multiple Lines")
plt.show()

# subplots
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Left Plot")

plt.subplot(1, 2, 2)
plt.bar(['A', 'B', 'C'], [3, 5, 7])
plt.title("Right Plot")

plt.tight_layout() # for good looking
plt.show()


# for saving the chartc:\Users\MANN PRAJAPATI\Downloads\MATPLOTLIB_Task.pdf c:\Users\MANN PRAJAPATI\Downloads\SQL_Practice_Dataset.xlsx
x = [1, 2, 3]
y = [10, 20, 30]
plt.plot(x, y)
plt.title("Saved Plot Example")
plt.savefig("my_plot.png")  # Saves the figure as an image
plt.show()