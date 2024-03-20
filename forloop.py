# nums = [1,2,3,4,5]

# for val in nums:
#     print(val)

# #Questions based on for loops
# #1. Print the elements of the following list using a loop:
#     #[1,4,9,16,25,36,49,64,81,100]
# nums = [1,4,9,16,25,36,49,64,81,100]

# for val in nums:
#     print(val)

# #2. Search for a number x in this tupe using loop:
#     #(1,4,9,16,25,36,49,64,81,100)
# tupl = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("enter any number:"))
# i=0
# for val in tupl:
#     if(val == x):
#         print("Found at idx",i)
#         break
#     i += 1 
    
#3.Write a program to find the factorial of first n numbers.(using for)
    
n = int(input("enter any number"))

fact = 1
for el in range(1,n+1):
    fact *= el
print(fact)