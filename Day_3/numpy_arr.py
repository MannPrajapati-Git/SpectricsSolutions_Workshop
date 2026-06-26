import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr) # [1 2 3 4 5]
print("----------")
print(type(arr)) # <class 'numpy.ndarray'>
print("----------")
print(arr[2]) # 3
print("----------")

arr_1d = np.array([1, 2, 3, 4, 5])  # 1D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array

print("1D Array:")
print(arr_1d) # [1 2 3 4 5]
print("----------")
print("2D Array:")
print(arr_2d) # [[1 2 3]
               # [4 5 6]]
print("----------")

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])  # 3D array
print("3D Array:")
print(arr_3d) # [[[1 2 3]
             #   [4 5 6]]
             #  [[7 8 9]
             #   [10 11 12]]]
print("----------")

# Arithmetic operations
addition = arr_1d + 2  # Add 2 to each element
subtraction = arr_1d - 2 # Subtract 2 from each element
multiplication = arr_2d * 2  # Multiply each element by 2
division = arr_2d / 2 # Divide each element by 2

print("\nArray After Addition:")
print(addition) # [3 4 5 6 7]
print("\nArray After Subtraction:")
print(subtraction) # [0 1 2 3 4]
print("Array After Multiplication:")
print(multiplication) # [[2 4 6]
                        #[8 10 12]]
print("\nArray After Division:")
print(division) # [[0.5 1.  1.5]
                  #[2.  2.5 3. ]]
print("----------")

# Accessing elements
print("Element at row 1 column 2 in 2D Array:")
print(arr_2d[1, 2])  # Access element from second row, third column
print("----------")

# Slicing
print("\nSlicing 1D Array:")
print(arr_1d[1:3])  # Access elements from index 1 to 3 (exclusive)
print("----------")

# Reshaping arrays
reshaped_array = np.reshape(arr_2d, (3,2))
print("\nReshaped 2D Array (3x2):")
print(reshaped_array) # [[1 2]
                      #  [3 4]
                      #  [5 6]]
print("----------")

# Statistical functions
mean_value = np.mean(arr_1d)
max_value = np.max(arr_2d)
std_dev = np.std(arr_1d)
print("\nStatistics:")
print("Mean of 1D Array:", mean_value)
print("Maximum in 2D Array:", max_value)
print("Standard Deviation of 1D Array:", std_dev)
print("----------")

# Creating specialized arrays
zeros_array = np.zeros((2, 3))  # 2x3 array of zeros
ones_array = np.ones((3, 2))  # 3x2 array of ones
identity_matrix = np.eye(3)  # 3x3 identity matrix
print("\nSpecial Arrays:")
print("Zeros Array:")
print(zeros_array)
print("Ones Array:")
print(ones_array)
print("Identity Matrix:")
print(identity_matrix)
print("----------")

# copying array
original_arr = np.array([1,2,3,4,5])
copy_arr = original_arr.copy()
copy_arr[2] = 99 # modifying copy array
print("Original array :", original_arr) # unchanged
print("Copy array :", copy_arr) # modified
print("----------")

# viewing array 
view_array = original_arr.view()
view_array[2] = 99 # modifying view array
print("Original array :", original_arr) # modified
print("View array :", view_array) # modified
print("----------")

# shape
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  #(2,3) number of rows and columns
print("----------")

# concatenate array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.concatenate((arr1, arr2))
print(result) # [1 2 3 4 5 6]
print("----------")

# concatenate array with axis
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
result = np.concatenate((arr1, arr2), axis=0)
print(result)
print("----------")

# The stack() function joins arrays along a new axis.
# axis = 0 -> column-wise -> vertically down
# axis = 1 -> row-wise -> horizontally
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([4, 5, 6, 7])
result = np.stack((arr1, arr2), axis=0) 
print(result)
result = np.stack((arr1, arr2), axis=1)  
print(result)
print("----------")

#The hstack() function stacks arrays horizontally (column-wise).
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.hstack((arr1, arr2))
print(result) 

#2-d array
arr1 = np.array([[1], [3]])
arr2 = np.array([[2], [4]])
result = np.hstack((arr1, arr2))
print(result)
print("----------")

#The vstack() function stacks arrays vertically (row-wise).
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
result = np.vstack((arr1, arr2))
print(result)
print("----------")

#The split() function splits an array into multiple sub-arrays along a specified axis.
arr = np.array([1, 2, 3, 4, 5, 6])
result = np.split(arr, 3)  # Split into 3 equal parts
print(result)
#Use indices to specify uneven splits:
result = np.split(arr, [2, 5])  # Split at indices 2 and 4
print(result)
#The hsplit() function splits an array horizontally (column-wise).
arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.hsplit(arr, 3)  # Split into 3 columns
print(result)
#The vsplit() function splits an array vertically (row-wise).
arr = np.array([[1, 2, 3], [4, 5, 6]])
result = np.vsplit(arr, 2)  # Split into 2 rows
print(result)
#The dsplit() function splits an array depth-wise (along the third dimension).
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
result = np.dsplit(arr, 2)  # Split into 2 depth-wise slices
print(result)
print("----------")

# Mathematical Operations
# Power and exponential functions
arr = np.array([1, 2, 3, 4, 5, 6])
powers = np.power(arr, 2)  # Square of each element
exponentials = np.exp(arr)  # Exponential of each element

print("Powers of Array Elements:")
print(powers)
print("Exponential of Array Elements:")
print(exponentials)
print("----------")

# random
import random as rm
print(rm.random()) # A random number between 0 and 1

# randint(a, b) : A random number between provided two numbers
print(rm.randint(1, 10)) 

# uniform : A random float between a and b.
print(rm.uniform(1, 10))  

# choice : chooses a random element from a given sequence
sequence = [1, 2, 3, 4, 5]
print(rm.choice(sequence))

# shuffle : Randomly shuffles the elements of a list in place.
my_list = [1, 2, 3, 4, 5]
rm.shuffle(my_list)
print(my_list) 

#numpy.random.rand(): Returns an array of random numbers between 0 and 1.
import numpy as np
arr = np.random.rand(3, 2)  # 3x2 array of random floats between 0 and 1
print(arr)

#numpy.random.randint(low, high, size): Returns a random integer array between low and high (exclusive of high).
arr = np.random.randint(1, 10, size=(2, 3))  # 2x3 array of random integers between 1 and 10
print(arr)

# numpy.random.uniform(low, high, size): Returns an array of random floats between low and high.
arr = np.random.uniform(1, 10, size=(2, 3))  # 2x3 array of random floats between 1 and 10
print(arr)

#numpy.random.choice(a, size, replace, p): Randomly selects elements from an array.
arr = np.array([1, 2, 3, 4, 5])
result = np.random.choice(arr, size=3, replace=False)  # Select 3 elements without replacement
print(result)

#numpy.random.normal(loc, scale, size): Generates random numbers from a normal (Gaussian) distribution.
arr = np.random.normal(0, 1, 5)  # 5 random numbers from a normal distribution with mean=0 and std=1
print(arr)

# Using random.seed():
rm.seed(42)
print(rm.random()) # Output: Always the same value for the same seed

np.random.seed(42)
print(np.random.rand(2, 2))  # Output: Always the same array for the same seed

# Simulate a dataset with 100 samples and 3 features
data = np.random.rand(100, 3)  # 100 rows, 3 columns of random floats between 0 and 1
print(data)
# Generate random labels (0 or 1)
labels = np.random.randint(0, 2, size=100)  # Random binary labels
print(labels)
print("----------")