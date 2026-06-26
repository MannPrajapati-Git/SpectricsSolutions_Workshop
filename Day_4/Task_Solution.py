import numpy as np

# 1. Create an array of 5 integers and display all elements.

arr1 = np.array([34,32,45,67,78])
print("Answer 1")
print(arr1)
print("----------")

# 2. Store 10 numbers in an array and print them in reverse order.

arr2 = np.array([34,12,23,35,45,56,67,78,89,90])
print("Answer 2")
print(arr2[::-1])
print("----------")

# 3. Find the sum of all elements in an array.

arr3 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Answer 3")
print(arr3.sum())
print("----------")

# 4. Find the average of array elements.

arr4 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Answer 4")
print(arr4.mean())
print("----------")

# 5. Find the maximum element in an array.

arr5 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Answer 5")
print(arr5.max())
print("----------")

# 6. Find the minimum element in an array.

arr6 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Answer 6")
print(arr6.min())
print("----------")

# 7. Count the number of even and odd elements in an array.

arr7 = np.array([1,2,3,4,5,7,6,8,9])
even = 0
odd = 0
print("Answer 7")
for i in arr7:
    if i % 2 == 0:
        even += 1
print("Even :",arr7[arr7 % 2 == 0])
print("Even Count :", even)
for i in arr7:
    if i % 2 != 0:
        odd += 1
print("Odd :",arr7[arr7 % 2 != 0])
print("Odd Count :",odd)
print("----------")

# 8. Search for a given element in an array.

arr8 = np.array([1,2,3,4,5,7,6,8,9,10])
print("Answer 8")
search = int(input("Enter Searching Element : "))
if search in arr8:
    print("Element ",search," is present in the array")
else:
    print("Element ",search," is not present in the array")
print("----------")

# 9. Count the occurrences of a specific element in an array.

arr9 = np.array([1,2,3,3,5,7,6,3,9,10])
print("Answer 9")
search = int(input("Enter Searching Element : "))
count = 0
for i in arr9:
    if i == search:
        count += 1
print(f"Element {search} is present in the array {count} times")
print("----------")

# 10. Copy all elements from one array to another.

arr10_1 = np.array([1,2,3,4,5])
arr10_2 = np.copy(arr10_1)
print("Answer 10")
print(arr10_2)
print("----------")

# 11. Merge two arrays into a third array.

arr11_1 = np.array([1,2,3])
arr11_2 = np.array([4,5,6])
print("Answer 11")
print(np.concatenate((arr11_1,arr11_2)))
print("----------")

# 12. Remove duplicate elements from an array.

arr12 = np.array([1,2,2,3,3,4,5,6,7,7,7,8])
print("Answer 12")
print(np.unique(arr12))
print("----------")

# 13. Sort an array in ascending order.

arr13 = np.array([1,2,3,4,5,6,7,8,9])
print("Answer 13")
print(np.sort(arr13))
print("----------")

# 14. Sort an array in descending order.

arr14 = np.array([1,2,3,4,5,6,7,8,9])
print("Answer 14")
print(np.sort(arr14)[::-1])
print("----------")

# 15. Find the second largest element in an array.

arr15 = np.array([1,2,3,4,5,6,7,8,9])
print("Answer 15")
print(np.sort(arr15)[-2])
print("----------")

# 16. Create a 3×3 matrix and display all elements.

arr16 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 16")
print(arr16)
print("----------")

# 17. Find the sum of all elements in a matrix.

arr17 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 17")
print(arr17.sum())
print("----------")

# 18. Find the maximum element in a matrix.

arr18 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 18")
print(arr18.max())
print("----------")

# 19. Find the minimum element in a matrix.

arr19 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 19")
print(arr19.min())
print("----------")

# 20. Find the sum of each row in a matrix.

arr20 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 20")
print(arr20.sum(axis=1))
print("----------")

# 21. Find the sum of each column in a matrix.

arr21_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Answer 21")
print(arr21_1.sum(axis=0))
print("----------")

# 22. Find the sum of the main diagonal elements.


