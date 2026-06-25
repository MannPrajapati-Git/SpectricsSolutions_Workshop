import numpy as np

# 1. Create a 1D NumPy array of numbers from 0 to 9.
arr1 = np.array([0,1,2,3,4,5,6,7,8,9])
print("Answer 1")
print(arr1)
print("----------")

# 2. Create a 1D NumPy array of all even numbers from 2 to 20.

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

arr2 = arr[arr % 2 == 0]
print("Answer 2")
print(arr2)
print("----------")


# 3. Create a 2D NumPy array of shape (3, 3) ﬁlled with zeros.
arr3 = np.zeros((3,3))
print("Answer 3")
print(arr3) 
print("----------")

# 4. Create a 2D NumPy array of shape (4, 4) ﬁlled with ones.

arr4 = np.ones((4,4))
print("Answer 4")
print(arr4)
print("----------")

# 5. Create a NumPy array ﬁlled with a speciﬁc number (e.g., 7) of size (3, 3).

arr5 = np.full((3,3),7)
print("Answer 5")
print(arr5)
print("----------")

# 6. Create an array of numbers between 10 and 50 using np.arange().

arr6 = np.arange(10,51)
print("Answer 6")
print(arr6)
print("----------")

# 7. Create an array of 5 random integers between 1 and 100.

arr7 = np.random.randint(1,101,5)
print("Answer 7")
print(arr7)
print("----------")

# 8. Create an array of 10 random ﬂoats between 0 and 1.

arr8 = np.random.rand(10)
print("Answer 8")
print(arr8)
print("----------")

# 9. Get the shape, size, and data type of an array.
arr9 = np.array([1,2,3,4,5])
print("Answer 9")
print("Shape Of The Array is :",arr9.shape)
print("Size Of The Array is :",arr9.size)
print("Data Type Of The Array is :",arr9.dtype)
print("----------")



# 10. Convert a Python list [1, 2, 3, 4, 5] into a NumPy array.

number = [1,2,3,4,5]
arr10 = np.array(number)
print("Answer 10")
print(arr10)
print("----------")

# 11. Access the 2nd element from a 1D array.

arr11 = np.array([1,2,3,4,5])
print("Answer 11")
print(arr11[1])
print("----------")

# 12. Slice the ﬁrst 3 elements from a 1D array.

arr12 = np.array([1,2,3,4,5])
print("Answer 12")
print(arr12[0:3])
print("----------")

# 13. Create a 2D array and access a speciﬁc row and column.
arr13 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 13")
print(arr13)
print(arr13[1,1])
print("----------")


# 14. Reverse a 1D NumPy array.

arr14 = np.array([1,2,3,4,5,6])
print("Answer 14")
print(arr14[::-1])
print("----------")


# 15. Create a 3x3 identity matrix.

arr15 = np.eye(3)
print("Answer 15")
print(arr15)
print("----------")


# 16. Find the maximum and minimum value in a NumPy array.
arr16 = np.array([1,2,3,4,5,7,8,9])
print("Answer 16")
print("Maximum Value Of The Array is :",arr16.max())
print("Minimum Value Of The Array is :",arr16.min())
print("----------")


# 17. Find the sum of all elements in a NumPy array.

arr17 = np.array([1,2,3,4,5,6,7,8,9])
print("Answer 17")
print(arr17.sum())
print("----------")

# 18. Calculate the mean, median, and standard deviation of an array.

arr18 = np.array([23,34,54,65,77,88,99])
print("Answer 18")
print("Mean Of The Array is :",np.mean(arr18))
print("Median Of The Array is :",np.median(arr18))
print("Standard Deviation Of The Array is :",np.std(arr18))
print("----------")


# 19. Multiply all elements of an array by 2 using broadcasting.

arr19 = np.array([1,2,3,4,5])
print("Answer 19")
print(arr19 * 2)
print("----------")

# 20. Create two arrays and perform element-wise addition, subtraction, multiplication, and division

arr20_1 = np.array([1,2,3,4,5])
arr20_2 = np.array([6,7,8,9,10])
print("Answer 20")
print("Addition Of The Array is :",np.add(arr20_1,arr20_2))
print("Subtraction Of The Array is :",np.subtract(arr20_1,arr20_2))
print("Multiplication Of The Array is :",np.multiply(arr20_1,arr20_2))
print("Division Of The Array is :",np.divide(arr20_1,arr20_2))
print("----------")

# 21. Create a 1D array of numbers from 0 to 50 and reshape it into a (5, 10) array.

arr21 = np.arange(50)
reshaped_arr21 = np.reshape(arr21, (5,10))
print("Answer 21")
print("Original Array :")
print(arr21)
print("Reshaped Array :")
print(reshaped_arr21)
print("----------")

# 22. Flatten a 2D array into a 1D array using ravel() or ﬂatten().

arr22 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 22")
print("Ravel() Method :")
print(arr22.ravel())
print("Flatten Method :")
print(arr22.flatten())
print("----------")

# 23. Create a 4x4 array and extract the last two rows.

arr23 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print("Answer 23")
print(arr23[-2:])
print("----------")

# 24. Create a 3x3 array and extract the diagonal elements.

arr24 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 24")
print(arr24.diagonal())
print("----------")

# 25. Concatenate two 1D arrays using np.concatenate().

arr25_1 = np.array([1,2,3])
arr25_2 = np.array([4,5,6])
print("Answer 25")
print(np.concatenate((arr25_1,arr25_2)))
print("----------")

# 26. Stack two 2D arrays vertically and horizontally.

arr26_1 = np.array([[1,2,3],[4,5,6]])
arr26_2 = np.array([[7,8,9],[10,11,12]])
print("Answer 26")
print("Vertically :")
print(np.vstack((arr26_1,arr26_2)))
print("Horizontally :")
print(np.hstack((arr26_1,arr26_2)))
print("----------")

# 27. Split an array into equal parts using np.split().

arr27 = np.array([1,2,3,4,5,6])
print("Answer 27")
print(np.split(arr27,3))
print("----------")

# 28. Replace all elements greater than 10 with 10 in an array.

arr28 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("Answer 28")
print(np.where(arr28 > 10,10,arr28))
print("----------")

# 29. Create a 3x3 matrix and ﬁnd its transpose.


# 30. Create two 2D arrays and perform matrix multiplication.


# 31. Create a 3x3 matrix and ﬁnd its inverse using np.linalg.inv().


# 32. Create a 3x3 matrix and ﬁnd its determinant using np.linalg.det().


# 33. Sort a NumPy array in ascending and descending order.

arr33 = np.array([1,2,3,4,5,6,7,8,9])
print("Answer 33")
print("Ascending :",np.sort(arr33))
print("Descending :",np.sort(arr33)[::-1])
print("----------")

# 34. Find unique elements in an array using np.unique().

arr34 = np.array([1,2,2,3,3,4,5,6,7,7,7,8])
print("Answer 34")
print(np.unique(arr34))
print("----------")

# 35. Use boolean indexing to extract elements greater than a certain value.


# 36. Create an array and reshape it dynamically using reshape(-1, 1).

arr36 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Answer 36")
print(arr36.reshape(-1,1))
print("----------")

# 37. Create two arrays and ﬁnd their element-wise power (a ** b).


# 38. Create two arrays and ﬁnd their dot product.


# 39. Generate a random 3x3 array and normalize it (values between 0 and 1).


# 40. Create a 2D array and replace all even numbers with 0 using slicing and conditions.

arr40 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 40")

