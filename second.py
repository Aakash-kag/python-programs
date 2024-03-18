import random
fruits=['orange','gavava','cherry']
addfruit = input("enter any fruitname")

if addfruit.lower() in fruits :
    print('already exsist')
else:
    fruits.append(addfruit.lower())
 
print(fruits)