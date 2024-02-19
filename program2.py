course="AI ML"
print("I AM Learning ",course)
print("data type is ",type(course))

# Data Types and Addition of elements
# List Data Type
courseList = ["Python","Java","C"]
print("Before Append ",courseList)

courseList.append("C#")
courseList.append("JavaScript")

print("After Append ",courseList)

for single_course in courseList:
    print(single_course)

print("update")
courseList.pop(0)
print("After Pop ",courseList)