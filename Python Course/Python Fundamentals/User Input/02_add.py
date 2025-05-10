a = input("Enter a number: ")
b = input("Enter another number: ")

print(a + b) # 34 + 22 = 3422 becuase both a and b are strings so it concatenates the two strings.

a = input("Enter a number: ") # enter a number is a prompt. use prompt to ask the user for input
print(a + 3) # it thorws an error because a is a string and 3 is an integer. so we need to convert a to integer.


# solving the above problem

a = int(input("Enter a number: ")) # enter a number is a prompt. use prompt to ask the user for input
b = int(input("Enter another number: "))

print(a + b) # 34 + 22 = 56
