'''
python supports several data types, including:


1. Numeric Types:
   - int: Integer type, used to represent whole numbers (e.g., 5, -10).
   - float: Floating-point type, used to represent decimal numbers (e.g., 3.14, -0.5).
   - complex: Complex number type, used to represent complex numbers (e.g., 2 + 3j).

2. Sequence Types:
   - str: String type, used to represent sequences of characters (e.g., "Hello").
   - list: List type, used to represent ordered collections of items (e.g., [1, 2, 3]).
   - tuple: Tuple type, used to represent ordered, immutable collections of items (e.g., (1, 2, 3)).

   
   3. Mapping Type:
   - dict: Dictionary type, used to represent key-value pairs (e.g., {"name": "Alice", "age": 30}).

   
   4. Set Types:
   - set: Set type, used to represent unordered collections of unique items (e.g., {1, 2, 3}).
   - frozenset: Immutable version of a set.


5. Boolean Type:
   - bool: Boolean type, used to represent True or False values.

6. None Type:
   - NoneType: Represents the absence of a value or a null value (e.g., None).
'''
# integer 

age = 3 
print(age)
print(type(age))  # <class 'int'>

# float
cgpa = 9.5
print(cgpa)
print(type(cgpa))  # <class 'float'>

#  complex
complex_number = 2 + 3j
print(complex_number)
print(type(complex_number))  # <class 'complex'>

# string
name = "Urvil"
print(name)
print(type(name))  # <class 'str'>

# boolean
is_computer_science_student = True  # can also be False
print(is_computer_science_student)
print(type(is_computer_science_student))  # <class 'bool'>