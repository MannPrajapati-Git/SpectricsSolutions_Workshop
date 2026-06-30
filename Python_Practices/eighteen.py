# 18. Create a dictionary of student names and marks. Print which students passed (≥50) and which failed (<50).

students = {
    "Mann" : 45,
    "Heli" : 56,
    "Divyang" : 78,
    "Roshni" : 90
}
passed = {}
failed = {}

for name, marks in students.items():
    if marks >= 50:
        passed[name] = marks
    else:
        failed[name] = marks

print("Passed Students : ", passed)
print("Failed Students : ", failed)