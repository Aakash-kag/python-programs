# info =[]
# n = int(input("enter size of list"))
# for i in range(n):
#     info.append(input("enter student name"))

# user = input("enter student name to find")
# if user in info:
#     print("info")
# else:
#     info.append(user)
# print(info)






studentName = []
n = int(input("enter size of list : "))
for i in range(n):
    studentName.append(input("enter student name : "))

name = input("enter different person in list.")
if name in studentName:
    studentName.remove(name)
else:
    studentName.append(name)
print(studentName)
