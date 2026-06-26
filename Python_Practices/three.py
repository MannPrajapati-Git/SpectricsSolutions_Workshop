# 3. Store 5 subject marks in a tuple. Calculate the average and print Pass if average ≥ 50, otherwise Fail.

marks = []
for i in range(5):
    mark = int(input("Enter Mark :"))
    marks.append(mark)

marks_tuple = tuple(marks)
print(marks_tuple)

avg = sum(marks) / len(marks)
print("Average : ", avg)

if avg >= 50:
    print("Pass")
else:
    print("Fail")