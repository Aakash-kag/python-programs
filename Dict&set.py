# Dictionary & Set in python 

dict = {
    "surname" : ["kag","varfa","pawar"],
    "topics" : ("dict","set"),
    "name" : "Aakash",
    "cgpa" : 8.1,
    "marks" : [98,97,85]
}

# print(dict["name"])
# print(dict["cgpa"])
# print(dict["mark"])

student = {
    "name" : "rahul kumar",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

#nested dictonary !

# print(list(student.values()))

# print(student.get("name2"))
# print("hello world")
# print(student["name2"])
# print("i am aakash")

new_dict = {"city" : "delhi"}
student.update(new_dict)

# print(student)

collection = {1,2,3,4}

print(collection)
print(type(collection))

#Question about dictionary in python 

# 1. Store following word meanings in a python dictionary :

meaning = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture" , "list of facts & figures"]
}

print(meaning)

# 2.You are given a list of subjects for student.Assume one classroom 
# is required for 1 subject.How many classrooms are needed by all students.
subject = {
    "python","java","c++","javascript","java",
    "python","java","c++","c"
}

print(len(subject))

# 3.  write a program to enter marks of 3 subjects from the
# user and store them in a dictionary.Start with an empty
# dictionary & add one by one.Use subject name as key & marks as value.

marks = {}

chem = int(input("enter chemistry marks"))
marks.update({"chemistry" : chem})
phy = int(input("enter physics marks"))
marks.update({"physics " : phy})
bio = int(input("enter biology marks"))
marks.update({"biology ": bio})

print(marks)


# 4. Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

values = {
    ("float",9.0),
    ("int",9)
}
print(values)