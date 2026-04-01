# 1. Immutable: Pointers to immutable objects (like integers, strings, tuples) point to the same memory location. When you change the value of an immutable object, a new memory location is created for the new value.
a = 1
b = a     # b (Pointer) in the memory for a not the value of a, so b is a copy of a.
b = 10    # Changing b does not affect a, so a = 1
print(a)  # Output: 1

#2. Mutable: Pointers to mutable objects (like lists, dictionaries, sets) point to the same memory location. When you change the value of a mutable object, it affects all pointers that reference that object because they all point to the same memory location.
a = [1, 2, 3, 4, 5]
b = a     # b (Pointer) is a reference to the same list as a
b[0] = 10 # Changing b affects a because both a and b point to the same list in memory, so a = [10, 2, 3, 4, 5]
print(a)  # Output: [10, 2, 3, 4, 5]

b = a.copy()    # b is a new list that is a copy of a, so changing b does not affect a, so a = [10, 2, 3, 4, 5]
b[0] = 20       # Changing b does not affect a, so a = [10, 2, 3, 4, 5]
print(a)        # Output: [10, 2, 3, 4, 5]  
# or
b = a[:]        # b is a new list that is a copy of a, so changing b does not affect a, so a = [10, 2, 3, 4, 5]

# 3. Sequences: Pointers to sequences (like lists, tuples, strings) point to the same memory location. When you change the value of a sequence, it affects all pointers that reference that sequence because they all point to the same memory location.
a = {'a', 'b', 'c', 10, True} # set is a mutable sequence: It can contain different types but not duplicates
b = {'a': 1, 'b': 2, 'c': 3, 10: 4, True: 5} # dictionary is a mutable sequence
c = ['a', 'b', 'c', 10, True] # list is a mutable sequence: It can contain different types and duplicates, but list can be modified after creation
d = ('a', 'b', 'c', 10, True) # tuple is an immutable sequence: It can contain different types, but tuple can't be modified after creation
e = "abc10True" # string is an immutable sequence

# Indexing and slicing: 
print(a)  # Output: {'a', 'b', 'c', 10, True} (sets are unordered, so the order of elements may vary)
print(b)  # Output: {'a': 1, 'b': 2, 'c': 3, 10: 4, True: 5}
print(c[0])  # Output: 'a'
print(d[0])    # Output: 'a'
print(e[0])    # Output: 'a'

# Iteration: We can iterate through the elements of a sequence using a for loop:
for char in e: # strings are iterable, so we can iterate through each character in the string
    print(char)  # Output: 'a', 'b', 'c', '1', '0', 'T', 'r', 'u', 'e' (each character is printed on a new line)

# Dictionaries and sets do not support indexing or slicing because they are unordered collections. However, we can iterate through their items:
for item in b: # dictionaries are iterable, so we can iterate through each key in the dictionary
    print(item)  # Output: 'a', 'b', 'c', 10, True (each key is printed on a new line)

for value in b.values(): # dictionaries are iterable, so we can iterate through each value in the dictionary
    print(value)  # Output: 1, 2, 3, 4, 5 (each value is printed on a new line)

for key, value in b.items(): # dictionaries are iterable, so we can iterate through each key-value pair in the dictionary
    print(key, value)  # Output: 'a' 1, 'b' 2, 'c' 3, 10 4, True 5 (each key-value pair is printed on a new line)

# For Loop: We can use a for loop to iterate through the elements of a sequence:
for i in range(5): # range is a built-in function that generates a sequence of numbers, so we can use it to iterate through a sequence of numbers
    print(i)  # Output: 0, 1, 2, 3, 4 (each number is printed on a new line)

for char in ["a", "b", "c", "1", "0", "T", "r", "u", "e"]: # strings are iterable, so we can iterate through each character in the string
    print(char)  # Output: 'a', 'b', 'c', '1', '0', 'T', 'r', 'u', 'e' (each character is printed on a new line)

# While Loop: We can use a while loop to iterate through the elements of a sequence:
a = 0
while a < 50:                           # The while loop continues as long as a is less than 50
    b = int(input('Say a number: '))    # Input function is used to take input from the user, so we can use it to get a number from the user
    a += b                              # a is incremented by the value of b, so the loop continues until a is greater than or equal to 50

# Functions: We can define functions to perform specific tasks. Functions are reusable blocks of code that can take input, perform operations, and return output.
def add(a, b): # This function takes two parameters a and b, and returns their sum
    return a + b
result = add(5, 10) # We can call the function with different arguments to get different results
print(result) # Output: 15

# Class: We can define classes to create objects that have attributes and methods. Classes are blueprints for creating objects, and they allow us to encapsulate data and behavior together.
class Person: # This class defines a blueprint for creating Person objects
    def __init__(self, name, age): # The __init__ method is a special method that is called when an object is created, and it initializes the attributes of the object
        self.name = name # self is a reference to the current instance of the class, so we can use it to access the attributes of the object
        self.age = age

    def greet(self): # This method defines a behavior for the Person class, and it can be called on any instance of the class
        return f"Hello, my name is {self.name} and I am {self.age} years old." # This method returns a greeting message that includes the name and age of the person
person1 = Person("Alice", 30) # We can create an instance of the Person class by calling the class with the required arguments
print(person1.greet()) # Output: "Hello, my name is Alice and I am 30 years old." (we can call the greet method on the person1 object to get the greeting message)


# Main Python's data types methods:

# 1. String Methods:
s = "Hello, World!"
print(s.upper()) # Output: "HELLO, WORLD!" (converts all characters in the string to uppercase)
print(s.lower()) # Output: "hello, world!" (converts all characters in the string to lowercase)
print(s.split(", ")) # Output: ['Hello', 'World!'] (splits the string into a list of substrings based on the specified delimiter)
print(s.replace("World", "Python")) # Output: "Hello, Python!" (replaces occurrences of a specified substring with another substring)

# 2. List Methods:
list = [1, 2, 3, 4, 5]
list.append(6) # This method adds an element to the end of the list
print(list) # Output: [1, 2, 3, 4, 5, 6]
list.remove(3) # This method removes the first occurrence of a specified value from the list
print(list) # Output: [1, 2, 4, 5, 6]
list.sort() # This method sorts the elements of the list in ascending order
print(list) # Output: [1, 2, 4, 5, 6]

# 3. Dictionary Methods:
dict = {'a': 1, 'b': 2, 'c': 3}
print(dict.keys()) # Output: dict_keys(['a', 'b', 'c']) (returns a view object that displays a list of all the keys in the dictionary)
print(dict.values()) # Output: dict_values([1, 2, 3]) (returns a view object that displays a list of all the values in the dictionary)
print(dict.items()) # Output: dict_items([('a', 1), ('b', 2), ('c', 3)]) (returns a view object that displays a list of all the key-value pairs in the dictionary)
dict.update({'d': 4}) # This method updates the dictionary with the key-value pairs
print(dict) # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}