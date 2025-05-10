# it is a process of converting one data type to another

a = 34
d = 22
print(a)

print(type(a)) # integer


b = "3" 
print(b)
print(type(b)) # string


# convert string to integer

# 1) explicit type casting.
c = int(b) # c is a variable and int(b) is a value
print(c)
print(type(c)) # integer

e = str(d)

print(e)
print(type(e)) # string 

# 2) implicit type casting
# python automatically converts one data type to another data type. implicit type casting is also called automatic type conversion.


f = 3.5

g = 4

print(f + g) # 7.5 
print(type(f + g)) # float
# python automatically converts integer to float implicitly type casting