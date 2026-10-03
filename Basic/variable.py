#varibles it is an identifier that is used to store a value in memory. 
# It can be used to store different types of data such as numbers, strings, lists, etc. 
# In Python, variables are created when you assign a value to them.

name = "Harshad"        #in here the name is an variable and "Harshad" is a string value that is assigned to the variable name.
age = 20                #in here the age is an variable and 20 is an integer value that is assigned to the variable age.
percentage = 90.5       #in here the percentage is an variable and 90.5 is a float value that is assigned to the variable percentage.
age2 = age              #in here the age2 is an variable and age is an variable that is assigned to the variable age2.

print("My name is", name)       
print("My age is", age)           
print("My percentage is", percentage)
print("My age2 is", age2)

score = 0
score = 10
print("my score is ",score)


a = 5
b = 10
c = 5
a = b
print(a)
b = c
print(b)


price = 49
tax = 5
total = price + tax
print(total) 


item = "laptop"
original_price = 1000
discount = 200
final_price = original_price - discount

print(f"The {item} costs ${final_price} after a ${discount} discount.")
a = 5
b = 10


a, b = b, a

print(a)  # Prints 10
print(b)  # Prints 5
