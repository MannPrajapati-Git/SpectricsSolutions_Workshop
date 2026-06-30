# 20. Create a list of numbers and store the smallest, largest, and average value in a dictionary.

numbers = [1,2,3,4,5,43,56,77,22,11,0,65]
small = {}
large = {}
average = {}

small['small'] = min(numbers)
large['large'] = max(numbers)
average['average'] = sum(numbers)/len(numbers)

print(small)
print(large)
print(average)