# 23. Find the sum of the secondary diagonal elements.
# 24. Check whether a matrix is symmetric or not.
# 25. Create a 3D array of size 2×2×2 and display all elements.

arr25 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Answer 25")
print(arr25)
print("----------")

# 26. Find the sum of all elements in a 3D array.

arr26 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Answer 26")
print(arr26.sum())
print("----------")

# 27. Find the maximum element in a 3D array.

arr27 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Answer 27")
print(arr27.max())
print("----------")

# 28. Find the minimum element in a 3D array.

arr28 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print("Answer 28")
print(arr28.min())
print("----------")

# 29. Count the total number of elements in a 3D array.

arr29 = np.array([[[1,2,9],[3,4,9]],[[5,6,9],[7,8,9]]])
print("Answer 29")
print(arr29.size)
print(arr29)
print("----------")

# 30. Find all duplicate elements in an array.


# 31. Find all unique elements in an array.

arr31 = np.array([1,2,3,4,2,3,5])
print("Answer 31")
print(np.unique(arr31))
print("----------")

# 32. Rotate an array to the left by one position.


# 33. Rotate an array to the right by one position.


# 34. Rotate an array by N positions.


# 35. Find the frequency of each element in an array.



# 36. Find the third largest element in an array.

arr36 = np.array([23,45,65,12,11,89,54,0])
print("Answer 36")
sort_arr = np.sort(arr36)
print(sort_arr)
print(sort_arr[-3])
print("----------")

# 37. Reverse an array without using another array.

arr37 = np.array([34,23,54,67,98])
print("Answer 37")
print(arr37[::-1])
print("----------")

# 38. Insert an element at a specific position in an array.

arr38 = np.array([1,2,3,4,5,6,7,8,9])
print("Answer 38")
ins_arr = np.insert(arr38, 4, 34)
print(ins_arr)
print("----------")

# 39. Delete an element from a specific position in an array.

arr39 = np.array([34,23,54,67,98,12,23,54,78,67])
print("Answer 39")
del_arr = np.delete(arr39, 4)
print(del_arr)
print("----------")

# 40. Find the intersection of two arrays.

arr40_1 = np.array([1,2,3,4,5,6,7])
arr40_2 = np.array([3,4,5,6,7,8,9])
print("Answer 40")
print(np.intersect1d(arr40_1,arr40_2))
print("----------")

# 41. Find the union of two arrays.

arr41_1 = np.array([1,2,3,4,5,6,7])
arr41_2 = np.array([3,4,5,6,7,8,9])
print("Answer 41")
print(np.union1d(arr41_1,arr41_2))
print("----------")

# 42. Check whether two arrays are equal.

arr42_1 = np.array([1,2,3])
arr42_2 = np.array([1,2,3,4])
print("Answer 42")
print(np.array_equal(arr42_1,arr42_2))
print("----------")

# 43. Split an array into two equal halves.

arr43 = np.array([1,2,3,4,5,6,7,8,9,10])
print("Answer 43")
print(np.split(arr43,2))
print("----------")

# 44. Find all pairs whose sum equals a given number.

arr44 = np.array([1,2,3,4,5,6,7,8,9])
print("Answer 44")
sum_num = int(input("Enter the sum : "))
for i in range(len(arr44)):
    for j in range(i+1,len(arr44)):
        if arr44[i] + arr44[j] == sum_num:
            print(arr44[i],"+",arr44[j])
print("----------")

# 45. Find the missing number from an array containing 1 to N.

arr45 = np.array([1,2,3,4,6,7,8,9])
print("Answer 45")
print(arr45[arr45 != np.arange(1,10)])
print("----------")

# 46. Move all zeros to the end of the array.

arr46 = np.array([1,2,0,4,5,6,7,0,8,9,0])
print("Answer 46")
print(arr46[arr46 != 0])
print("----------")

# 47. Separate positive and negative numbers in an array.

arr47 = np.array([-1,-2,3,4,5,-6,7,8,9])
print("Answer 47")
print(arr47[arr47 > 0])
print(arr47[arr47 < 0])
print("----------")

# 48. Find the longest increasing sequence in an array.
# 49. Implement matrix multiplication using 2D arrays.