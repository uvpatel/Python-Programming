'''
 Comparison operator
Comparison operators are used to compare two values. It returns either True or False according to the condition.
Comparison operators: 

 in python = is assignment operator and == is comparison operator
Comparison operators are used to compare two values. It returns either True or False according to the condition.
   
Type of comparison operators in Python:
 1. Equal to (==)  
    2. Not equal to (!=)
    3. Greater than (>)
    4. Less than (<)
    5. Greater than or equal to (>=)
    6. Less than or equal to (<=)
    7. Identity (is)
    8. Not identity (is not)

    example:
'''

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("x == y: ", x == y) # True if x is equal to y
print("x != y: ", x != y) # True if x is not equal to y
print("x > y: ", x > y) # True if x is greater than y
print("x < y: ", x < y) # True if x is less than y
print("x >= y: ", x >= y) # True if x is greater than or equal to y
print("x <= y: ", x <= y) # True if x is less than or equal to y
print("x is y: ", x is y) # True if x is y
print("x is not y: ", x is not y) # True if x is not y
print("x in y: ", x in y) # True if x is in y



print("or, and Not operator")
print("True and False: ", True and False)
print("True and True: ", True and True)
print("False and True: ", False and True)
print("False and False: ", False and False)

print("True or False: ", True or False)
print("False or False: ", False or False)
print("True or True: ", True or True)
print("not True: ", not True)
print("not False: ", not False)