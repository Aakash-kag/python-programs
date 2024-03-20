#Questions based on loops

#1. Print numbers from 1 to 100.
counter = 1
while counter <= 100:
    print(counter)
    counter += 1


#2. Print numbers from 100 to 1.
count = 100
while count >= 1 :
    print(count)
    count -= 1

#3. Print the multiplication table of a number n.
n = int(input("enter any number: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1
    
#4. Print the elements of the following list using a loop:
    #[1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]

#traverse
idx = 0
while idx <= len(nums)-1:
    print(nums[idx])
    idx += 1


#5. Search for a number x in this tuple using loop:
    #(1,4,9,16,25,36,49,64,81,100)
nums2 = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter your number"))

i=0
while i < len(nums2):
    if(nums[i]==x):
        print("Found at idx", i)
    i += 1 
print(x,"is not present in any list.")
    

#6.Write a program the sum of first n natural numbers.(using while)
n = int(input("enter any positive number"))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total Sum =", sum)



# break & continue keywords:
m = 1
while m <= 5:
    print(m)
    if(m == 3):
        break
    m += 1
print("end of loop")

n = 0
while n <= 5:
    if(n == 3):
        n += 1
        continue#skip
    print(n)
    n += 1